# ReservationAndShared

A scalable backend system built with Django, MongoDB (sharded), Celery, and Redis—fully containerized using Docker Compose with automated cluster setup.

---

## Tech Stack

**Backend**: Django  
**Database**: MongoDB (Sharded + Replica Sets)  
**Task Queue**: Celery + Redis  
**Containerization**: Docker + Docker Compose  


---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ReservationService.git
cd ReservationService

```

## Start services, install dependencies, migrate DB, and run server

docker compose up -d
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
