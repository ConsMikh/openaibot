FROM python:3.10

RUN mkdir -p /app
RUN CHMOD 777 /app
WORKDIR /app

COPY src/ ./
COPY docker/ ./ 

RUN pip install --upgrade pip

ENTRYPOINT ["/app/entrypoint.sh"]
