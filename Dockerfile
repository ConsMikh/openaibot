FROM python:3.10-alpine

WORKDIR /usr/src/app
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./

CMD [ "python", "./bot.py" ]