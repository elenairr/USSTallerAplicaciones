# Guía de Despliegue en Streamlit Cloud

Sigue estos pasos para llevar tu aplicación local a la web.

## Paso 1: Subir código a GitHub
Como ya hemos inicializado el repositorio Git localmente, ahora debes vincularlo a tu cuenta de GitHub.

1.  Crea un **nuevo repositorio** en [GitHub](https://github.com/new) (ej. `bank-marketing-streamlit`).
2.  No marques "Initialize with README", "gitignore", ni "license". Crea el repo vacío.
3.  Ejecuta estos comandos en tu terminal (ajusta la URL a tu repositorio):
    ```bash
    git remote add origin https://github.com/TU_USUARIO/bank-marketing-streamlit.git
    git branch -M main
    git push -u origin main
    ```

## Paso 2: Configurar Streamlit Cloud
1.  Ingresa a [Streamlit Cloud](https://streamlit.io/cloud) y regístrate con tu cuenta de GitHub.
2.  Haz clic en **"New app"**.
3.  Selecciona tu repositorio (`bank-marketing-streamlit`).
4.  Configura los parámetros:
    *   **Branch:** `main`
    *   **Main file path:** `streamlit_app/app.py`
5.  Haz clic en **"Deploy!"**.

## Paso 3: Verificar Dependencias
Streamlit Cloud buscará automáticamente el archivo `requirements.txt` que ya hemos creado en la carpeta `streamlit_app/`.

## Paso 4: Solución de Problemas (Si ocurren errores)
*   **Error de rutas:** Hemos configurado `app.py` para usar rutas relativas seguras (`os.path.abspath`), por lo que debería funcionar bien.
*   **Versiones de Python:** Streamlit Cloud usualmente usa Python 3.9+. Tu código es compatible.

¡Listo! En unos minutos deberías tener una URL pública para compartir tu proyecto.
