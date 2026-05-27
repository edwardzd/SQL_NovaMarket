# 🚀 Guía de Despliegue: Publicando tu Dashboard en Internet

¡Felicidades! Si llegaste hasta aquí, tienes un Dashboard interactivo corriendo en tu computadora. Ahora, vamos a llevarlo al siguiente nivel: **Ponerlo en internet para que cualquier persona en el mundo pueda usarlo** (ideal para impresionar a la Junta Directiva de NovaMarket durante el evento EXPLO-RA).

Haremos esto utilizando **Streamlit Community Cloud**, un servicio oficial y 100% gratuito.

---

## 🛠️ Requisitos Previos

Antes de empezar, necesitas tener dos cosas listas:
1. **Una cuenta en GitHub** (si no tienes, crea una gratis en [github.com](https://github.com)).
2. **Los archivos vitales:** Debes subir a un repositorio en tu GitHub los siguientes dos archivos que generaste en tu proyecto:
   * `dashboard_novamarket.py` (el código de la aplicación).
   * `S01_Ventas_Novamarket_Datos_Limpios.csv` (los datos que lee el dashboard).
3. **El archivo `requirements.txt`:** Crea un archivo de texto plano en tu repositorio llamado `requirements.txt` que contenga las librerías que usas, simplemente escribe esto adentro:
   ```text
   streamlit
   pandas
   plotly
   ```

---

## 🌐 Pasos para publicar tu App

### Paso 1: Entrar a Streamlit Cloud
Ve a la página oficial: **[share.streamlit.io](https://share.streamlit.io/)** e inicia sesión usando tu cuenta de GitHub (te pedirá autorizar la conexión, dile que sí).

### Paso 2: Crear una nueva aplicación
Una vez adentro, verás tu panel principal. Haz clic en el botón azul brillante que dice **"New app"** (Nueva aplicación).

### Paso 3: Conectar con tu repositorio
Te aparecerá un formulario muy sencillo. Llénalo así:
* **Repository:** Selecciona de la lista desplegable el repositorio donde subiste tus archivos (ej. `edward/Explora-NovaMarket`).
* **Branch:** Normalmente es `main` o `master`.
* **Main file path:** Escribe exactamente el nombre de tu archivo de python: `dashboard_novamarket.py`.
* **App URL (Opcional):** ¡Aquí puedes elegir cómo se llamará tu enlace! Por ejemplo, si pones `novamarket-explora`, tu link final será `https://novamarket-explora.streamlit.app`.

### Paso 4: ¡Desplegar!
Haz clic en el botón **"Deploy!"**. 
Verás una pantalla con animaciones mientras Streamlit instala tus librerías y configura un servidor web real en la nube. Esto suele tardar entre 1 y 3 minutos la primera vez.

---

## 🎉 ¡Listo para compartir!

Cuando termine, tu dashboard aparecerá funcionando directamente en el navegador. 
Copia el enlace de la barra de direcciones y compártelo por WhatsApp, correo o preséntalo directamente en EXPLO-RA. 

> [!TIP]
> **Actualizaciones Mágicas:** La mejor parte de esto es que si encuentras un error o quieres cambiar un color, solo tienes que modificar tu código en VS Code, hacer *Push* a GitHub, y ¡tu página web se actualizará sola automáticamente en un par de minutos! No tienes que repetir este proceso nunca más.
