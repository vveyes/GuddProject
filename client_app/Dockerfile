# client_app/Dockerfile
FROM python

WORKDIR /app

COPY client_app/requirements.txt /app/client_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "app/client_app.py"]