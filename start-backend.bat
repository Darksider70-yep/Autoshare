@echo off
echo Starting AutoShare Backend (Spring Boot 3.3.4)...
cd /d "%~dp0backend"
java -jar "target\autoshare-backend-0.0.1-SNAPSHOT.jar"
pause
