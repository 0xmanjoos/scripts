// Very useful for web fuzzing in htb dante
// This is just the base fuzzer, if you want to change this into a web fuzzer its not that hard
package main

import (
	"fmt"
	"net/http"
	"os"
	"io/ioutil"
	"golang.org/x/net/proxy"
)

const (
	url = "http://172.16.1.20/"
	proxyaddr = "127.0.0.1:9001"
)


func main() {
	// CREATE PROXY DIALER
	dialer, err := proxy.SOCKS5("tcp", proxyaddr, nil, proxy.Direct)

	if err != nil {
		fmt.Fprintln(os.Stderr, "Could not create dial:", err)
		os.Exit(1)
}

	httpTransport := &http.Transport{}
	httpClient := &http.Client{Transport: httpTransport}
	// setup socks5 proxy as our dialer
	httpTransport.Dial = dialer.Dial

	// create the request
	req, err := http.NewRequest("GET", url, nil)

	if err != nil {
		fmt.Fprintln(os.Stderr, "cant create request: ", err)
		os.Exit(2)
}

	response, err := httpClient.Do(req)

	if err != nil {
		fmt.Fprintln(os.Stderr, "cant GET page", err)
		os.Exit(3)
}

	defer response.Body.Close()

	b, err := ioutil.ReadAll(response.Body)

	if err != nil {
		fmt.Fprintln(os.Stderr, "error reading body: ", err)
		os.Exit(4)
	}
	fmt.Println(string(b))

}
