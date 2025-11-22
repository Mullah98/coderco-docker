# Stage 1: Build Stage

FROM python:3.8-slim AS build

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Stage 2: Production Stage

FROM python:3.8-slim

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]