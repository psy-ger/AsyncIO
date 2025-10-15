# AsyncIO Tasks: README

## Опис (українською)

Ця папка містить приклади асинхронного програмування на Python з використанням asyncio, aiohttp, багатопотоковості та багатопроцесорності.

### Завдання

1. **task_1_basics_of_asynchrony.py**
   - Основи асинхронності: симуляція завантаження сторінок з випадковою затримкою.
   - Запуск: `python task_1_basics_of_asynchrony.py`

2. **task_2_working_with_asynchronous_http_requests.py**
   - Асинхронні HTTP-запити через aiohttp. Паралельне завантаження сторінок.
   - Запуск: `python task_2_working_with_asynchronous_http_requests.py`

3. **task_3_asynchronous_queues.py**
   - Асинхронна черга: producer додає завдання, кілька consumer обробляють їх.
   - Запуск: `python task_3_asynchronous_queues.py`

4. **task_4_asynchronous_timeout.py**
   - Асинхронний таймаут: демонстрація використання asyncio.wait_for.
   - Запуск: `python task_4_asynchronous_timeout.py`

5. **task_5_creating_simple_asynchronous_web_server.py**
   - Простий асинхронний веб-сервер на aiohttp з двома маршрутами (`/` і `/slow`).
   - Запуск: `python task_5_creating_simple_asynchronous_web_server.py` і перейдіть у браузері на http://127.0.0.1:8080/

6. **task_6_downloading_images_from_multiple_websites.py**
   - Асинхронне завантаження зображень з декількох сайтів.
   - Запуск: `python task_6_downloading_images_from_multiple_websites.py`

7. **task_7_comparing_multithreading_multiprocessing_asynchrony.py**
   - Порівняння часу виконання 500 HTTP-запитів у різних режимах: синхронно, багатопотоково, багатопроцесорно, асинхронно.
   - Запуск: `python task_7_comparing_multithreading_multiprocessing_asynchrony.py`

### Встановлення залежностей

Виконайте команду:
```
pip install -r requirements.txt
```

---

## Description (English)

This folder contains examples of asynchronous programming in Python using asyncio, aiohttp, multithreading, and multiprocessing.

### Tasks

1. **task_1_basics_of_asynchrony.py**
   - Basics of asynchrony: simulates page downloads with random delays.
   - Run: `python task_1_basics_of_asynchrony.py`

2. **task_2_working_with_asynchronous_http_requests.py**
   - Asynchronous HTTP requests with aiohttp. Parallel page downloads.
   - Run: `python task_2_working_with_asynchronous_http_requests.py`

3. **task_3_asynchronous_queues.py**
   - Asynchronous queue: producer adds tasks, multiple consumers process them.
   - Run: `python task_3_asynchronous_queues.py`

4. **task_4_asynchronous_timeout.py**
   - Asynchronous timeout: demonstrates asyncio.wait_for usage.
   - Run: `python task_4_asynchronous_timeout.py`

5. **task_5_creating_simple_asynchronous_web_server.py**
   - Simple asynchronous web server with aiohttp and two routes (`/` and `/slow`).
   - Run: `python task_5_creating_simple_asynchronous_web_server.py` and open http://127.0.0.1:8080/ in your browser.

6. **task_6_downloading_images_from_multiple_websites.py**
   - Asynchronous image downloading from multiple websites.
   - Run: `python task_6_downloading_images_from_multiple_websites.py`

7. **task_7_comparing_multithreading_multiprocessing_asynchrony.py**
   - Compares execution time of 500 HTTP requests in sync, multithreaded, multiprocess, and async modes.
   - Run: `python task_7_comparing_multithreading_multiprocessing_asynchrony.py`

### Installing dependencies

Run:
```
pip install -r requirements.txt
```

---

## Додаткові питання для роздумів / Additional questions for reflection

### 1. Як можна інтегрувати асинхронний код у вже існуючий синхронний проект на Python?
- Можна використовувати окремі асинхронні модулі або сервіси, які взаємодіють із синхронним кодом через черги, процеси або мережеві запити (наприклад, через HTTP API).
- Для запуску асинхронних функцій із синхронного коду можна використовувати `asyncio.run()` (у головному потоці) або створювати окремий event loop у фоновому потоці.
- Важливо уникати блокуючих викликів у асинхронному коді, інакше це зведе нанівець переваги асинхронності.

### 2. Які підводні камені використання асинхронних бібліотек при роботі з базами даних?
- Не всі драйвери баз даних підтримують асинхронність (наприклад, стандартний psycopg2 для PostgreSQL — синхронний, а asyncpg — асинхронний).
- Асинхронні бібліотеки можуть мати інші API та вимагати іншого підходу до керування транзакціями.
- Важливо стежити за пулом з'єднань: асинхронні запити можуть швидко вичерпати доступні з'єднання.
- Деякі ORM (наприклад, SQLAlchemy) мають окремі асинхронні версії, і їх не можна змішувати із синхронними моделями.
