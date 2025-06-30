FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

ENV SAGES_ENV=123
ENV OVERRIDE_ENV=456

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]