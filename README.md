# Redis Playground

A simple Python application that demonstrates basic Redis operations using Docker.

## Features

- Redis key-value storage
- Queue operations (LPUSH/RPOP)
- TTL (Time To Live) for keys
- Dockerized environment

## Prerequisites

- Docker
- Docker Compose
- Make (optional, for using Makefile commands)

## Setup

1. Clone the repository
2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   The `.env` file contains:
   ```
   REDIS_HOST=redis
   REDIS_PORT=6379
   ```

## Running the Application

You can run the application in two ways:

1. Using Docker Compose directly:
```bash
docker compose up
```

2. Using the Makefile (recommended):
```bash
make up
```

The application will:
1. Connect to Redis
2. Set a key with a 10-second TTL
3. Push two tasks to a queue
4. Process the tasks from the queue

## Connecting to Redis

You can connect to Redis in two ways:

1. Using local Redis CLI (if installed):
```bash
redis-cli -h localhost -p 6379
```

2. Using Redis CLI from the container:
```bash
docker compose exec redis redis-cli
```

## Project Structure

```
.
├── main.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── .env.example
├── LICENSE
└── README.md
```

## Services

- **redis**: Redis server (v7.4.2)
- **app**: Python application demonstrating Redis operations

## Environment Variables

- `REDIS_HOST`: Redis server hostname
- `REDIS_PORT`: Redis server port 