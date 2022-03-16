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

	// Db credentails and setup
	dbHost := os.Getenv("DB_HOST")
	dbPassword := os.Getenv("DB_PASSWORD")
	dbUser := os.Getenv("DB_USER")

	dns := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8&parseTime=True&loc=Local", dbUser, dbPassword, dbHost, 3306, "personalwebsite")
	db, err := gorm.Open(mysql.Open(dns), &gorm.Config{})
	if err != nil {
		log.Fatalf("Failed to connect to the database: %s\n", err.Error())
		os.Exit(10)
	}

	// Setup visitor
	visitorRepo := visitor.NewRepo(db)
	visitorService := visitor.NewService((visitorRepo))

	server := server.NewServer(visitorService)

	// Routes
	http.HandleFunc("/v1/visitor/replace", server.ReplaceVisitor)
	http.ListenAndServe(":80", nil)
}
