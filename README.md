# Python TCP Port Scanner

A basic TCP port scanner built with Python's `socket` module to understand how TCP connect scanning works at a fundamental level.

This project was developed as part of my cybersecurity and network security learning journey.

## Objective

The goal of this project was to understand how a simple TCP port scanner works internally and compare its results with Nmap's TCP connect scan (`-sT`).

## How It Works

The scanner:

1. Creates a TCP socket using Python's `socket` module.
2. Iterates through ports 1–1024.
3. Attempts to establish a TCP connection using `socket.connect()`.
4. Uses a timeout to avoid waiting indefinitely.
5. Reports a port as open when the connection succeeds.
6. Closes the socket after each connection attempt.

## Code

```python
import socket

target = "LAB_IP"

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print(f"{port}/tcp OPEN")
    except socket.error:
        pass
    finally:
        s.close()
```

Testing Environment
Operating System: Kali Linux
Target: Intentionally vulnerable lab VM
Scanner: Python socket
Comparison tool: Nmap
Scan type: TCP Connect Scan (-sT)
Port range: 1–1024
Results

The Python scanner identified the following open TCP ports within the 1–1024 range:

21
22
23
25
53
80
111
139
445
512
513
514

Nmap's -sT scan identified the same open ports within this range and additionally provided service identification.

Python Scanner vs Nmap

The Python implementation helped me understand the basic mechanism behind a TCP connect scan.

The Python scanner determines whether a port is reachable by attempting to establish a TCP connection.

Nmap builds on this concept and provides considerably more functionality, including service identification and many other scanning techniques.

Python scanner

Nmap scan

Key Learnings
Understanding Python's socket module
Creating TCP sockets
Understanding socket.connect()
TCP port states at a basic level
Handling connection timeouts
Exception handling in network programs
Understanding the basic idea behind TCP connect scanning
Comparing a custom implementation with Nmap
Limitations

This is a learning project and is intentionally simple.

It does not currently include:

Multithreading
Service/version detection
OS detection
UDP scanning
Advanced error handling
Stealth scanning techniques
Future Improvements

Possible improvements include:

Multithreaded scanning
Command-line arguments
Custom port ranges
Better error handling
Service detection
Output formatting
Logging scan results
Ethical Use

This tool was developed and tested in an isolated lab environment.

Only scan systems that you own or have explicit permission to test.

Author

Chethan M

B.Tech Computer Science & Engineering — Cyber Security
