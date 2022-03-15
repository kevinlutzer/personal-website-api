package apperror

import "fmt"

type ErrorType string

const (
	AlreadyExists    ErrorType = "AlreadyExists"
	NotFound         ErrorType = "NotFound"
	Internal         ErrorType = "Internal"
	InvalidArguments ErrorType = "InvalidArguments"
)

type RequestError struct {
	Type ErrorType
	Msg  string
}

func (r *RequestError) Error() string {
	return fmt.Sprintf("%s: %s", r.Type, r.Msg)
}

func NewError(errorType ErrorType, msg string) error {
	return &RequestError{
		Type: errorType,
		Msg:  msg,
	}
}
