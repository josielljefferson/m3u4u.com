import requests
import xml.etree.ElementTree as ET
import time

def download_epg(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"EPG atualizado e salvo em {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o EPG: {e}")

def update_epg():#http://m3u4u.com/m3u/xe47yz1pd9spv21mn9vq
    epg_url = "http://m3u4u.com/epg/xe47yz1pd9spv21mn9vq"  # Substitua pela URL do EPG
    output_file = "epg.xml"
    download_epg(epg_url, output_file)

def schedule_epg_update(interval):
    while True:
        update_epg()
        time.sleep(interval)

if __name__ == "__main__":
    # Define o intervalo para 24 horas (86400 segundos)
    schedule_epg_update(86400)
