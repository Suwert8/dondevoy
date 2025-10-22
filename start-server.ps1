# Servidor HTTP simple para DondeVoy
# Ejecutar: .\start-server.ps1

$port = 8000
$url = "http://localhost:$port/"

Write-Host ""
Write-Host "Servidor DondeVoy iniciando..." -ForegroundColor Cyan
Write-Host ""

# Crear el listener
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add($url)

try {
    $listener.Start()
    Write-Host "Servidor iniciado correctamente" -ForegroundColor Green
    Write-Host ""
    Write-Host "Abre tu navegador en: $url" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Para detener el servidor, presiona Ctrl+C" -ForegroundColor Gray
    Write-Host ""

    # Abrir el navegador automáticamente
    Start-Process $url

    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        # Obtener el path solicitado
        $path = $request.Url.LocalPath
        if ($path -eq "/") {
            $path = "/index.html"
        }

        $filePath = Join-Path $PSScriptRoot $path.TrimStart('/')

        # Log de la petición
        Write-Host "$(Get-Date -Format 'HH:mm:ss') - $($request.HttpMethod) $path" -ForegroundColor Gray

        if (Test-Path $filePath -PathType Leaf) {
            # Leer el archivo
            $content = [System.IO.File]::ReadAllBytes($filePath)
            
            # Determinar Content-Type
            $extension = [System.IO.Path]::GetExtension($filePath)
            $contentType = switch ($extension) {
                ".html" { "text/html; charset=utf-8" }
                ".css"  { "text/css; charset=utf-8" }
                ".js"   { "application/javascript; charset=utf-8" }
                ".json" { "application/json; charset=utf-8" }
                ".png"  { "image/png" }
                ".jpg"  { "image/jpeg" }
                ".jpeg" { "image/jpeg" }
                ".gif"  { "image/gif" }
                ".svg"  { "image/svg+xml" }
                ".ico"  { "image/x-icon" }
                default { "application/octet-stream" }
            }

            # Headers CORS
            $response.Headers.Add("Access-Control-Allow-Origin", "*")
            $response.Headers.Add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            $response.Headers.Add("Access-Control-Allow-Headers", "*")
            $response.Headers.Add("Cache-Control", "no-cache")
            
            $response.ContentType = $contentType
            $response.ContentLength64 = $content.Length
            $response.StatusCode = 200
            $response.OutputStream.Write($content, 0, $content.Length)
        }
        else {
            # 404 - Archivo no encontrado
            $response.StatusCode = 404
            $message = [System.Text.Encoding]::UTF8.GetBytes("404 - Archivo no encontrado: $path")
            $response.ContentLength64 = $message.Length
            $response.OutputStream.Write($message, 0, $message.Length)
        }

        $response.Close()
    }
}
catch {
    Write-Host ""
    Write-Host "Error: $_" -ForegroundColor Red
}
finally {
    if ($listener.IsListening) {
        $listener.Stop()
    }
    Write-Host ""
    Write-Host "Servidor detenido" -ForegroundColor Green
}
