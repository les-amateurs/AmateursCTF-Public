FROM golang:1.20.5

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY main.go flag.txt index.html ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /bot

EXPOSE 7000

CMD ["/bot"]