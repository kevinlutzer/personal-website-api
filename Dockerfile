FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/kevinlutzer/personal-website-api
RUN go build . 

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/personal-website-api

# Document that the service listens on port 8080.
EXPOSE 8080