# ReservationAndShared

A scalable backend system built with Django, MongoDB (Sharded), Celery, and Redis — fully containerized using Docker Compose with automated cluster setup.

---

## Tech Stack

- **Language**: Python 3.11  
- **Backend**: Django 5 + Django REST Framework  
- **Database**: MongoDB (Sharded + Replica Sets)  
- **Task Queue**: Celery + Redis  
- **Containerization**: Docker + Docker Compose  

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/ReservationService.git
cd ReservationService

```

### Create Virtual Environment & Install Dependencies
    python3.11 -m venv venv
    source venv/bin/activate    # Mac/Linux
    venv\Scripts\activate       # Windows
    pip install -r requirements.txt



## Start services,migrate DB, and run server

    docker compose up -d
    python manage.py migrate
    python manage.py runserver
