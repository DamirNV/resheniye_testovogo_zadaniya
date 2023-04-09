## Задание
Используем приложение https://github.com/anfederico/Flaskex<br>
Попробуйте запустить приложение локально, при наличии ошибок в запуске – исправьте их и приложите описание своего решения.<br>
Упакуйте данное приложение в docker. Проверьте, что контейнер запускается локально. Попробуйте запустить данное упакованное приложение через
docker-compose. Рабочий Dockerfile, docker-compose.yaml и текстовый документ с заметками выложить в свой репозиторий github.<br>
Полезная ссылка: https://docs.docker.com/<br>

## Решение

### Установка

Клонировал репозиторий командой git clone https://github.com/anfederico/Flaskex<br>
Перешел в репозиторий с программой командой cd Flaskex<br>
Установил зависимости с использованием requirements.txt командой pip install -r requirements.txt<br>
Запустил программу командой python app.py<br>
Вышла ошибка<br>

### Создание копии приложения и добавление в репозиторий на сайт github.com

Создал дирректорию командой mkdir resheniye<br>
Скопировал приложение в дирректорию resheniye командой cp -R flaskex/* resheniye/.<br>
Перешел в дирректорию командой cd resheniye<br>
Удалил лишние файлы git командой rm -rf flaskex/.git*<br>

Создал новый репозиторий на сайте https://github.com/DamirNV/resheniye_testovogo_zadaniya<br>

Добавил в репозиторий исходную программу командами:<br>
git init<br>
git add .<br>
git commit -m " Исходная программа"<br>
git branch -M main<br>
git remote add origin git@github.com:DamirNV/resheniye_testovogo_zadaniya.git<br>
git push -u origin main<br>

### Исправление ошибки в коде

При запуске программы терминал выдал ошибку<br>
Traceback (most recent call last):<br>
File "/home/user/Flaskex/app.py", line 4, in <module> from scripts import forms<br>
File "/home/user/Flaskex/scripts/forms.py", line 6, in <module> class LoginForm(Form):<br>
File "/home/user/Flaskex/scripts/forms.py", line 7, in LoginForm username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])<br>
AttributeError: module 'wtforms.validators' has no attribute 'required'<br>
Видим, что ошибка в файле forms.py, которая находится в дирректории /home/user/Flaskex/scripts/forms.py<br>

Суть ошибки 'wtforms.validators' не имеет атрибута 'required'<br>

Зашел в дирректорию файла forms.py <br>
Так как я копировал приложение в новую рабочую папку, то путь к файлу такой /home/user/resheniye/scripts/forms.py<br>
Команда cd resheniye<br>
Команда cd scripts<br>
Открыл файл forms.py командой nano forms.py<br>
Исправил validators=[validators.required() на validators=[InputRequired() в строках username и password<br>
Дабавил from wtforms.validators import InputRequired<br>
Сохранил изменения командой Ctrl+O<br>
Вышел из файла командой Ctrl+X<br>
Вышел из дирректории командой cd<br>

Зашел в дирректорию с программой командой cd resheniye<br>
Запустил приложение командой python3 app.py<br>
Приложение запустилось<br>
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:5000<br>

### Добавил исправленный файл в репозиторий git

Создал новую ветку в репозитории командой git branch develop<br>
Переключился на новую ветку git switch develop<br>
Добавил исправленный файл в репозиторий командами:<br>
git add .<br>
git commit -m "Исправил код"<br>
git push --set-upstream origin develop<br>

### Создание docker образа и запуск контейнера

Создал Dockerfile командой nano Dockerfile<br>

Со следующим содержимым:<br>
FROM python:3.6.15-alpine3.15<br>
WORKDIR /app<br>
COPY ./requirements.txt .<br>
RUN pip install -r requirements.txt<br>
COPY . .<br>
EXPOSE 5000<br>
CMD ["python3","app.py"]<br>
Сохранил изменения командой Ctrl+O<br>
Вышел из файла командой Ctrl+X<br>

Создал .dockerignore командой nano .dockerignore<br>

Со следующим содержимым:<br>
.git*<br>
**/.pytest_cashe/*<br>
Dockerfile<br>
docker-compose.yaml<br>
README.md<br>
Сохранил изменения командой Ctrl+O<br>
Вышел из файла командой Ctrl+X<br>

Создал docker образ командой sudo docker build -t app:obraz .<br>
Запустил контейнер с образом командой sudo docker run --rm --name -p 5000:5000 flaskex app:obraz<br>
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:5000<br>
Остановил командой Ctrl+C<br>

### Добавление Dockerfile и .dockerignore в репозиторий git

Выполнил следующие команды:<br>
git add .<br>
git commit -m "Добавил Dockerfile и .dockerignore"<br>
git push<br>

### Создание docker-compose.yml

Создал docker-compose.yml командой nano docker-compose.yml<br>

Со следующим содержимым:<br>
version: "3"<br>
services:<br>
web:<br>
build: <br>
context: .<br>
ports:<br>
- "8000:5000"<br>
networks:<br>
- flask<br>
networks:<br>
flask:<br>
Сохранил изменения командой Ctrl+O<br>
Вышел из файла командой Ctrl+X<br>

Запустил docker-compose командой sudo docker compose up<br>
Проверил, открылось ли приложение в браузере введя в адресную строку localhost:8000<br>
Остановил командой Ctrl+C<br>

### Добавление docker-compose.yml в репозиторий git

Выполнил следующие команды:<br>
git add .<br>
git commit -m "Добавил docker-compose.yaml"<br>
git push<br>

### Добавил инфомарцию о проделанной в файл README.md и дабавление файла в репозиторий git

nano README.md<br>
Описал проделанную работу над тестовым заданием с комментариями<br>
Сохранил изменения Ctrl+O<br>
Вышел из файла Ctrl+X<br>
Выполнил следующие команды:<br>
git add .<br>
git commit -m "Добавил инфомарцию о проделанной в файл README.md"<br>
git push<br>

### Создал pull request и сделал merge веток
Зашел в репозиторий на сайте github<br>
https://github.com/DamirNV/resheniye_testovogo_zadaniya/compare/main...develop<br>
Создал pull request нажав Create pull request<br>
Выбрал ветку develop к сравнению и слиянию с веткой main<br>
Добавил комментарии о проделанной работе<br> 

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
