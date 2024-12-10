import requests
import xml.etree.ElementTree as ET
import logging

# Configurar logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_epg(url, output_file):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Verifica se houve algum erro na solicitação
        with open(output_file, 'wb') as file:
            file.write(response.content)
        logging.info(f"EPG atualizado e salvo em {output_file}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao baixar o EPG: {e}")

def update_epg():
    epg_url = "http://m3u4u.com/epg/xe47yz1pd9spv21mn9vq"  # Substitua pela URL do EPG
    output_file = "epg.xml"
    download_epg(epg_url, output_file)

if __name__ == "__main__":
    update_epg()
