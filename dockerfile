FROM python:3.12-slim

WORKDIR /weather_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY  weather_bot/config/ .env

CMD ["python", "main.py"]
