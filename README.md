# Django Celery Redis Demo

This project was create to showcase how to use celery with Django/DRF to have api endpoints that allow a user to kick off long running tasks and view the results of those task when they are done.

## Install Instructions
1. Run `docker run -d -p 6379:6379 redis`
2. Install requirements.txt `pip install requirements.txt`
3. Start celery in a terminal `celery -A django_celery_redis_demo worker --loglevel=INFO`
4. Start django in another terminal `python3 manage.py runserver`
5. Start using api

## API Endpoints
| URL       | Method | Description | 
| -------- | - |  - | 
| /api/v1/generate_task/                | POST | Start a long running task
| /api/v1/task_status/?task_id={task_id}| GET  | View status of task
| /api/v1/task_result/?task_id={task_id}| GET  | View results of task