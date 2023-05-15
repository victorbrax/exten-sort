<div align="center">
  <table>
  <tr>
    <td><img height="24rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/0752b2c1c65a0862a346f7d0e93ca1a3fbd0447b/docs/us.svg" alt="euaflag"></td>
    <td>Do you speak English? Please, <a href="https://github.com/victorbrax/exten-sort">click here</a>.</td>
  </tr>
</table>
</div>

<div align="center">
  
[![Project](https://img.shields.io/badge/PROJETO_PESSOAL-important.svg)]()
[![Python](https://img.shields.io/badge/Python-informational.svg)]()
[![auto-py-to-exe](https://img.shields.io/badge/Auto_Py_to_Exe-green.svg)]()
[![OS](https://img.shields.io/badge/OS-gray.svg)]()
</div>


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/victorbrax/exten-sort/main/docs/logos/extensort-logo.png">
</div>
</div>
<p align="center">Por <strong>Víctor Gomes</strong></p>

# É um prazer ter você aqui! ⚜

Sempre fui obcecado por **organização**, mantendo as coisas em seus devidos lugares seguindo as melhores práticas. Isso sempre foi crucial para mim. Além disso, não há preço para o prazer de encontrar rapidamente o arquivo desejado olhando no lugar certo. É por isso que desenvolvi um aplicativo que organiza automaticamente a minha pasta de `Downloads` **quando o computador é ligado**.
</br>
</br>

## Visualização 🖼️

<div align="center">
<img height="400vh" src="https://raw.githubusercontent.com/victorbrax/exten-sort/main/docs/images/example-photo.png">
</div>

## Rode o projeto localmente (sem Python instalado) 🏠

Este projeto possui um arquivo executável, então se você é um usuário inexperiente em programação ou um desenvolvedor preguiçoso, você pode simplesmente baixá-lo e seguir as etapas abaixo.

* Baixe o arquivo _**.exe**_ `exten-sort` na pasta [dist](dist).
* Pressione `Win + R` e digite `shell:startup`
* Mova o arquivo executável para a pasta e seja feliz.

## Rode o projeto localmente (com Python instalado) 🏠

Garanta que você tenha o [Python](https://python.org/downloads) instalado para rodar o projeto da seguinte forma:

* Clone ou faça um fork deste repositório.
* Crie um ambiente virtual. Você pode fazer isso usando `python -m venv venv` no terminal.
* Instale as bibliotecas necessárias. Se você usa o pip para gerenciar seus pacotes, use `pip install -r requirements.txt` (caso queira criar o instalador posteriormente).
* Execute `auto-py-to-exe` no terminal, escolha "One File", use o ícone na [pasta icons](docs/icons) e gere seu arquivo executável.
* Execute `python main.py`
* Verifique sua pasta de `Downloads`.

## Tecnologias que foram usadas 🖥️
* [Shutil](https://docs.python.org/3/library/shutil.html)
* [OS](https://docs.python.org/3/library/os.html)
* [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe)

## Considerações 📝
Este projeto verifica a extensão de cada arquivo em sua pasta de Downloads. Em seguida, ele cria uma pasta (se ainda não existir) e move o arquivo para ela, tornando tudo mais organizado.

Este aplicativo me ajuda a manter minha pasta de downloads organizada diariamente, e espero que também te ajude. Você pode alterar o diretório de destino para outro, se necessário.

* Existem outros projetos semelhantes na internet, mas decidi criar o meu próprio porque queria um código mais conciso e eficiente, especialmente para lidar com extensões de arquivo menos conhecidas.

## Licença 📜

O código neste projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.</br>

> Obrigado pelo prestígio. 🐍
