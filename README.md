# 📦 LIVZIP - Python File Compressor & Extractor


O **LIVZIP** é uma ferramenta utilitária robusta desenvolvida em **Python**, projetada para simplificar a compressão e extração de ficheiros e pastas. Este projeto oferece flexibilidade total ao disponibilizar duas formas de interação: uma via linha de comandos (CLI) e outra com interface gráfica (GUI).


## ✨ Funcionalidades Principais


* **Compressão Eficiente**: Algoritmo otimizado para agrupar múltiplos ficheiros e pastas em ficheiros `.zip`.

* **Extração Rápida**: Descompressão de ficheiros de forma segura e organizada.

* **Interface Dual**:

    * **LIVZIP CLI**: Focada em performance e automação via terminal.

    * **LIVZIP GUI**: Interface amigável construída com **Tkinter**, ideal para quem prefere interação visual.

* **Tratamento de Erros**: Sistema preparado para lidar com permissões de ficheiros e caminhos inválidos.


## 🛠️ Tecnologias Utilizadas


* **Linguagem**: Python 3.x

* **Bibliotecas Core**: `zipfile`, `os`, `pathlib`.

* **Interface Gráfica**: `tkinter`.


## ⚙️ Configuração do Ambiente (Boas Práticas)


Para manter o seu sistema limpo, este projeto foi estruturado para rodar num ambiente virtual (venv).


1.  **Criar o ambiente virtual**:

    ```bash

    python -m venv .venv

    ```

2.  **Ativar o ambiente**:

    * **Windows**: `.venv\Scripts\activate`

    * **Linux/Mac**: `source .venv/bin/activate`

      

### Instalar dependências:


pip install -r requirements.txt


## 🚀 Como Executar


### Para a versão com Interface Gráfica (GUI):

```bash

python livzip_gui.py


Para a versão de Terminal (CLI):

python livzip_cli.py --help


Autor: Lacelmo Carlos (LYV1)

Desenvolvedor focado em Backend e Cibersegurança.




