#!/usr/bin/env python3
"""
Servidor HTTP simple para la aplicación DondeVoy
Ejecutar: python server.py
Luego abrir: http://localhost:8000
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Añadir headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Logging más limpio
        sys.stdout.write("%s - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))

def main():
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"")
        print(f"🌍 Servidor DondeVoy iniciado")
        print(f"")
        print(f"📍 Abre tu navegador en: http://localhost:{PORT}")
        print(f"")
        print(f"Para detener el servidor, presiona Ctrl+C")
        print(f"")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\n✓ Servidor detenido")
            sys.exit(0)

if __name__ == "__main__":
    main()
