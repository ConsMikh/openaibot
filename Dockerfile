FROM python:3.10

RUN mkdir -p /app
RUN chmod 777 /app
WORKDIR /app

COPY src/ ./
COPY docker/ ./

RUN pip install --upgrade pip
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]