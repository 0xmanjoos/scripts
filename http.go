package main

import (
	"fmt"
	"net/http"
	"os"
	"io/ioutil"
	"github.com/yosssi/gohtml"
)

func main() {
	url := "https://youtube.com"
	response, err := http.Get(url)

	check(err)
//	fmt.Println(response)

	body, _ := ioutil.ReadAll(response.Body)
	fmt.Println(gohtml.Format(string(body)))

	response.Body.Close()
}

func check(err error) {

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
