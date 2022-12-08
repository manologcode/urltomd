FROM python:3.11-alpine
  
RUN apk --update add --no-cache
RUN apk add curl

#RUN pip install --upgrade pip --user

RUN adduser -D myuser
USER myuser

RUN mkdir -p /home/myuser/app/data_ext
WORKDIR /home/myuser/app

COPY ./app /home/myuser/app
ENV PATH="/home/myuser/.local/bin:$PATH" 

RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py"]