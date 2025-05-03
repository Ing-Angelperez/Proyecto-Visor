Smart Motorcycle Helmet Visor Controlled by Eye‑Blink Detection


Link de video de prueba:

  https://drive.google.com/file/d/14yHrkGTjfc_vgV7G8wCq8YfxDMVyUtO5/view?usp=sharing

📑 Descripción

El proyecto Visor Inteligente busca aumentar la seguridad y la comodidad de los motociclistas mediante un sistema que abre y cierra automáticamente el visor de un casco cuando el usuario parpadea de forma intencional. El reconocimiento del parpadeo se realiza con visión por computadora (OpenCV + MediaPipe) corriendo en una Raspberry Pi 5; el movimiento del visor lo ejecutan motores paso a paso fijados al casco. Además, la misma interfaz habilita comandos de voz (Google Assistant/Alexa) sin soltar el manubrio.

✨ Características principales

Detección robusta de parpadeo a 30 FPS usando la cámara Raspberry Pi 5 (1080p).

Control de dos motores paso a paso NEMA‑17 para movimiento suave del visor.

Desacople de falsos positivos mediante filtrado de ángulo de vista y umbral adaptativo.

Módulo opcional de asistente de voz (p. ej. Google Assistant) invocado con doble parpadeo.

Registro de eventos y métricas en parpadeos_log.txt para análisis posterior.

🛠️ Requisitos de hardware

Componente

Cantidad

Notas

Raspberry Pi 5 (4 GB RAM +)

1

Raspbian Bookworm 64‑bit

Cámara Raspberry Pi Cam v3 (1080p)

1

FOV ≈ 60 °

Motores paso a paso NEMA‑17

2

Torque ≥ 45 N·cm

Drivers A4988 + disipador

2

Micro‑stepping 1/8

Powerbank 5 V / 3 A

1

Alimenta Pi + drivers

Batería Li‑Po 11.1 V

1

Motores (regulador DC‑DC)

Casco integral

1

Con anclaje impreso 3D

💻 Requisitos de software

tested on: Python 3.11.2 (64‑bit)
OpenCV‑Python 4.9.0.80
mediapipe‑solutions 0.10.3
RPi.GPIO 0.7.x
numpy ≥ 1.24
matplotlib ≥ 3.8

Instala todo con pip install -r requirements.txt o usa el archivo pyproject.toml.

🚀 Instalación rápida

# 1. Clona este repositorio
$ git clone https://github.com/Ing-Angelperez/Proyecto-Visor.git
$ cd Proyecto-Visor

# 2. Crea y activa un entorno virtual (opcional pero recomendado)
$ python -m venv venv
$ source venv/bin/activate   # en Windows: venv\Scripts\activate

# 3. Instala dependencias
(venv) $ pip install -r requirements.txt

# 4. Conecta la cámara y ejecuta
(venv) $ python Visor_Inteligente.py

📂 Estructura del repositorio

Proyecto_Mecatronico/
├─ Pruebas/                 # material de test local (no subido en produccion)
├─ Visor_Inteligente.py     # script principal
├─ requirements.txt         # dependencias de Python
└─ README.md

Nota: Los vídeos de prueba y el entorno virtual se excluyen mediante .gitignore para mantener el repositorio ligero.

📝 Uso básico

Ajusta los pines de los drivers A4988 en la sección CONFIG de Visor_Inteligente.py.

Coloca la cámara dentro del casco y enfoca el ojo dominante.

Ejecuta el script. Atravesarás tres estados:

Calibración – 5 s para capturar el tamaño de tu ojo abierto.

Detección de parpadeo – parpadeo intencional (> 400 ms) activa motores.

Asistente de voz – parpadeo doble abre micro.

Detén el programa con Ctrl + C.

🔭 Roadmap



🤝 Contribuir

¡Se aceptan pull requests! Por favor abre un issue primero para discutir cambios mayores.

Crea una branch: git checkout -b feature/nueva-funcionalidad

Commit tus cambios: git commit -m "Añade X"

Push a la rama: git push origin feature/nueva-funcionalidad

Abre un Pull Request.

📜 Licencia

Este proyecto se publica bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

🧑‍💻 Autor

Nombre

Contacto

Ángel Alberto Pérez López

LinkedIn • ing.angelperez@gmail.com

¡Gracias por visitar el proyecto! Si te es útil, dale ⭐ y comparte tus ideas para mejorarlo.