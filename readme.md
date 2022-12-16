# Пульт охраны банка

Вэб приложение для отслеживания активности входа сотрудников в хранилище банка. Позволяет находить подозрительные посещения, которые длятся более 1 часа

### Как установить

Необходимо создать файл в корне проекта `.env` и в нем прописать занчения переменных для подключения к базе данных

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
SECRET_KEY=
DB_ENGINE=
ALLOWED_HOSTS=
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```commandline
pip install -r requirements.txt
```

### Как установить

Для запуска приложения необходимо выполнить команду

```commandline
python manage.py runserver 0.0.0.0:8000
```

и открыть в браузере страницу [0.0.0.0:8000](http://0.0.0.0:8000), в Windows [localhost:8000](http://127.0.0.1:8000)
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).