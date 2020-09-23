// +build !test

package main

import (
    "fmt"
    "os"
)


func main() {
    doLogging()

    text, err := something("SHELL")
    if err != nil {
        os.Exit(1)
    }

    fmt.Println(text)
}
