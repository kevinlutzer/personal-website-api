package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/kevinlutzer/personal-website-api/pkg/server"
	"github.com/kevinlutzer/personal-website-api/pkg/visitor"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Code  string
	Price uint
}

func main() {

	dns := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local", "personal-website-api", "JWUyMfDMGIJpgxQ2a0/9henWzWqRGYuPygbUxtEnIhM=", "localhost", 3306, "personal-website")
	db, err := gorm.Open(mysql.Open(dns), &gorm.Config{})
	if err != nil {
		log.Fatalf("Failed to connect to the database: %s\n", err.Error())
		os.Exit(10)
	}

	visitorRepo := visitor.NewRepo(db)
	visitorService := visitor.NewService((visitorRepo))

	server := server.NewServer(visitorService)

	// Routes
	http.HandleFunc("/v1/visitor/create", server.CreateVisitor)
	http.ListenAndServe(":8080", nil)
}
