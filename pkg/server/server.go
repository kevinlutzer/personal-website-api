package server

import (
	"net/http"
)

type server struct {
	// visitorService visitor.Service
}

type Server interface {
	CreateVisitor(w http.ResponseWriter, r *http.Request)
}

func NewServer() Server {
	return &server{
		// visitorService: visitorService,
	}
}
