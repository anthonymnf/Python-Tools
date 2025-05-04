import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def converter_para_mp3(pasta_origem):
    if not os.path.isdir(pasta_origem):
        print("Caminho inválido ou a pasta não existe.")
        return

    nome_pasta = os.path.basename(os.path.normpath(pasta_origem))
    pasta_destino = os.path.join(os.path.dirname(pasta_origem), nome_pasta + "_mp3")

    os.makedirs(pasta_destino, exist_ok=True)

    for arquivo in os.listdir(pasta_origem):
        caminho_video = os.path.join(pasta_origem, arquivo)
        nome_base, extensao = os.path.splitext(arquivo)

        if extensao.lower() not in ['.mp4', '.mkv', '.avi', '.mov', '.webm']:
            continue  # ignora arquivos que não são vídeos

        try:
            print(f"Convertendo: {arquivo}")
            video = VideoFileClip(caminho_video)
            caminho_mp3 = os.path.join(pasta_destino, f"{nome_base}.mp3")
            video.audio.write_audiofile(caminho_mp3)
            video.close()
            print(f"Salvo: {caminho_mp3}\n")
        except Exception as e:
            print(f"Erro ao converter {arquivo}: {e}")

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta que contém os vídeos: ").strip()
    converter_para_mp3(caminho)
