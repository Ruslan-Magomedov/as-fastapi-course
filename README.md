1. Создать виртуальное окружение
```
python -m venv <file_name>
```

2. Активировать виртулальное окружения
```
linux:
source <file_name>\bin\activate
```
```
windows:
<file_name>\script\activate
```

3. Установка зависимостей
```
pip install -r requirements.txt
```


Создайте файл .env и запишите туда данные для подключения к бд.
```
DB_NAME=...
DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASS=...
```
