FROM python:3.9-slim

WORKDIR /app

COPY flask_app.py .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "flask_app.py"]
