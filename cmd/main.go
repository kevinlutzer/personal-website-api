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

func main() {

	// Setup DB
	dns := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local", "personal-website-api", "JWUyMfDMGIJpgxQ2a0/9henWzWqRGYuPygbUxtEnIhM=", "localhost", 3306, "personal-website")
	db, err := gorm.Open(mysql.Open(dns), &gorm.Config{})
	if err != nil {
		log.Fatalf("Failed to connect to the database: %s\n", err.Error())
		os.Exit(10)
	}

	// Visitor
	visitorRepo := visitor.NewRepo(db)
	visitorService := visitor.NewService((visitorRepo))

	server := server.NewServer(visitorService)

	// Routes
	http.HandleFunc("/v1/visitor/replace", server.ReplaceVisitor)
	http.ListenAndServe(":80", nil)
}
