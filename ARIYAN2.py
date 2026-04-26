import requests
import urllib3
from google_play_scraper import app

# Esto desactiva las advertencias de seguridad en la consola
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def AuToUpDaTE():
    # Obtiene la versión actual del juego desde la Play Store
    result = app('com.dts.freefireth', lang="fr", country='fr')
    version = result['version']
    
    url_api = f'https://bdversion.ggbluefox.com/live/ver.php?version={version}&lang=ar&device=android&channel=android&appstore=googleplay&region=ME&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993'
    
    # Engañamos al servidor haciéndole creer que somos un celular Android
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PQ3B.190801.10101846)"
    }
    
    try:
        r = requests.get(url_api, headers=headers, verify=False, timeout=10)
        
        # Intentamos leer la respuesta como JSON
        datos = r.json()
        url = datos.get('server_url')
        ob = datos.get('latest_release_version')
        
        return url, ob, version

    except Exception as e:
        # Si la API bloquea a Railway o se cae, entramos aquí
        print(f"⚠️ Alerta: El servidor de actualización bloqueó la petición o falló. Usando valores de respaldo...")
        
        # VALORES POR DEFECTO PARA QUE EL BOT NO SE APAGUE
        # Si el juego se actualiza, solo cambia este '1.111.1' por el nuevo OB
        url_respaldo = "https://100067.connect.garena.com/api" 
        ob_respaldo = "1.111.1"
        
        return url_respaldo, ob_respaldo, version
