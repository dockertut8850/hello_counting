FROM hello_base:latest

RUN apt-get update && apt-get install -y python3-redis

COPY server.py /app/server.py
COPY test_server.py /app/test_server.py
