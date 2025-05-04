import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Caminho da pasta onde os vídeos serão salvos
PASTA_DESTINO = "videos_baixados"

# Cria a pasta se ela não existir
if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)

# Lê os links do arquivo "links_dos_videos.txt"
try:
    with open("links_dos_videos.txt", "r", encoding="utf-8") as arquivo:
        links = [linha.strip() for linha in arquivo if linha.strip()]
except FileNotFoundError:
    print("Arquivo 'links_dos_videos.txt' não encontrado.")
    exit()

# Baixa cada vídeo
for url in links:
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Baixando: {yt.title}")

        ys = yt.streams.get_lowest_resolution()
        ys.download(output_path=PASTA_DESTINO)

        print(f"Download concluído: {yt.title}\n")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
