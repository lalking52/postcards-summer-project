# Postcard Microservice

**Простой сервис для создания и хранения открыток**  
*Flask + PostgreSQL в Docker*


1. Запуск проекта:
   ```bash
   git clone https://github.com/ваш-логин/first.git
   cd first
   docker-compose up -d
2. Откройте в браузере:
http://localhost:5001
## Технологии
Backend: Python Flask
Database: PostgreSQL
Infrastructure: Docker

## API Endpoints

| Метод  | URL              | Действие               | Пример запроса                                                                 |
|--------|------------------|------------------------|-------------------------------------------------------------------------------|
<<<<<<< HEAD
| `GET`  | `/postcards`     | Получить все открытки  | `curl -s http://localhost:5001/postcards jq`                                        |
| `POST` | `/postcards`     | Создать открытку       | `curl -X POST -H "Content-Type: application/json" -d '{"recipient":"Друг", "message":"Привет!"}' http://localhost:5001/postcards` |
=======
| `GET`  | `/postcards`     | Получить все открытки  | `curl http://localhost:5001/postcards`                                        |
| `POST` | `/postcards`     | Создать открытку       | `curl -X POST -H "Content-Type: application/json" \-d '{"recipient":"Тест", "message":"Проверка работы"}' \ http://localhost:5001/postcards` |
>>>>>>> 8f7897f7dfb7a30be66bc74fded63a19380a9e52
