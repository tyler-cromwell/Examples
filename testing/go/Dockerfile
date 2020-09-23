FROM golang:1.15

WORKDIR $GOPATH/src
RUN mkdir ./app
WORKDIR ./app
COPY test.sh ./
COPY *.go ./
COPY go.mod ./
COPY go.sum ./
ENV PATH $PATH:/usr/local/go/bin
RUN go get
RUN go build
CMD ["./test.sh"]
