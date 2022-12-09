FROM python:3.11-alpine
  
RUN apk --update add --no-cache
RUN apk add curl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser -D myuser
# RUN chown myuser:myuser /app

USER myuser

RUN python -m venv /home/myuser/venv
ENV PATH="/home/myuser/venv/bin:$PATH"

RUN pip install --upgrade pip
WORKDIR /app

COPY ./app/* /app/
ENV PATH="/home/myuser/.local/bin:$PATH" 

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py"]