# Projeto de vendas de cursos online

Este projeto, a IPP Academy, tem a intenção de vender cursos online

Projeto feito para a disciplina de Integração de Sistemas da pós-graduação em [Data Science and Digital Transformation](https://www.ipportalegre.pt/pt/oferta-formativa/pos-graduacao-data-science-and-digital-transformation) do [Instituto Politécnico de Portalegre](https://www.ipportalegre.pt/pt/)

## Configurações do projeto
Para rodar este projeto, segue os seguintes passos:

### Instalar ambiente virtual com Poetry e ativá-lo
```bash
$ poetry install
```
Se não possui o poetry instalado, basta instalá-lo com `pip`

```bash
$ pip install poetry
```

Após a criação do ambiente, temos que ativá-lo
```bash
$ poetry shell
```
### Rodar Servidor
Para rodar o servidor com o django, basta rodar o seguinte comando dentro da pasta `django_ecommerce` o seguinte comando
```bash
$ python manage.py runserver

```