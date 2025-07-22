# 🚀 fastapi_haproxy_gateway

A lightweight, production-grade gateway setup using **FastAPI**, **HAProxy**, **NGINX**, **Docker Compose**, and **GitHub Actions CI/CD**.

---

## ✨ Features

- ⚡ **FastAPI Microservice** — Simple, high-performance REST API backend.
- 🔁 **HAProxy Load Balancer** — Routes traffic using round-robin strategy.
- 🌐 **NGINX TLS Reverse Proxy** — Secures incoming traffic with HTTPS.
- 📶 **Multiple Replicas** — Scales FastAPI with two replicas behind HAProxy.
- 🧠 **Smart Routing** — HAProxy intelligently balances requests to healthy services.
- 🔒 **HTTPS Support** — Self-signed TLS certificate for secure HTTPS access.
- 🚦 **Rate Limiting** — Limits clients to 5 requests per minute with burst delay instead of hard blocking.
- 📝 **Logging** — Access logs and rate-limit violations stored for audit/debug purposes.
- 📊 **Monitoring Ready** — NGINX access/error logs enabled for observability.
- 🔄 **CI/CD Pipeline** — GitHub Actions workflow builds and pushes Docker image to DockerHub (`dhiraj918106/fastapi_haproxy_gateway`).

---

## 🧪 Usage

- 🔗 Access the app securely via NGINX HTTPS:  
  `https://localhost`

- 💡 If accessing via browser, accept the self-signed certificate warning.

- 🔁 Refresh or send multiple requests to test HAProxy load balancing between FastAPI replicas.

- 🚧 Rate Limit Test:  
  Try sending more than **5 requests/min** — NGINX will delay extra requests instead of rejecting them immediately.

---

## 📦 CI/CD

- 🔧 **CI/CD via GitHub Actions**:
  - Automatically builds the FastAPI Docker image on push.
  - Pushes the image to [DockerHub](https://hub.docker.com/repository/docker/dhiraj918106/fastapi_haproxy_gateway).

---

## 📌 Tech Stack

- 🐍 FastAPI
- 🌐 HAProxy
- 🛡️ NGINX (HTTPS + Rate Limiting)
- 🐳 Docker & Docker Compose
- 🧪 GitHub Actions (CI/CD)
