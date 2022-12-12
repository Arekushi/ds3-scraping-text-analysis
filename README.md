<h1 align="center">
  DS3 Weapons - Scraping and Text analysis
</h1>

<p align="center">
  <a href="#" target="blank">
    <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/685fbcbf-2f26-4a6a-bee8-e17ffba0a830/d8amrvs-ef4af258-2c85-4c3b-b3bf-a34156ffae46.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi82ODVmYmNiZi0yZjI2LTRhNmEtYmVlOC1lMTdmZmJhMGE4MzAvZDhhbXJ2cy1lZjRhZjI1OC0yYzg1LTRjM2ItYjNiZi1hMzQxNTZmZmFlNDYucG5nIn1dXX0.UZh6sJhFCawOXpynexeDH849ZVVLEI0op67kEBIDTCU" width="250" alt="Nest Logo" />
  </a>
</p>

<p align="center">
  Project that captures information about all Dark Souls 3 (DS3) weapons and performs textual analysis on.
</p>

## About The Project
Project of the discipline `Projeto Integrador IV` of the 4º semester of the course of [`Technology in Big Data for Business`][big_data_course] at [`FATEC Ipiranga`][fatec_ipiranga]. Supervised by [`Marco Mazzei`](mailto:marco.mazzei@fatec.sp.gov.br).

### Portuguese description
O projeto tem como objetivo capturar informações da wiki de Dark Souls 3 referente as [armas][ds3_weapons_url] encontradas no jogo e realizar uma análise sobre o texto encontrado.

Dentro do projeto foi aplicado a técnica de `Topic Modelling`

### O que é Topic Modelling?
> A modelagem de tópicos é o processo de extrair os principais temas de um determinado corpus de dados de texto.

> Wikipedia: No aprendizado de máquina e no processamento de linguagem natural, um modelo de tópico é um tipo de modelo estatístico para descobrir os "tópicos" abstratos que ocorrem em uma coleção de documentos.



## Built With
- [Python 3.8.15][python:3.8]
- [Apache Spark 3.1.2][spark:3.1.2]
- [Spark NLP 4.2.4][spark-nlp]

## Getting Started
For the use of the project, some prerequisites will be necessary.

### Prerequisites (Windows)
* Python
  1. You can download here: [Python][python_url]
  2. Here is a step-by-step installation tutorial. [(Tutorial)][python_tutorial_url]
     1. Tutorial with Miniconda. [(Tutorial)][miniconda_tutorial]
* Poetry
  1. You can install here: [Poetry][poetry_url]
* Apache Spark
  1. Follow the step by step: [Spark][apache_spark_tutorial]

<br>

### Installation and usage
1. Clone this repo.
    ```sh
    git clone https://github.com/Arekushi/ds3-scraping-text-analysis.git
    ```

2. Install packages with `Poetry`
    ```sh
    poetry install
    ```

3. Download the `FAT JAR` from `Spark NLP` and put it wherever you want
    1. You can find here: https://github.com/JohnSnowLabs/spark-nlp/releases

4. Go to `./src/config/settings.toml` and edit `spark_nlp_jar_path` value to your path.
    ```toml
    spark_nlp_jar_path = 'C:\\spark\\jars\\spark-nlp-assembly-4.2.4.jar'
    ```

5. Execute:
    ```sh
    python ./main.py
    ```

6. Done, the whole process has been completed 🎉
    1. You can see the results inside the `./src/data` folder

## Roadmap
> Will be added soon...

## Video
> Will be added soon...

## Acknowledgments
Here in this [link][acknowledgments_url] you can see all the material I used to build the project. 😉

## Contributors
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] |
| :---: |

<!-- [Build With] -->
[python:3.8]: https://www.python.org/downloads/
[spark:3.1.2]: https://spark.apache.org/downloads.html
[spark-nlp]: https://nlp.johnsnowlabs.com/docs/en/quickstart

<!-- [Some links] -->
[fatec_ipiranga]: https://fatecipiranga.edu.br/
[big_data_course]: https://fatecipiranga.edu.br/curso-superior-de-tecnologia-em-big-data-para-negocios/

[apache_spark_tutorial]: https://nlp.johnsnowlabs.com/docs/en/install#how-to-correctly-install-spark-nlp-on-windows

[python_url]: https://www.python.org/downloads/
[python_tutorial_url]: https://www.digitalocean.com/community/tutorials/install-python-windows-10
[miniconda_tutorial]: https://katiekodes.com/setup-python-windows-miniconda/
[poetry_url]: https://python-poetry.org/docs/#installation

[ds3_weapons_url]: https://darksouls.fandom.com/wiki/Weapons_(Dark_Souls_III)


<!-- Acknowledgments -->
[acknowledgments_url]: https://arekushi.notion.site/Acknowledgments-ea81ca63d5ee4d4ca9dc2ee0795c2262

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
