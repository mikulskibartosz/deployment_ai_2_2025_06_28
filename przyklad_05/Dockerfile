# Przykład 05
FROM python:3.13-slim as builder

WORKDIR /app

COPY ./requirements_build.txt .
RUN pip install -r requirements_build.txt

COPY . .

RUN python build.py

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/summary.json .
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
