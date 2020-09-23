package main

import (
    "errors"
    "os"

    log "github.com/sirupsen/logrus"
)


func something(env string) (string, error) {
    value := os.Getenv(env)

    if len(value) == 0 {
        return "", errors.New("variable not defined")
    }

    return value, nil
}


func doLogging() {
    fields := log.Fields{
        "animal": "walrus",
        "number": 1,
        "size": 10,
    }

    log.SetFormatter(&log.TextFormatter{
        FullTimestamp: true,
    })

    log.WithFields(fields).Info("A walrus informs")
    log.Trace("A walrus traces")
    log.Debug("A walrus debugs")
    log.Warn("A walrus is concerned")
    log.Error("A walrus screwed up")
}
