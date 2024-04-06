FROM python:3.10

RUN mkdir /fastapi-app

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8000

CMD ["python", "main.py"]
