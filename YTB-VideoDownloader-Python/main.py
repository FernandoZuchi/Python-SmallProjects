from pytube import YouTube
import os

# Introduza a URL do vídeo que deseja baixar
url = 'https://www.youtube.com/watch?v=JcHRC_G-sOI&list=RDJcHRC_G-sOI&start_radio=1'

# Criando um objeto youtube
video = YouTube(url)

# Imprimindo detalhes do vídeo no console
print(f'Título: ", {video.title}')
print(f'Duração: {video.length} segundos')
print(f'Dimensão do vídeo : {video.streams.get_highest_resolution().filesize / (1024 ** 2):.2f} MB')


# Direcionando o objeto para o desktop
desktop_path = os.path.expanduser("~/Desktop")

# Baixando o vídeo em alta resolução no desktop
video.streams.get_highest_resolution().download(output_path=desktop_path)

print("Download concluído. O vídeo foi salvo no desktop.")