FROM python:3.9.13-slim

WORKDIR /app
# RUN pip install gunicorn==20.1.0
COPY requirements.txt .
RUN pip install -r /app/requirements.txt --no-cache-dir
COPY . .

CMD python manage.py collectstatic --noinput && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 blogs.wsgi:application --reload
# CMD ["gunicorn", "blogs.wsgi:application", "--bind", "0:8000"]