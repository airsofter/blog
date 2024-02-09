## Описание проекта

Сервис предназначен для создания индивидуального плана обучения пользователя на основе навыков, которые ему нужно развить и курсов Яндекс Практикума, которые обеспечат это развитие.


## Локальный запуск приложения в Docker  

Склонировать репозиторий на свой компьютер и перейти в корневую папку:
```python
git clone git@github.com:airsofter/blogs.git
cd blogs
```

Создать в корневой папке файл .env с переменными окружения, необходимыми
для работы приложения.

Пример содержимого файла:
```
SECRET_KEY=secret_key
DEBUG=True/False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DEFAULT_FROM_EMAIL=example@example.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db_name
POSTGRES_USER=db_postgres
POSTGRES_PASSWORD=db_postgres
DB_HOST=db
DB_PORT=db_port
USE_SQLITE=False
```

Из корневой директории запустить сборку контейнеров с помощью
docker-compose:
```
docker compose up -d
```

После этого проект должен стать доступен по адресу  http://localhost:8000/.

### Создание суперпользователя

Чтобы создать пользователя с правами администратора выполните следующую команду при запущенном проекте:
```
docker-compose exec web python3 manage.py createsuperuser
```


### Остановка контейнеров

Для остановки работы приложения можно набрать в терминале команду Ctrl+C
либо открыть второй терминал и воспользоваться командой:
```
docker-compose stop
```

Снова запустить контейнеры без их пересборки можно командой
```
docker-compose start
```