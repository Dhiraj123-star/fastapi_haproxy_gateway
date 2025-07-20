
# 🚀 fastapi_haproxy_gateway

A lightweight, production-style gateway setup using **FastAPI**, **HAProxy**, **NGINX**, and **Docker Compose**.

---

## ✨ Features

- ⚡ **FastAPI Microservice** — Simple, high-performance REST API backend.
- 🔁 **HAProxy Load Balancer** — Routes traffic using round-robin strategy.
- 🌐 **NGINX TLS Reverse Proxy** — Secures incoming traffic with HTTPS.
- 📶 **Multiple Replicas** — Scales FastAPI with two replicas behind HAProxy.
- 🧠 **Smart Routing** — HAProxy intelligently balances requests to healthy services.
- 🔒 **HTTPS Support** — Self-signed TLS certificate for secure HTTPS access.
- 🚦 **Rate Limiting** — Limits clients to 5 requests per minute with burst delay.
- 📝 **Logging** — Access logs and rate-limit violations stored for audit/debug.
- 📊 **Monitoring Ready** — NGINX access/error logs enabled for analysis.

---

## 🧪 Usage

- 🔗 Access the app securely via NGINX HTTPS:  
  `https://localhost:8443`

- 💡 If accessing via browser, accept the self-signed certificate warning.

- 🔁 Refresh the page or make multiple requests to test load balancing across FastAPI replicas.

- 🚧 Rate Limit Test:  
  Try sending more than **5 requests/min** to trigger rate limiting with burst delay (delays instead of blocking).

---

## 📌 Tech Stack

- 🐍 FastAPI
- 🌐 HAProxy
- 🛡️ NGINX (HTTPS + Rate Limiting)
- 🐳 Docker & Docker Compose

---
