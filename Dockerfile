FROM golang:alpine

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN go build -o main cmd/main.go

ENTRYPOINT [ "/app/main" ]
EXPOSE 80