@echo off
title AutoShare User-Management Service (Port 8081)
echo ======================================================================
echo    AutoShare User-Management Microservice (Port 8081)
echo ======================================================================
echo Starting Spring Boot on Port 8081 with dedicated User database...
echo.
cd /d "%~dp0backend"
java -jar "target\autoshare-backend-0.0.1-SNAPSHOT.jar" --spring.profiles.active=users
pause
