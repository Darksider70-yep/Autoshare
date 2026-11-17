@echo off
title AutoShare Ride-Booking Service (Port 8080)
echo ======================================================================
echo    AutoShare Ride-Booking Microservice (Port 8080)
echo ======================================================================
echo Starting Spring Boot on Port 8080 with dedicated Ride database...
echo Communicating with User Service on http://localhost:8081/api/users
echo.
cd /d "%~dp0backend"
java -jar "target\autoshare-backend-0.0.1-SNAPSHOT.jar" --spring.profiles.active=rides
pause
