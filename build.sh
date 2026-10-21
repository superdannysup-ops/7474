#!/bin/sh
set -eu
if ! command -v gradle >/dev/null 2>&1; then
    echo 'Install Gradle 8.12.1 first, or build using the included GitHub Actions workflow.' >&2
    exit 1
fi
gradle build
echo 'Built: build/libs/hangulcraft-1.0.0.jar'
