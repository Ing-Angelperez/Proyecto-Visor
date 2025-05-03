import cv2
import time
import matplotlib.pyplot as plt
import numpy as np

# === CONFIGURACIÓN ===
input_video_path = "ojo_test.mp4"
output_video_path = "video_salida_area.avi"
log_file_path = "parpadeos_log.txt"

area_threshold = 30000
min_area = 15000
max_area = 300000
retencion_ojos_frames = 10
suavizado_ventana = 5

# === CARGA ===
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
video = cv2.VideoCapture(input_video_path)
if not video.isOpened():
    raise Exception("❌ No se pudo abrir el video.")

frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

# === VARIABLES ===
last_eye = None
last_detected_frame = -retencion_ojos_frames
last_estado = None
start_time = time.time()
frame_count = 0

areas = []
tiempo = []
parpadeos = []
smooth_areas = []

blink_times = []
doble_parpadeo_umbral = 1.2  # segundos
visor_cerrado = False

with open(log_file_path, "w") as f:
    f.write("Tiempo(s),Estado\n")

plt.ion()
fig, ax = plt.subplots(figsize=(10, 4))
line_area, = ax.plot([], [], color='blue', label="Área del ojo")
ax.axhline(area_threshold, color='red', linestyle='--', label="Umbral")
ax.set_ylim(0, max_area)
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Área")
ax.set_title("Área del ojo en tiempo real")
ax.legend()
plt.show()

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    estado = "NO DETECTADO"
    area = 0
    timestamp = round(time.time() - start_time, 2)
    frame_count += 1

    if len(eyes) > 0:
        (x, y, w, h) = max(eyes, key=lambda b: b[2] * b[3])
        area = w * h

        if min_area < area < max_area:
            last_eye = (x, y, w, h)
            last_detected_frame = frame_count
            estado = "CERRADO" if area < area_threshold else "ABIERTO"
    elif frame_count - last_detected_frame < retencion_ojos_frames and last_eye:
        (x, y, w, h) = last_eye
        area = w * h
        estado = "CERRADO" if area < area_threshold else "ABIERTO"

    if estado != "NO DETECTADO":
        areas.append(area)
        tiempo.append(timestamp)
        if len(areas) >= suavizado_ventana:
            avg_area = np.mean(areas[-suavizado_ventana:])
        else:
            avg_area = area
        smooth_areas.append(avg_area)

        if estado == "CERRADO" and last_estado == "ABIERTO":
            blink_times.append(timestamp)
            blink_times = [t for t in blink_times if timestamp - t <= doble_parpadeo_umbral]

            if len(blink_times) >= 2:
                visor_cerrado = not visor_cerrado
                accion = "CERRADO" if visor_cerrado else "ABIERTO"
                print(f"[SIMULACIÓN] Visor {accion}")
                blink_times = []
            print(f"Parpadeo detectado en t={timestamp}s")

        last_estado = estado

    # === DIBUJAR ===
    if last_eye:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Area: {int(area)}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, f"Ojo: {estado}", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, f"Umbral: {area_threshold}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    out.write(frame)

    resized = cv2.resize(frame, (640, 480))
    cv2.imshow("Simulador de Visor", resized)

    # === GRAFICA ACTUAL ===
    line_area.set_data(tiempo, smooth_areas)
    ax.set_xlim(0, max(10, tiempo[-1]))
    fig.canvas.draw()
    fig.canvas.flush_events()

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()

# === GUARDAR GRAFICA FINAL ===
plt.ioff()
plt.savefig("grafica_final_area.png")
plt.show()
