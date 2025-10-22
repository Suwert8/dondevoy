# 📱 Guía para Móviles - DondeVoy

## ¿Cómo usar en tu móvil?

Esta aplicación es **100% frontend** y funciona completamente en tu navegador sin necesidad de servidor backend. Puedes usarla de varias formas:

### Opción 1: GitHub Pages (Recomendado) 🌐

1. Sube el proyecto a un repositorio de GitHub
2. Activa GitHub Pages en la configuración del repositorio
3. Accede desde cualquier dispositivo a `https://tu-usuario.github.io/DondeVoy2/`
4. ¡Ya está! Funciona directamente

### Opción 2: Netlify/Vercel (Muy fácil) ⚡

1. Sube tu repositorio a GitHub
2. Conecta con [Netlify](https://netlify.com) o [Vercel](https://vercel.com)
3. Deploy automático en segundos
4. Obtienes una URL pública: `https://tu-app.netlify.app`

### Opción 3: Servidor Local (Para desarrollo) 💻

Si quieres probar localmente en tu móvil:

1. Ejecuta el servidor:
   ```bash
   powershell -ExecutionPolicy Bypass -File start-server.ps1
   ```

2. Encuentra tu IP local:
   ```bash
   ipconfig
   ```
   Busca "Dirección IPv4" (ejemplo: `192.168.1.100`)

3. En tu móvil, abre el navegador y ve a:
   ```
   http://192.168.1.100:8000
   ```

**Importante:** Tu móvil debe estar en la misma red WiFi que tu PC.

## 🎯 Instalar como App (PWA)

Una vez que tengas la app accesible en una URL (opciones 1 o 2):

### En Android:
1. Abre la app en Chrome
2. Toca el menú (⋮) → "Instalar app" o "Añadir a pantalla de inicio"
3. Confirma la instalación
4. ¡Listo! Ahora tienes un icono en tu pantalla de inicio

### En iOS (iPhone/iPad):
1. Abre la app en Safari
2. Toca el botón de compartir (⬆️)
3. Selecciona "Añadir a pantalla de inicio"
4. Confirma
5. ¡Ya tienes la app en tu iPhone!

## ✨ Características Mobile-Friendly

✅ **Diseño Responsive**: Se adapta a cualquier tamaño de pantalla
✅ **Gestos Táctiles**: Optimizado para touch
✅ **Sin CORS**: Funciona desde cualquier dominio
✅ **Offline Ready**: Una vez cargada, funciona sin conexión (excepto APIs)
✅ **PWA**: Instalable como app nativa
✅ **Ligera**: Carga rápida incluso con 3G

## 🔧 Configuración Inicial

1. Obtén tu API key de [OpenWeather](https://openweathermap.org/api) (gratis)
2. En la app, toca el ⚙️ (arriba a la derecha)
3. Ingresa tu API key
4. Ajusta tus preferencias
5. Toca "Guardar"

## 💡 Tips para Móviles

- **Usa el botón 📍**: Tu móvil detectará automáticamente tu ubicación
- **Instala la app**: Mucho más rápido que abrir el navegador
- **Activa la ubicación**: Para mejores resultados
- **Guarda tu API key**: Se mantiene aunque cierres la app
- **Modo avión**: La app recuerda tus últimas búsquedas

## 🌐 Hosting Gratis Recomendado

Para tener tu app siempre disponible en internet:

1. **GitHub Pages** (100% gratis)
   - Ilimitado tráfico
   - HTTPS automático
   - Actualización con git push

2. **Netlify** (Plan gratuito)
   - 100 GB/mes de ancho de banda
   - Deploy automático
   - HTTPS incluido

3. **Vercel** (Plan gratuito)
   - Hosting ilimitado
   - Edge network global
   - Analytics incluido

4. **Firebase Hosting** (Plan Spark gratuito)
   - 10 GB de almacenamiento
   - 360 MB/día de transferencia
   - SSL gratuito

## 🚀 Deploy Rápido a GitHub Pages

```bash
# 1. Inicializar git (si no lo has hecho)
git init
git add .
git commit -m "Primera versión"

# 2. Crear repositorio en GitHub y conectar
git remote add origin https://github.com/TU-USUARIO/DondeVoy2.git
git branch -M main
git push -u origin main

# 3. En GitHub: Settings → Pages → Source: main branch
# ¡Listo! Tu app estará en https://TU-USUARIO.github.io/DondeVoy2/
```

## 📝 Notas Importantes

- **No necesitas servidor**: Es solo HTML/CSS/JavaScript
- **APIs externas**: OpenWeather y Nominatim (geocodificación)
- **Privacidad**: Todo se ejecuta en tu navegador
- **Sin base de datos**: La configuración se guarda en localStorage
- **Sin backend**: No hay costos de servidor

## 🔒 Seguridad

- Tu API key se guarda localmente en tu dispositivo
- Nunca se envía a ningún servidor nuestro
- Las peticiones van directamente a OpenWeather API
- Revoca tu API key si compartes tu dispositivo

## ❓ Problemas Comunes

**"No funciona en mi móvil"**
- Verifica que estés usando HTTPS o localhost
- Las APIs requieren conexión segura

**"No puedo instalar la app"**
- Debe estar en HTTPS (usa GitHub Pages/Netlify)
- Solo funciona en Chrome (Android) o Safari (iOS)

**"La geolocalización no funciona"**
- Activa los permisos de ubicación en tu navegador
- Debe ser HTTPS o localhost

**"Errores de CORS"**
- No abras el archivo directamente (file://)
- Usa un servidor HTTP (opciones 1, 2 o 3)

## 📞 Soporte

Si tienes problemas, verifica:
1. ¿Estás usando HTTPS o localhost?
2. ¿Tienes una API key válida?
3. ¿Activaste los permisos de ubicación?
4. ¿Tienes conexión a internet?

---

**¡Disfruta de DondeVoy en tu móvil! ☀️📍**
