@echo off
where gradle >nul 2>nul
if errorlevel 1 (
    echo Gradle not found. Install Gradle 8.12.1 or open this project in IntelliJ with Gradle.
    exit /b 1
)
gradle build
if errorlevel 1 exit /b 1
echo Built: build\libs\hangulcraft-1.0.0.jar
