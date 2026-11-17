@echo off
title AutoShare Launcher
echo ======================================================================
echo           Starting AutoShare Microservices Architecture
echo ======================================================================
echo.
echo [1/3] Launching User-Management Service on Port 8081...
start "AutoShare User Service (:8081)" cmd /k "cd /d %~dp0backend && java -jar target\autoshare-backend-0.0.1-SNAPSHOT.jar --spring.profiles.active=users"

echo [2/3] Launching Ride-Booking Service on Port 8080...
start "AutoShare Ride Service (:8080)" cmd /k "cd /d %~dp0backend && java -jar target\autoshare-backend-0.0.1-SNAPSHOT.jar --spring.profiles.active=rides"

echo [3/3] Launching React 19 Frontend on Port 3000...
start "AutoShare Frontend (:3000)" cmd /k "cd /d %~dp0 && npm run dev"

echo.
echo ======================================================================
echo All AutoShare services successfully launched across separate ports!
echo.
echo  - Frontend Web UI:        http://localhost:3000
echo  - User-Management API:    http://localhost:8081/api/users
echo  - User H2 Database:       http://localhost:8081/h2-console  (JDBC: jdbc:h2:mem:userdb)
echo  - Ride-Booking API:       http://localhost:8080/api/rides
echo  - Ride H2 Database:       http://localhost:8080/h2-console  (JDBC: jdbc:h2:mem:ridedb)
echo  - Topology & Simulator:   http://localhost:8080/api/microservices/topology
echo ======================================================================
echo.
pause
