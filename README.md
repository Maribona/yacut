# Проект: сервис YaCut
## Описание проекта:
Проект YaCut — это сервис укорачивания ссылок.     
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.           
## Технологии
![Python 3.9.10](https://img.shields.io/badge/python-3.9.10-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)        
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)    
## Как запустить проект в Dev-режиме:
### Клонировать репозиторий:
```bash
git@github.com:Maribona/yacut.git
```
### Создать виртуальное окружение:
```bash
python -m venv venv
```
### Активировать виртуальное окружение:
```bash
source venv/bin/activate
```  
### Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
### Создайте файл .env с настройками проекта
```bash
# пример
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY 
```
### Выполните миграции
```bash
flask db init
flask db migrate -m "init"
flask db upgrade
```
### Запуск проекта:
```bash
flask run
```
### Автор: 
Алехандро Марибона
