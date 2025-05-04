# 🎵 Utilitários de Vídeo e Áudio com Python

Este repositório contém dois utilitários simples em Python para facilitar o download de vídeos e a conversão para o formato MP3.

## 📁 Estrutura do Projeto

```
.
├── BaixarVideos
│   ├── videos_baixados/
│   ├── links_dos_videos.txt
│   └── main.py
├── ConverterParaMP3Classico
│   └── main.py
└── .gitignore
└── LICENSE
└── README.md
```

---

## 📥 Baixar Vídeos

Pasta: `BaixarVideos`

### O que faz:

- Lê links de vídeos de um arquivo `links_dos_videos.txt`
- Baixa os vídeos para a pasta `videos_baixados`

### Como usar:

1. Insira os links dos vídeos no arquivo `links_dos_videos.txt`, um por linha.
2. Execute o script:

```bash
python main.py
```

---

## 🎧 Converter para MP3

Pasta: `ConverterParaMP3Classico`

### O que faz:

- Converte arquivos de vídeo (MP4, MKV, AVI, etc.) para o formato MP3.
- Os arquivos convertidos são salvos em uma nova pasta com o sufixo `_mp3`.

### Como usar:

1. Execute o script e informe o caminho da pasta com os vídeos:

```bash
python main.py
```

---

## 🧰 Requisitos

- Python 3.8+
- [moviepy](https://pypi.org/project/moviepy/)
- [pytube](https://pypi.org/project/pytube/) (caso use para download de vídeos)

Instale as dependências com:

```bash
pip install -r requirements.txt
```

> **Dica:** Se quiser transformar os scripts em executáveis (.exe), você pode usar o [PyInstaller](https://www.pyinstaller.org/).

---

## 📄 Licença

Este projeto é de uso pessoal/educacional. Sinta-se livre para modificar conforme sua necessidade.
