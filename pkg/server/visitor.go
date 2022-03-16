package server

import (
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/kevinlutzer/personal-website-api/pkg/apperror"
)

type ErrorResponse struct {
	ErrorMsg string `json:"error"`
}

type SuccessResponse struct {
	Success string `json:"success"`
}

func (s *server) getIPFromHeader(h http.Header) (string, error) {
	ipHeaders := []string{"X-FORWARDED-FOR", "x-forwarded-for", "X-Forwarded-For"}
	for _, ipHeader := range ipHeaders {
		if ip := h.Get(ipHeader); ip != "" {
			return ip, nil
		}
	}

	return "", apperror.NewError(apperror.InvalidArguments, "x-forwarded-for header is required")
}

var errorTypeToCode = map[apperror.ErrorType]int{
	apperror.AlreadyExists: 409,
}

func (s *server) writeSuccessResponse(w http.ResponseWriter, msg string) {
	json, _ := json.Marshal(SuccessResponse{Success: msg})

	w.WriteHeader(200)
	w.Write(json)
}

func (s *server) writeErrorResponse(w http.ResponseWriter, err error) {
	var code int
	var ok bool
	var msg string

	appError, ok := err.(*apperror.RequestError)
	if !ok {
		msg = "Internal Error"
		code = 500
	}

	msg = err.Error()
	code, ok = errorTypeToCode[appError.Type]
	if !ok {
		code = 500
	}

	json, _ := json.Marshal(ErrorResponse{ErrorMsg: msg})

	w.WriteHeader(code)
	w.Write(json)
}

func (s *server) ReplaceVisitor(w http.ResponseWriter, r *http.Request) {
	ip, err := s.getIPFromHeader((r.Header))
	if err != nil {
		s.writeErrorResponse(w, err)
		return
	}

	if err := s.visitorService.Replace(ip, "Other"); err != nil {
		fmt.Println(err.Error())

		s.writeErrorResponse(w, err)
		return
	}

	s.writeSuccessResponse(w, "Successfully replaced the visitor information")

}
