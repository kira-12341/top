import http.server
import socketserver
import os
import sys

# رقم البورت
PORT = 8000

# مجلد الملفات
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class SilentHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # السماح بالوصول (CORS) ومنع الكاش
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # كتم تسجيل كل الطلبات
        return

# تعطيل stdout حتى لا يطبع أي شيء
class NullWriter:
    def write(self, _): pass
    def flush(self): pass
sys.stdout = NullWriter()
sys.stderr = NullWriter()

# تشغيل السيرفر بصمت
with socketserver.TCPServer(("", PORT), SilentHTTPRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
