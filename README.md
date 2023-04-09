## Задание
Используем приложение https://github.com/anfederico/Flaskex
Попробуйте запустить приложение локально, при наличии ошибок в запуске – исправьте их и приложите описание своего решения.
Упакуйте данное приложение в docker. Проверьте, что контейнер запускается локально. Попробуйте запустить данное упакованное приложение через
docker-compose. Рабочий Dockerfile, docker-compose.yaml и текстовый документ с заметками выложить в свой репозиторий github.
Полезная ссылка:
https://docs.docker.com/

## Решение

### Установка

Клонировал репозиторий командой git clone https://github.com/anfederico/Flaskex
Перешел в репозиторий с программой командой cd Flaskex
Установил зависимости с использованием requirements.txt командой pip install -r requirements.txt
Запустил программу командой python app.py
Вышла ошибка

### Создание копии приложения и добавление в репозиторий на сайт github.com
Создал дирректорию командой mkdir resheniye
Скопировал приложение в дирректорию resheniye командой cp -R flaskex/* resheniye/.
Перешел в дирректорию командой cd resheniye
Удалил лишние файлы git командой rm -rf flaskex/.git*

Создал новый репозиторий на сайте https://github.com/DamirNV/resheniye_testovogo_zadaniya

Добавил в репозиторий исходную программу командами
git init
git add .
git commit -m " Исходная программа"
git branch -M main
git remote add origin git@github.com:DamirNV/resheniye_testovogo_zadaniya.git
git push -u origin main

### Исправление ошибки в коде

При запуске программы терминал выдал ошибку
Traceback (most recent call last):
File "/home/user/Flaskex/app.py", line 4, in <module> from scripts import forms
File "/home/user/Flaskex/scripts/forms.py", line 6, in <module> class LoginForm(Form):
File "/home/user/Flaskex/scripts/forms.py", line 7, in LoginForm username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
AttributeError: module 'wtforms.validators' has no attribute 'required'
Видим, что ошибка в файле forms.py, которая находится в дирректории /home/user/Flaskex/scripts/forms.py
Суть ошибки 'wtforms.validators' не имеет атрибута 'required'
Зашел в дирректорию файла forms.py 
Так как я копировал приложение в новую рабочую папку, то путь к файлу такой /home/user/resheniye/scripts/forms.py
команда cd resheniye
команда cd scripts
Открыл файл forms.py командой nano forms.py
Исправил validators=[validators.required() на validators=[InputRequired() в строках username и password
Дабавил в import from wtforms.validators import InputRequired
Сохранил изменения командой Ctrl+O
Вышел из файла командой Ctrl+X
Вышел из дирректории командой cd
Зашел в дирректорию с программой командой cd resheniye
Запустил приложение командой python3 app.py
Приложение запустилось
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:5000

### Добавил исправленный файл в репозиторий git

Создал новую ветку в репозитории командой git branch develop
Переключился на новую ветку git switch develop
Добавил исправленный файл в репозиторий командами:
git add .
git commit -m "Исправил код"
git push --set-upstream origin develop

### Создание docker образа и запуск контейнера

Создал Dockerfile командой nano Dockerfile
Со следующим содержимым:
FROM python:3.6.15-alpine3.15
WORKDIR /app
COPY ./requirements.txt . 
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3","app.py"]
Сохранил изменения командой Ctrl+O
Вышел из файла командой Ctrl+X
Создал .dockerignore командой nano .dockerignore
Со следующим содержимым:
.git*
**/.pytest_cashe/*
Dockerfile
docker-compose.yaml
README.md
Сохранил изменения командой Ctrl+O
Вышел из файла командой Ctrl+X
Создал docker образ командой sudo docker build -t app:obraz .
Запустил контейнер с образом командой sudo docker run --rm --name -p 5000:5000 flaskex app:obraz
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:5000
Остановил командой Ctrl+C

### Добавление Dockerfile и .dockerignore в репозиторий git

Выполнил следующие команды:
git add .
git commit -m "Добавил Dockerfile и .dockerignore"
git push

### Создание docker-compose.yml

Создал docker-compose.yml командой nano docker-compose.yml
Со следующим содержимым:
version: "3"
services:
web:
build: 
context: .
ports:
- "8000:5000"
networks:
- flask
networks:
flask:
Запустил docker-compose командой sudo docker compose up
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:8000
Остановил командой Ctrl+C

### Добавление docker-compose.yml в репозиторий git

Выполнил следующие команды:
git add .
git commit -m "Добавил docker-compose.yaml"
git push

### Добавил инфомарцию о проделанной в файл README.md и дабавление файла в репозиторий git

nano README.md
Описал проделанную работу над тестовым заданием с комментариями 
Сохранил изменения Ctrl+O
Вышел из файла Ctrl+X
Выполнил следующие команды:
git add .
git commit -m "Добавил инфомарцию о проделанной в файл README.md"
git push

### Создал pull request и сделал merge веток
Зашел в репозиторий на сайте github
https://github.com/DamirNV/resheniye_testovogo_zadaniya/compare/main...develop
Создал pull request нажав Create pull request 
Выбрал ветку develop к сравнению и слиянию с веткой main 
Добавил комментарии о проделанной работе 

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
