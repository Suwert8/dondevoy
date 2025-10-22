# 🚀 Cómo Subir DondeVoy a GitHub (Sin Git instalado)

## Opción 1: Subir archivos directamente en GitHub.com (MÁS FÁCIL)

### Paso 1: Crear el repositorio
1. Ve a https://github.com/new
2. Nombre del repositorio: `DondeVoy2` (o el que prefieras)
3. Descripción: `Aplicación web para encontrar lugares con buen tiempo`
4. Marca como: **Public** (necesario para GitHub Pages gratis)
5. NO marques "Add a README file" (ya tienes uno)
6. Click en "Create repository"

### Paso 2: Subir archivos
1. En la página del nuevo repositorio, verás "uploading an existing file"
2. Click en ese enlace o ve a "Add file" → "Upload files"
3. Arrastra TODOS estos archivos desde `C:\Users\Usario\Desktop\DondeVoy2`:
   - `index.html` ⭐ (PRINCIPAL)
   - `manifest.json` (para PWA)
   - `README.md` (documentación)
   - `MOBILE.md` (guía móvil)
   - `start-server.ps1` (servidor local)
   - `server.py` (servidor alternativo)
   - `.gitignore` (opcional)

4. **NO SUBAS**: requirements.txt, archivos .py adicionales (no se necesitan)
5. Escribe un mensaje: "Primera versión de DondeVoy"
6. Click en "Commit changes"

### Paso 3: Activar GitHub Pages
1. Ve a "Settings" (en tu repositorio)
2. En el menú izquierdo, click en "Pages"
3. En "Source", selecciona: **Deploy from a branch**
4. En "Branch", selecciona: **main** (o master)
5. Deja la carpeta en: **/ (root)**
6. Click en "Save"

### Paso 4: ¡Listo! 🎉
- Espera 1-2 minutos
- Tu app estará en: `https://TU-USUARIO.github.io/DondeVoy2/`
- Abre esa URL en tu móvil
- ¡Instálala como PWA!

---

## Opción 2: Instalar Git primero (Más control)

### Instalar Git:
1. Descarga Git desde: https://git-scm.com/download/win
2. Instala con las opciones por defecto
3. Reinicia la terminal

### Luego ejecuta estos comandos:

```powershell
cd C:\Users\Usario\Desktop\DondeVoy2

# Configurar Git (primera vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Inicializar repositorio
git init
git add .
git commit -m "Primera versión de DondeVoy - App móvil optimizada"

# Crear repositorio en GitHub (hazlo en github.com primero)
# Luego conecta tu repo local:
git remote add origin https://github.com/TU-USUARIO/DondeVoy2.git
git branch -M main
git push -u origin main
```

### Activar GitHub Pages:
(Mismos pasos que la Opción 1, paso 3)

---

## Opción 3: Usar GitHub Desktop (Visual y fácil)

1. Descarga GitHub Desktop: https://desktop.github.com/
2. Instala e inicia sesión con tu cuenta de GitHub
3. File → Add Local Repository
4. Selecciona: `C:\Users\Usario\Desktop\DondeVoy2`
5. Click en "Publish repository"
6. Marca como "Public"
7. Click en "Publish"

Luego activa GitHub Pages desde la web (Opción 1, paso 3)

---

## 🎯 Después de Publicar

### Probar en tu móvil:
1. Abre: `https://TU-USUARIO.github.io/DondeVoy2/`
2. Configura tu API key de OpenWeather
3. Dale permiso de ubicación
4. ¡Prueba la app!

### Instalar como PWA:
**Android (Chrome):**
- Menú (⋮) → "Instalar app"

**iOS (Safari):**
- Botón compartir → "Añadir a pantalla de inicio"

---

## 📝 Archivos que DEBES subir:

✅ **index.html** - La aplicación principal
✅ **manifest.json** - Para instalación PWA
✅ **README.md** - Documentación
✅ **MOBILE.md** - Guía para móviles
✅ **.gitignore** - Control de archivos
✅ **start-server.ps1** - Para desarrollo local
✅ **server.py** - Servidor alternativo

❌ **NO subir:**
- `requirements.txt` - No se necesita para frontend
- Archivos `__pycache__/`
- Archivos `.pyc`

---

## 🔧 Actualizar después:

Si haces cambios:

**Opción Web:**
1. Ve a tu repositorio en GitHub
2. Click en el archivo a editar
3. Click en el lápiz (Edit)
4. Haz los cambios
5. Commit changes

**Con Git:**
```powershell
git add .
git commit -m "Descripción de los cambios"
git push
```

---

## ❓ Problemas Comunes

**"No veo mi página en GitHub Pages"**
- Espera 2-3 minutos después de activar Pages
- Verifica que el repositorio sea Public
- Revisa que index.html esté en la raíz

**"La app no funciona"**
- Abre la consola del navegador (F12)
- Verifica que tengas API key configurada
- Prueba en modo incógnito

**"No puedo instalar la PWA"**
- Solo funciona con HTTPS (GitHub Pages lo tiene)
- No funciona con file:// local
- Necesitas Chrome (Android) o Safari (iOS)

---

## 🌟 Mi recomendación

**Para empezar rápido:** Usa la **Opción 1** (subir archivos directamente)
**Para proyectos serios:** Instala Git o GitHub Desktop

---

## 📞 URL de tu app será:

```
https://TU-USUARIO.github.io/DondeVoy2/
```

Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub.

---

**¡Disfruta tu app en el móvil! 📱☀️**
