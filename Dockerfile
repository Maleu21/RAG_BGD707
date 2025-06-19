FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y datasets && \
    pip install --no-cache-dir "datasets>=2.18.0"

COPY . .

CMD ["python3", "main.py"]

