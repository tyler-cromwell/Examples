package main

import (
    "math/rand"
    "os"
    "testing"
)


func BenchmarkSomething(b *testing.B) {
    for i := 0; i < b.N; i++ {
        rand.Int()
    }
}


func TestDoLogging(t *testing.T) {
    doLogging()
}


// The "main" method for the TESTING MODULE
func TestMain(m *testing.M) {
    // Call flag.Parse() here if TestMain uses flags
    // BEFORE tests
    status := m.Run()
    // AFTER tests
    os.Exit(status)
}


func TestSomething(t *testing.T) {
    text, err := something("HELLO")

    if err == nil {
        t.Errorf("something(\"HELLO\") = %s; want \"\"", text)
    }
}
