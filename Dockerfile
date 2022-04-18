FROM python:alpine3.10

RUN mkdir /app
COPY . /app

WORKDIR /app

# install python dependencies
RUN apk add gcc linux-headers musl-dev libc-dev python3-dev libffi-dev openssl  openldap-dev
RUN apk add g++ zlib zlib-dev jpeg-dev 

# install server dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]