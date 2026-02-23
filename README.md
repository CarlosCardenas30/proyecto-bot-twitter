# Proyecto Bots - Fundamentos de Telecomunicaciones
# 🤖 Proyecto de Simulación y Análisis de Bots en Redes Sociales

Este proyecto consiste en la creación, implementación y análisis de un bot para la plataforma X (Twitter) utilizando la **API v2**. El sistema no solo publica contenido, sino que registra su actividad en una base de datos local para un análisis de datos posterior.

## 🛠️ Infraestructura Utilizada
* **Lenguaje:** Python 3.10+
* **Entorno de Desarrollo:** Google Colab
* **Librería de API:** Tweepy (v4.x)
* **Base de Datos:** SQLite (Almacenamiento local de interacciones)
* **Análisis de Datos:** Pandas
* **Hosting del Dashboard:** GitHub Pages

## 📊 Funcionamiento del Sistema
1. **Generación de Contenido:** El bot genera mensajes automáticos con marcas de tiempo para evitar duplicados.
2. **Persistencia:** Cada tweet publicado exitosamente se almacena en una base de datos SQLite (`mi_bot_data.db`).
3. **Dashboard:** Se genera un archivo `index.html` mediante Pandas que muestra el historial de publicaciones.

## 📁 Estructura del Repositorio
* `main.py`: Código principal con la lógica de conexión y funciones de base de datos.
* `index.html`: Dashboard estático generado para visualización en GitHub Pages.
* `README.md`: Documentación del proyecto (este archivo).

## 🚀 Cómo ejecutarlo
1. Clona este repositorio.
2. Instala las dependencias: `pip install tweepy pandas`.
3. Configura tus credenciales de la API de Twitter en las variables de entorno o directamente en el script (para uso local).
4. Ejecuta el script para publicar y registrar datos.

---
**Nota Académica:** Este proyecto fue desarrollado como parte del curso de Análisis de Datos en Redes Sociales, cumpliendo con los requisitos de integración de APIs y manejo de bases de datos relacionales.
