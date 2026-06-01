# 🐍 Guía: Entornos Virtuales en Python

¡Hola estudiante de NovaMarket! 

Al trabajar en proyectos de Python, especialmente en aquellos que utilizan múltiples librerías como Pandas o Streamlit, vas a escuchar mucho el término **"Entorno Virtual"** o **"Virtual Environment" (venv)**. 

En esta guía te explicaremos qué son, por qué los necesitamos y cómo configurarlos para el proyecto final.

---

## 1. 🤔 ¿Qué es un Entorno Virtual?

Imagina que un entorno virtual es como una "caja de arena" (sandbox) aislada dentro de tu computadora. 

Cuando instalas librerías de Python (como `streamlit` o `pandas`) de forma normal, se instalan "globalmente" en toda tu computadora. Si tienes varios proyectos, esto puede causar un caos: el Proyecto A podría necesitar la versión 1.0 de una librería, pero el Proyecto B podría necesitar la versión 2.0.

Un **entorno virtual** crea una carpeta oculta (generalmente llamada `.venv` o `venv`) dentro de la carpeta de tu proyecto. Todo lo que instales mientras este entorno esté "activado" se quedará atrapado dentro de esa carpeta y no afectará al resto de tu computadora.

## 2. ❓ ¿Por qué no subimos el entorno virtual a GitHub?

Si revisas el repositorio en GitHub, notarás que **no hay ninguna carpeta llamada `.venv`**. Esto es completamente intencional.

Los entornos virtuales contienen miles de archivos y pueden pesar cientos de megabytes. Sería muy ineficiente subir todo eso a internet. En su lugar, utilizamos un archivo de texto llamado **`requirements.txt`**.

* **`requirements.txt`**: Es como una "receta" o lista de compras. Simplemente contiene los nombres de las librerías que el proyecto necesita.
* Cuando descargas el proyecto, tú creas tu propio entorno virtual local y usas esta "receta" para instalar lo necesario.

---

## 3. 🛠️ Cómo Crear y Activar tu Entorno Virtual

Sigue estos pasos dentro de tu terminal en VS Code, asegurándote de estar en la carpeta `/Reto_Final_Python/`:

### Paso 1: Crear el entorno virtual
Ejecuta el siguiente comando en tu terminal para crear la carpeta `.venv`:

```bash
python -m venv .venv
```
*(Nota: Si usas Mac/Linux y el comando anterior no funciona, intenta usar `python3 -m venv .venv`)*

### Paso 2: Activar el entorno virtual
Antes de instalar cualquier cosa, debes "entrar" a la caja de arena. El comando varía según tu sistema operativo:

**Para Mac / Linux:**
```bash
source .venv/bin/activate
```

**Para Windows (Command Prompt o PowerShell):**
```bash
.venv\Scripts\activate
```

> [!TIP]
> **¿Cómo sé si funcionó?**
> Deberías ver un texto que dice `(.venv)` al principio de la línea en tu terminal. Esto indica que estás dentro del entorno.

### Paso 3: Instalar los requerimientos (La Receta)
Ahora que el entorno está activo, instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Esto leerá la "receta" y descargará Streamlit, Pandas, Plotly y todo lo que tu dashboard necesita para funcionar correctamente.

---

## 4. ⚙️ Seleccionar el Entorno en Visual Studio Code

A veces, VS Code necesita que le digas explícitamente que utilice este nuevo entorno para autocompletar tu código o ejecutar archivos.

1. Abre cualquier archivo `.py` (como `dashboard_novamarket.py`).
2. Presiona `Ctrl + Shift + P` (Windows) o `Cmd + Shift + P` (Mac) para abrir la Paleta de Comandos.
3. Escribe **`Python: Select Interpreter`** y presiona Enter.
4. VS Code debería mostrarte tu nuevo entorno en la lista con un nombre similar a: `Python 3.12.x ('.venv': venv)`. **Selecciónalo**.

¡Listo! Ya tienes configurado un entorno seguro y profesional, exactamente como se hace en la industria tecnológica real.
