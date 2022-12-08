FROM python:3.9-alpine
  
RUN apk --update add --no-cache
RUN apk add curl
RUN pip install --upgrade pip

RUN adduser -D myuser
USER myuser

RUN mkdir -p /home/myuser/app/data_ext
WORKDIR /home/myuser/app

COPY ./app /home/myuser/app
ENV PATH="/home/myuser/.local/bin:$PATH" 

RUN pip install  --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py"]