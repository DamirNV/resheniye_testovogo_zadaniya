### Задание
Используем приложение https://github.com/anfederico/Flaskex<br>
Попробуйте запустить приложение локально, при наличии ошибок в запуске – исправьте их и приложите описание своего решения.<br>
Упакуйте данное приложение в docker. Проверьте, что контейнер запускается локально. Попробуйте запустить данное упакованное приложение через
docker-compose. Рабочий Dockerfile, docker-compose.yaml и текстовый документ с заметками выложить в свой репозиторий github.<br>
Полезная ссылка: https://docs.docker.com/<br>

### Решение

**Запуск приложения в виртуальном окружении:**
 
1. Установить виртуальное окружение питона (выполнять в директории программы):
`python3 -m venv .venv`<br>
`source .venv/bin/activate`<br>

2. Установить зависимости:
`pip install -r requirements.txt`<br>

3. Запустить приложение:
`python3 app.py`<br>

**Описание решения ошибки:**
При запуске программы терминал выдал ошибку в файле forms.py 'wtforms.validators' не имеет атрибута 'required'<br>
Исправил `validators=[validators.required()` на `validators=[InputRequired()` в строках username и password<br>
Дабавил `from wtforms.validators import InputRequired`<br>

**Команда для сборки docker образа:**
`docker build -t app:test .`<br>

**Команда для запуска контейнера:**
`docker run --rm --name -p 5000:5000 flaskex app:test`<br>

**Команда для сборки образа c помощью docker-compose:**
`docker-compose build`<br>

**Команда для запуска контейнера c помощью docker-compose:**
`docker compose up`<br>

<p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-logo.png" width="128px"><p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/anfederico/flaskex/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ef2f8f65c67a4043a9362fa6fb4f487a)](https://www.codacy.com/app/RDCH106/Flaskex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RDCH106/Flaskex&amp;utm_campaign=Badge_Grade)
[![Run on Repl.it](https://repl.it/badge/github/anfederico/Flaskex)](https://repl.it/github/anfederico/Flaskex)

<br><br>

<p align="center"><img src="https://raw.githubusercontent.com/anfederico/Flaskex/master/media/flaskex-demo.png" width="100%"><p>

## Features
- Encrypted user authorizaton
- Database initialization
- New user signup
- User login/logout
- User settings
- Modern user interface
- Bulma framework
- Limited custom css/js
- Easily customizable

## Setup
``` 
git clone https://github.com/anfederico/Flaskex
cd Flaskex
pip install -r requirements.txt
python app.py
```

## Contributing
Please take a look at our [contributing](https://github.com/anfederico/Flaskex/blob/master/CONTRIBUTING.md) guidelines if you're interested in helping!
