#!/bin/bash

go test -v -coverprofile coverage.out -failfast -tags test -bench .
go tool cover -html=coverage.out -o coverage.html
