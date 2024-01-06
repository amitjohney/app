FROM python:3.8-slim-buster
WORKDIR /app
COPY test.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3","app.py"]