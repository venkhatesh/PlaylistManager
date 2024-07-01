FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

COPY database /app/database

COPY tests /app/tests

RUN mkdir -p /app/logs

RUN python -m unittest discover -s tests -v 

EXPOSE 5000

CMD ["python", "backend/app.py"]
