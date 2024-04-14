FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
#Changes in main branch and another change. Got added from dis
#Changes at zero commit in main branch
#Changes from newb branch using base zero commit from main

