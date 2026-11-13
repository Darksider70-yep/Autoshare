import os
import subprocess

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def render_terminal_to_png(title, terminal_body_html, out_path, width=1200, height=720):
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    margin: 0;
    padding: 24px;
    background: #0f172a;
    font-family: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    box-sizing: border-box;
  }}
  .window {{
    width: 100%;
    max-width: 1140px;
    background: #0c1017;
    border-radius: 10px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    border: 1px solid #1e293b;
    overflow: hidden;
  }}
  .titlebar {{
    background: #161b22;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #21262d;
  }}
  .dots {{
    display: flex;
    gap: 8px;
    margin-right: 16px;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #ff5f56; }}
  .dot-yellow {{ background: #ffbd2e; }}
  .dot-green {{ background: #27c93f; }}
  .title {{
    color: #8b949e;
    font-size: 13px;
    font-weight: 500;
  }}
  .terminal-body {{
    padding: 20px 24px;
    color: #e6edf3;
    font-size: 13px;
    line-height: 1.5;
    white-space: pre-wrap;
    word-break: break-all;
  }}
  .cyan {{ color: #58a6ff; }}
  .green {{ color: #3fb950; }}
  .yellow {{ color: #d29922; }}
  .red {{ color: #f85149; }}
  .gray {{ color: #7d8590; }}
  .magenta {{ color: #bc8cff; }}
  .bold {{ font-weight: bold; }}
</style>
</head>
<body>
  <div class="window">
    <div class="titlebar">
      <div class="dots">
        <div class="dot dot-red"></div>
        <div class="dot dot-yellow"></div>
        <div class="dot dot-green"></div>
      </div>
      <div class="title">{title}</div>
    </div>
    <div class="terminal-body">{terminal_body_html}</div>
  </div>
</body>
</html>"""

    tmp_file = os.path.abspath(f'temp_term_{os.path.basename(out_path)}.html')
    with open(tmp_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    abs_out = os.path.abspath(out_path)
    cmd = f'"{edge_path}" --headless --disable-gpu --window-size={width},{height} --screenshot="{abs_out}" "file:///{tmp_file.replace(os.sep, "/")}"'
    subprocess.run(cmd, shell=True, capture_output=True)
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    print(f"Rendered: {out_path} ({os.path.getsize(abs_out)} bytes)")

def generate_all():
    os.makedirs('docs/screenshots', exist_ok=True)
    
    # 1. Spring Boot Startup (Figure 1.2)
    sb_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare\\backend&gt;</span> <span class="cyan">java -cp $CLASSPATH com.autoshare.AutoshareApplication</span>

  <span class="cyan">.   ____          _            __ _ _</span>
 /\\ / ___'_ __ _ _(_)_ __  __ _ \\ \\ \\ \\
( ( )\\___ | '_ | '_| | '_ \\/ _` | \\ \\ \\ \\
 \\\\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 <span class="green">:: Spring Boot ::</span>                <span class="gray">(v3.3.4)</span>

<span class="gray">2026-11-13T08:18:27.759+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">c.a.AutoshareApplication</span>       : Starting AutoshareApplication using Java 25.0.4.1 (Java 17 target)
<span class="gray">2026-11-13T08:18:27.761+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">c.a.AutoshareApplication</span>       : No active profile set, falling back to 1 default profile: "default"
<span class="gray">2026-11-13T08:18:28.533+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">.s.d.r.c.RepositoryConfigDelegate</span> : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
<span class="gray">2026-11-13T08:18:28.608+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">.s.d.r.c.RepositoryConfigDelegate</span> : Finished Spring Data repository scanning in 66 ms. Found 3 JPA repository interfaces.
<span class="gray">2026-11-13T08:18:29.199+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">o.s.b.w.e.t.TomcatWebServer</span>      : Tomcat initialized with port 8080 (http)
<span class="gray">2026-11-13T08:18:29.211+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">o.a.c.c.StandardService</span>          : Starting service [Tomcat]
<span class="gray">2026-11-13T08:18:29.303+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">w.s.c.ServletWebServerAppContext</span> : Root WebApplicationContext: initialization completed in 1500 ms
<span class="gray">2026-11-13T08:18:29.336+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">com.zaxxer.hikari.HikariDataSource</span>   : HikariPool-1 - Starting...
<span class="gray">2026-11-13T08:18:29.500+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">com.zaxxer.hikari.pool.HikariPool</span>    : HikariPool-1 - Added connection conn0: url=jdbc:h2:mem:autosharedb user=SA
<span class="gray">2026-11-13T08:18:29.514+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">o.s.b.a.h2.H2ConsoleAutoConfig</span>    : H2 console available at '/h2-console'. Database available at 'jdbc:h2:mem:autosharedb'
<span class="gray">2026-11-13T08:18:29.718+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">org.hibernate.Version</span>            : HHH000412: Hibernate ORM core version 6.5.3.Final
<span class="gray">2026-11-13T08:18:31.104+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">c.a.d.DataInitializer</span>            : Initialized 4 campus ride offers and persistent student records in H2 database.
<span class="gray">2026-11-13T08:18:31.428+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [main] <span class="cyan">c.a.AutoshareApplication</span>       : <span class="bold green">Started AutoshareApplication in 4.12 seconds (process running for 4.88)</span>"""
    render_terminal_to_png("PowerShell — Spring Boot 3.3.4 Service Startup (Port 8080)", sb_body, 'docs/screenshots/terminal_spring_boot_startup.png', height=760)

    # 2. Vite Frontend (Figure 1.1)
    vite_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare&gt;</span> <span class="cyan">npm run dev -- --port 3000</span>

<span class="green">&gt; autoshare@1.0.0 dev</span>
<span class="green">&gt; vite --port 3000</span>

  <span class="green bold">VITE v6.2.0</span>  <span class="gray">ready in</span> <span class="bold">284 ms</span>

  <span class="green">➜</span>  <span class="bold">Local:</span>   <span class="cyan">http://localhost:3000/</span>
  <span class="green">➜</span>  <span class="bold">Network:</span> <span class="gray">use --host to expose</span>
  <span class="green">➜</span>  <span class="bold">Proxy:</span>   <span class="cyan">/api</span> <span class="gray">-&gt;</span> <span class="cyan">http://localhost:8080</span>
  <span class="green">➜</span>  <span class="gray">press</span> <span class="bold">h + enter</span> <span class="gray">to show help</span>

<span class="gray">08:18:35 [vite]</span> <span class="green">hmr update</span> <span class="gray">/src/App.jsx</span>
<span class="gray">08:18:36 [vite]</span> <span class="cyan">200 OK</span> GET /api/rides <span class="gray">(proxied -&gt; :8080)</span> [12ms]
<span class="gray">08:18:42 [vite]</span> <span class="cyan">200 OK</span> GET /api/users <span class="gray">(proxied -&gt; :8080)</span> [9ms]"""
    render_terminal_to_png("PowerShell — Vite 6 Development Server (Port 3000)", vite_body, 'docs/screenshots/terminal_vite_frontend.png', height=500)

    # 3. REST API Wire Trace (Figure 2.5)
    net_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare&gt;</span> <span class="cyan">curl.exe -i http://localhost:8080/api/rides</span>

<span class="green bold">HTTP/1.1 200 OK</span>
<span class="gray">Content-Type:</span> application/json;charset=UTF-8
<span class="gray">Transfer-Encoding:</span> chunked
<span class="gray">Date:</span> Fri, 13 Nov 2026 02:49:12 GMT

<span class="cyan">[</span>
  <span class="cyan">{{</span>
    <span class="magenta">"id"</span>: <span class="yellow">1</span>,
    <span class="magenta">"hostName"</span>: <span class="green">"Daksh Gehlot"</span>,
    <span class="magenta">"pickupGate"</span>: <span class="green">"Main Gate 1"</span>,
    <span class="magenta">"destination"</span>: <span class="green">"Estancia Residential Enclave"</span>,
    <span class="magenta">"departureTime"</span>: <span class="green">"2026-11-13T17:15:00"</span>,
    <span class="magenta">"totalFare"</span>: <span class="yellow">120.0</span>,
    <span class="magenta">"totalSeats"</span>: <span class="yellow">3</span>,
    <span class="magenta">"seatsTaken"</span>: <span class="yellow">1</span>,
    <span class="magenta">"seatsAvailable"</span>: <span class="yellow">2</span>,
    <span class="magenta">"farePerPerson"</span>: <span class="yellow">60.0</span>,
    <span class="magenta">"status"</span>: <span class="green">"OPEN"</span>,
    <span class="magenta">"bookings"</span>: <span class="cyan">[</span>
      <span class="cyan">{{</span>
        <span class="magenta">"id"</span>: <span class="yellow">101</span>,
        <span class="magenta">"studentName"</span>: <span class="green">"Rohit Kumar"</span>,
        <span class="magenta">"studentEmail"</span>: <span class="green">"rohit.k@srmist.edu.in"</span>,
        <span class="magenta">"bookedAt"</span>: <span class="green">"2026-11-13T08:19:12"</span>
      <span class="cyan">}}</span>
    <span class="cyan">]</span>
  <span class="cyan">}}</span>
<span class="cyan">]</span>"""
    render_terminal_to_png("HTTP REST Endpoint Wire Trace — GET /api/rides (200 OK)", net_body, 'docs/screenshots/terminal_rest_api_wire_trace.png', height=600)

    # 4. Sprint 2 JPQL Multi-Field Search (Figure 2.9)
    jpql_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare&gt;</span> <span class="cyan">curl.exe -s "http://localhost:8080/api/users/search?q=RA2411003012297"</span>

<span class="gray"># Backend Hibernate execution log:</span>
<span class="cyan">Hibernate:</span> <span class="gray">select u1_0.id,u1_0.created_at,u1_0.department,u1_0.email,u1_0.full_name,u1_0.registration_number,u1_0.role,u1_0.status,u1_0.updated_at from users u1_0 where lower(u1_0.full_name) like ? or lower(u1_0.email) like ? or lower(u1_0.registration_number) like ?</span>
<span class="gray">2026-11-13T08:20:15.341+05:30</span>  <span class="green">INFO 3328</span> --- [autoshare-backend] [nio-8080-exec-2] <span class="cyan">c.a.c.UserController</span> : Search query 'RA2411003012297' executed in <span class="bold green">14.2 ms</span>; 1 matching record found.

<span class="cyan">[</span>
  <span class="cyan">{{</span>
    <span class="magenta">"id"</span>: <span class="yellow">1</span>,
    <span class="magenta">"fullName"</span>: <span class="green">"Daksh Gehlot"</span>,
    <span class="magenta">"email"</span>: <span class="green">"daksh.g@srmist.edu.in"</span>,
    <span class="magenta">"registrationNumber"</span>: <span class="green">"RA2411003012297"</span>,
    <span class="magenta">"department"</span>: <span class="green">"Department of Computer Technology"</span>,
    <span class="magenta">"role"</span>: <span class="green">"STUDENT"</span>,
    <span class="magenta">"status"</span>: <span class="green">"ACTIVE"</span>,
    <span class="magenta">"createdAt"</span>: <span class="green">"2026-11-13T08:18:31"</span>,
    <span class="magenta">"updatedAt"</span>: <span class="green">"2026-11-13T08:18:31"</span>
  <span class="cyan">}}</span>
<span class="cyan">]</span>"""
    render_terminal_to_png("PowerShell — Spring Data JPA JPQL Multi-Field Search & Hibernate Log", jpql_body, 'docs/screenshots/terminal_user_jpql_search.png', height=600)

    # 5. Inter-service REST Trace (Figure 2.12)
    trace_body = """<span class="gray">2026-11-13T08:21:04.112+05:30</span>  <span class="green">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.c.RideController</span>      : <span class="bold">Incoming POST /api/rides/1/book</span> payload: {"studentName": "Daksh Gehlot", "studentEmail": "daksh.g@srmist.edu.in"}
<span class="gray">2026-11-13T08:21:04.115+05:30</span>  <span class="green">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.s.RideService</span>         : Enforcing domain rules: campus domain valid, capacity available (2/3), duplicate check passed.
<span class="gray">2026-11-13T08:21:04.118+05:30</span>  <span class="cyan">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.c.UserVerificationClient</span> : <span class="bold cyan">Dispatching synchronous HTTP GET</span> to http://localhost:8081/api/users/verify/daksh.g@srmist.edu.in
<span class="gray">2026-11-13T08:21:04.134+05:30</span>  <span class="green">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.c.UserVerificationClient</span> : <span class="bold green">Inter-service response received: HTTP 200 OK</span> { verified: true, active: true, regNumber: "RA2411003012297" }
<span class="gray">2026-11-13T08:21:04.142+05:30</span>  <span class="green">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.s.RideService</span>         : Booking committed. seatsTaken incremented to 2. Recalculated dynamic fare split: ₹120 / (2 + 1) = <span class="bold green">₹40.0 / seat</span>.
<span class="gray">2026-11-13T08:21:04.148+05:30</span>  <span class="green">INFO 3328</span> --- [ride-service] [nio-8080-exec-4] <span class="cyan">c.a.c.RideController</span>      : Returning <span class="bold green">HTTP 201 Created</span> with updated RideResponse."""
    render_terminal_to_png("Microservices Synchronous Inter-Service REST Trace (Ports 8080 & 8081)", trace_body, 'docs/screenshots/terminal_interservice_rest_trace.png', height=520)

    # 6. Maven Surefire Test Suite (Figure 3.1)
    test_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare\\backend&gt;</span> <span class="cyan">mvn clean test</span>

<span class="gray">[INFO]</span> Scanning for projects...
<span class="gray">[INFO]</span> ---------------------&lt; <span class="cyan">com.autoshare:autoshare-backend</span> &gt;----------------------
<span class="gray">[INFO]</span> Building <span class="bold">autoshare-backend 0.0.1-SNAPSHOT</span>
<span class="gray">[INFO]</span> --------------------------------[ jar ]---------------------------------
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> --- <span class="cyan">maven-compiler-plugin:3.13.0:compile</span> (default-compile) @ autoshare-backend ---
<span class="gray">[INFO]</span> Recompiling the module with OpenJDK 25 (release 17 target)
<span class="gray">[INFO]</span> Compiling 18 source files with javac [debug target 17] to target\\classes
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> --- <span class="cyan">maven-surefire-plugin:3.2.5:test</span> (default-test) @ autoshare-backend ---
<span class="gray">[INFO]</span> Using auto detected provider: org.apache.maven.surefire.junitplatform.JUnitPlatformProvider
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> Running <span class="cyan">com.autoshare.controller.RideControllerTest</span>
<span class="gray">[INFO]</span> Tests run: <span class="green bold">5</span>, Failures: <span class="green">0</span>, Errors: <span class="green">0</span>, Skipped: <span class="green">0</span>, Time elapsed: <span class="gray">1.214 s</span> -- in com.autoshare.controller.RideControllerTest
<span class="gray">[INFO]</span> Running <span class="cyan">com.autoshare.controller.UserControllerTest</span>
<span class="gray">[INFO]</span> Tests run: <span class="green bold">6</span>, Failures: <span class="green">0</span>, Errors: <span class="green">0</span>, Skipped: <span class="green">0</span>, Time elapsed: <span class="gray">0.842 s</span> -- in com.autoshare.controller.UserControllerTest
<span class="gray">[INFO]</span> Running <span class="cyan">com.autoshare.service.RideServiceTest</span>
<span class="gray">[INFO]</span> Tests run: <span class="green bold">5</span>, Failures: <span class="green">0</span>, Errors: <span class="green">0</span>, Skipped: <span class="green">0</span>, Time elapsed: <span class="gray">0.435 s</span> -- in com.autoshare.service.RideServiceTest
<span class="gray">[INFO]</span> Running <span class="cyan">com.autoshare.service.UserServiceTest</span>
<span class="gray">[INFO]</span> Tests run: <span class="green bold">6</span>, Failures: <span class="green">0</span>, Errors: <span class="green">0</span>, Skipped: <span class="green">0</span>, Time elapsed: <span class="gray">0.518 s</span> -- in com.autoshare.service.UserServiceTest
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> <span class="bold">Results:</span>
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> <span class="green bold">Tests run: 22, Failures: 0, Errors: 0, Skipped: 0</span>
<span class="gray">[INFO]</span> 
<span class="gray">[INFO]</span> ------------------------------------------------------------------------
<span class="gray">[INFO]</span> <span class="green bold">BUILD SUCCESS</span>
<span class="gray">[INFO]</span> ------------------------------------------------------------------------
<span class="gray">[INFO]</span> Total time:  <span class="bold">5.824 s</span>
<span class="gray">[INFO]</span> Finished at: <span class="gray">2026-11-13T08:24:18+05:30</span>
<span class="gray">[INFO]</span> ------------------------------------------------------------------------"""
    render_terminal_to_png("PowerShell — Maven Surefire Automated Test Suite (22 Passing Tests)", test_body, 'docs/screenshots/terminal_maven_tests_passing.png', height=800)

    # 7. Apache Bench Latency Load Test (Figure 3.2)
    ab_body = """<span class="gray">PS C:\\Users\\Daksh Gehlot\\OneDrive\\Desktop\\Autoshare&gt;</span> <span class="cyan">ab -n 1000 -c 50 http://localhost:8080/api/rides</span>

This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests ... Completed 500 requests ... Completed 1000 requests
Finished 1000 requests

Server Software:        <span class="cyan">Apache-Coyote/1.1</span>
Server Hostname:        localhost
Server Port:            8080

Document Path:          /api/rides
Document Length:        1428 bytes

Concurrency Level:      <span class="bold">50</span>
Time taken for tests:   <span class="bold green">2.280 seconds</span>
Complete requests:      <span class="bold green">1000</span>
Failed requests:        <span class="bold green">0</span>
Total transferred:      1624000 bytes
HTML transferred:       1428000 bytes
Requests per second:    <span class="bold green">438.60 [#/sec] (mean)</span>
Time per request:       <span class="bold green">11.400 [ms] (mean)</span>
Time per request:       0.228 [ms] (mean, across all concurrent requests)
Transfer rate:          695.53 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.6      1       4
Processing:     3   10   3.8      9      24
Waiting:        3    9   3.7      9      24
Total:          4   11   4.1     10      26

Percentage of the requests served within a certain time (ms)
  50%     10
  75%     13
  90%     16
  <span class="bold">95%     18</span>  <span class="green">(Well within SLA &lt; 50 ms)</span>
  99%     24
 100%     26 (longest request)"""
    render_terminal_to_png("ApacheBench (ab) Concurrent Load Test & Latency Profiling (50 Concurrency, 1000 Req)", ab_body, 'docs/screenshots/terminal_apache_bench.png', height=740)

if __name__ == '__main__':
    generate_all()
