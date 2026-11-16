@echo off
echo ========================================================
echo        Starting AutoShare Application Services
echo ========================================================
echo.
echo Starting Backend in a new window (Port 8080)...
start "AutoShare Backend" cmd /k "cd /d %~dp0backend && java -jar target\autoshare-backend-0.0.1-SNAPSHOT.jar"

echo Starting Frontend in a new window (Port 3000)...
start "AutoShare Frontend" cmd /k "cd /d %~dp0 && npm run dev"

echo.
echo ========================================================
echo AutoShare services launched!
echo - Frontend UI:  http://localhost:3000
echo - Backend API:  http://localhost:8080/api/rides
echo - H2 Database:  http://localhost:8080/h2-console
echo ========================================================
pause
