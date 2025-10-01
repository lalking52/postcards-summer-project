# Postcard Microservice

**A simple service for creating and storing postcards**  
Accepts a recipient (name, etc.) and a message as input. Request format as shown in the example.  
*Flask + PostgreSQL in Docker*

## Project Setup

1. Launch the project:
   ```bash
   git clone https://github.com/ваш-логин/first.git
   cd first
   docker-compose up -d
2. Open in your browser:
http://localhost:5001
## Technologies
Backend: Python Flask
Database: PostgreSQL
Infrastructure: Docker

## API Endpoints

| Method  | URL              | Actiom               | Example Request                                                                |
|--------|------------------|------------------------|-------------------------------------------------------------------------------|
| `GET`  | `/postcards`     | Get all postcards      | `curl -s http://localhost:5001/postcards \| jq`                                        |
| `POST` | `/postcards`     |Create a postcard       | `curl -X POST -H "Content-Type: application/json" -d '{"recipient":"Friend", "message":"Hi!"}' http://localhost:5001/postcards` |

