package visitor

import "github.com/kevinlutzer/personal-website-api/pkg/apperror"

type service struct {
	repo Repo
}

type Service interface {
	Replace(ip string, visitor_type string) error
}

func NewService(repo Repo) Service {
	return &service{repo: repo}
}

func (s *service) Replace(ip string, visitor_type string) error {
	err := s.repo.Create(&Visitor{IP: ip, Type: visitor_type})
	if err != nil && apperror.IsError(apperror.AlreadyExists, err) {
		return s.repo.Update(ip, visitor_type)
	}

	return nil
}
