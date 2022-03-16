package visitor

import (
	"github.com/go-sql-driver/mysql"
	"github.com/kevinlutzer/personal-website-api/pkg/apperror"
	"gorm.io/gorm"
)

type repo struct {
	db *gorm.DB
}

func mySQLErrorCode(err error) error {
	var code uint16
	if val, ok := err.(*mysql.MySQLError); ok {
		code = val.Number
	}

	if code == 1062 {
		return apperror.NewError(apperror.AlreadyExists, "visitor already exists")
	}

	return apperror.NewError(apperror.Internal, "something happened")
}

// interface for exposed methods
type Repo interface {
	Create(vistor *Visitor) error
	Update(ip string, visitor_type string) error
}

func NewRepo(db *gorm.DB) Repo {
	db.AutoMigrate(&Visitor{})

	return &repo{
		db: db,
	}
}

func (s *repo) Create(vistor *Visitor) error {
	if tx := s.db.Create(vistor); tx.Error != nil {
		return mySQLErrorCode(tx.Error)
	}

	return nil
}

func (s *repo) Update(ip string, visitor_type string) error {
	tx := s.db.Model(&Visitor{}).
		Where("ip = ?", ip).
		Update("type", "hello")

	if tx.Error != nil {
		return mySQLErrorCode(tx.Error)
	}

	return nil
}
