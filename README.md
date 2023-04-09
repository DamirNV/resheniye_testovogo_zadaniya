### Задание

Используем приложение https://github.com/anfederico/Flaskex<br>
Попробуйте запустить приложение локально, при наличии ошибок в запуске – исправьте их и приложите описание своего решения.<br>
Упакуйте данное приложение в docker. Проверьте, что контейнер запускается локально. Попробуйте запустить данное упакованное приложение через
docker-compose. Рабочий Dockerfile, docker-compose.yaml и текстовый документ с заметками выложить в свой репозиторий github.<br>
Полезная ссылка: https://docs.docker.com/<br>

### Решение

#### Запуск приложения в виртуальном окружении:
 
1. Установить виртуальное окружение питона (выполнять в директории программы):

`python3 -m venv .venv`

`source .venv/bin/activate`

2. Установить зависимости: 

`pip install -r requirements.txt`

3. Запустить приложение: 

`python3 app.py`

#### Описание решения ошибки:<br>

При запуске программы терминал выдал ошибку в файле forms.py 'wtforms.validators' не имеет атрибута 'required'<br>

1. Исправил:

`validators=[validators.required()` на `validators=[InputRequired()` в строках username и password<br>

2. Добавил:

`from wtforms.validators import InputRequired`<br>

#### Команда для сборки docker образа:

`docker build -t app:test .`

#### Команда для запуска контейнера:

`docker run --rm --name -p 5000:5000 flaskex app:test`

#### Команда для сборки образа c помощью docker-compose:

`docker-compose build`

#### Команда для запуска контейнера c помощью docker-compose: 

`docker compose up`
