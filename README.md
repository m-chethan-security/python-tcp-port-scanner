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
