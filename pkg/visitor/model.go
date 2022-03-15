package visitor

import (
	"time"
)

type Visitor struct {
	IP      string `gorm:"primaryKey;size:48"`
	Type    string
	Created time.Time `gorm:"autoCreateTime"`
}

func (Visitor) TableName() string {
	return "visitor"
}
