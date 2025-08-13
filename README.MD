# Shared and Inventory

A scalable backend system for shared resources and inventory management, built with Django, MongoDB, Celery, Redis, and Docker. Supports async jobs, health checks, and admin APIs.

## Tech Stack

- **Django** – Web framework
- **MongoDB** – NoSQL database
- **Celery + Redis** – Background task processing
- **Docker + Docker Compose** – Containerized development

## Features

- Async reconciliation jobs via Celery
- Health check and metrics endpoints
- Admin APIs for internal operations
- Dockerized setup for easy local development
- MongoDB collections instead of Django ORM

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- MongoDB running locally or via Docker

### Setup

```bash
git clone https://github.com/your-username/shared-and-inventory.git
cd SharedAndInventory
docker-compose up --build