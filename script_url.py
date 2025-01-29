import subprocess
import platform
import time

#Archivo que va a cargar las URLs
filename = 'urls.txt'

def load_urls(filename):
    #Carga las URLs desde archivo de texto
    try:
        with open(filename,"r") as file:
            return[line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"El archivo no existe")
        return[]

def check_ping(url):
    #Verificar si la URL responde al ping.
    param = "-n" if platform.system().lower() == "windows " else "-c"
    try:
        response = subprocess.run(
            ["ping", param,"1",url],
            stdout=subprocess.DEVNULL,  #Oculta la salida en terminal.
            stderr=subprocess.DEVNULL
        )
        return response.returncode == 0 #Indica si ha sido exitoso.
    except Exception:
        return False

def send_notification(title,message):
    #Envia notificacion si alguna URL ha caído, según sistema operativo
    system = platform.system().lower()
    if system == "windows":
        subprocess.run(["powershell", "-Command", f"[System.Windows.MessageBox]::Show('{message}', '{title}')"])
    elif system == "darwin":  # macOS
        subprocess.run(["osascript", "-e", f'display notification "{message}" with title "{title}"'])
    elif system == "linux":
        subprocess.run(["notify-send", title, message])
    else:
        print(f"⚠️ Notificaciones no soportadas en {system}")
#Prueba enviado
#send_notification("🔔 Prueba de Notificación", "Si ves esto, las notificaciones funcionan correctamente.")

def main():
    urls = load_urls(filename)
    if not urls:
        return  #Esto saldrá si no hay URLs

    down_urls = [url for url in urls if not check_ping(url)]

    #Mostrar resultados
    if down_urls:
        print(f"Las siguientes URLs han caido:")
        for url in down_urls:
            print(f" - {url}")
            send_notification('URL caida: \n',url)
            time.sleep(5)
    else:
        print(f"Todas las URLs estan activas.")

if __name__ == "__main__":
    main()
