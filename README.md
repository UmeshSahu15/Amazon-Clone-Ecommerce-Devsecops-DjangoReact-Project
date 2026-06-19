
<div align="center">

<img width="1536" height="1024" alt="ChatGPT Image Jun 19, 2026, 12_51_00 PM" src="https://github.com/user-attachments/assets/f271bc1b-c5c4-4d51-a348-02ac30061c1c" />

# 🚀 Amazon Clone Ecommerce Inventory Management System

### End-to-End DevSecOps CI/CD Pipeline with Kubernetes, Monitoring & Security Automation

<img src="https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Backend-Django-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Jenkins-CI/CD-red?style=for-the-badge">
<img src="https://img.shields.io/badge/SonarQube-Code%20Quality-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/OWASP-Dependency%20Check-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Trivy-Security-yellow?style=for-the-badge">
<img src="https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Kubernetes-K3s-326CE5?style=for-the-badge">
<img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge">
<img src="https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge">

</div>

---
# 🏗️ Solution Architecture

The following architecture represents the complete end-to-end DevSecOps workflow implemented for the Amazon Clone Ecommerce Inventory Management System.

```text
┌──────────────────────────────────────────────────────────────┐
│                      AMAZON CLONE PROJECT                    │
│              End-to-End DevSecOps CI/CD Pipeline             │
└──────────────────────────────────────────────────────────────┘

                        ┌─────────────────┐
                        │   Developer     │
                        └────────┬────────┘
                                 │
                                 │ Code Push
                                 ▼
                        ┌─────────────────┐
                        │ GitHub Repo     │
                        │ Main Branch     │
                        └────────┬────────┘
                                 │
                                 │ Webhook Trigger
                                 ▼

══════════════════════════════════════════════════════════════════════
                     JENKINS CI/CD SERVER
                        (65.1.253.185)
══════════════════════════════════════════════════════════════════════

                        ┌─────────────────┐
                        │ Jenkins         │
                        │ Pipeline Start  │
                        └────────┬────────┘
                                 │
                                 ▼

                    ┌─────────────────────┐
                    │ Clean Workspace     │
                    └─────────┬───────────┘
                              │
                              ▼

                    ┌─────────────────────┐
                    │ Git Checkout        │
                    └─────────┬───────────┘
                              │
                              ▼

                    ┌─────────────────────┐
                    │ SonarQube Analysis  │
                    └─────────┬───────────┘
                              │
                              ▼

                    ┌─────────────────────┐
                    │ Quality Gate        │
                    └─────────┬───────────┘
                              │
                              ▼

        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼

 ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
 │ npm Audit   │     │ OWASP DC     │     │ Trivy FS    │
 │ Frontend    │     │ Vulnerability│     │ Scan        │
 └──────┬──────┘     └──────┬───────┘     └──────┬──────┘
        │                   │                    │
        └───────────────────┼────────────────────┘
                            │
                            ▼

                  ┌──────────────────────┐
                  │ Security Validation  │
                  └──────────┬───────────┘
                             │
                             ▼

══════════════════════════════════════════════════════════════════════
                         DOCKER STAGE
══════════════════════════════════════════════════════════════════════

                 ┌────────────────────────┐
                 │ Build Backend Image    │
                 │ amazon-backend         │
                 └──────────┬─────────────┘
                            │
                            ▼

                 ┌────────────────────────┐
                 │ Build Frontend Image   │
                 │ amazon-frontend        │
                 └──────────┬─────────────┘
                            │
                            ▼

        ┌───────────────────┼───────────────────┐
        │                                       │
        ▼                                       ▼

┌──────────────────┐                 ┌──────────────────┐
│ Trivy Backend    │                 │ Trivy Frontend   │
│ Image Scan       │                 │ Image Scan       │
└─────────┬────────┘                 └────────┬─────────┘
          │                                   │
          └─────────────────┬─────────────────┘
                            │
                            ▼

                  ┌─────────────────────┐
                  │ Docker Hub Push     │
                  └─────────┬───────────┘
                            │
                            ▼

        6378257556/amazon-backend:latest
        6378257556/amazon-frontend:latest

══════════════════════════════════════════════════════════════════════
                       DEPLOYMENT STAGE
══════════════════════════════════════════════════════════════════════

                            │
                            │ SSH using jenkins-k3s Key
                            ▼

                  ┌──────────────────────┐
                  │ Kubernetes Validation│
                  └──────────┬───────────┘
                             │
                             ▼

                  ┌──────────────────────┐
                  │ Rollout Restart      │
                  │ Backend Deployment   │
                  └──────────┬───────────┘
                             │
                             ▼

                  ┌──────────────────────┐
                  │ Rollout Restart      │
                  │ Frontend Deployment  │
                  └──────────┬───────────┘
                             │
                             ▼

                  ┌──────────────────────┐
                  │ Verify Deployments   │
                  └──────────┬───────────┘
                             │
                             ▼

                  ┌──────────────────────┐
                  │ Verify HPA           │
                  └──────────┬───────────┘
                             │
                             ▼

                  ┌──────────────────────┐
                  │ Smoke Testing        │
                  └──────────┬───────────┘
                             │
                             ▼

══════════════════════════════════════════════════════════════════════
                        K3s KUBERNETES
                          (15.206.14.85)
══════════════════════════════════════════════════════════════════════

                    amazon-clone namespace

        amazon-frontend Deployment
                    │
                    ▼
            Frontend Service
                    │
                    ▼
             NGINX Ingress
                    │
                    ▼
          http://15.206.14.85
                    │
                    ▼
             Amazon Clone UI
                    │
                    ▼
         amazon-backend Deployment
                    │
                    ▼
            Backend Service

══════════════════════════════════════════════════════════════════════
                    AUTO SCALING (HPA)
══════════════════════════════════════════════════════════════════════

amazon-frontend HPA
Min: 1 | Max: 5

amazon-backend HPA
Min: 1 | Max: 5

══════════════════════════════════════════════════════════════════════
                     MONITORING STACK
══════════════════════════════════════════════════════════════════════

Node Exporter
      │
      ▼
kube-state-metrics
      │
      ▼
Prometheus
      │
      ▼
Grafana

Grafana:
http://15.206.14.85/grafana

Prometheus:
http://15.206.14.85:31907

Node Exporter:
http://15.206.14.85:30779/metrics

══════════════════════════════════════════════════════════════════════
                     NOTIFICATION STAGE
══════════════════════════════════════════════════════════════════════

Email Success
Email Failure
Email Unstable
```



## 🎯 Project Objectives

The key objectives of this project are:

* Automate the complete software delivery lifecycle.
* Integrate security into every stage of the CI/CD pipeline.
* Improve deployment reliability and consistency.
* Reduce manual intervention during deployments.
* Enable continuous monitoring and observability.
* Implement scalable container orchestration using Kubernetes.
* Demonstrate real-world DevSecOps practices used in enterprise environments.

---


# 🏗️ Solution Architecture

The project follows a modern DevSecOps architecture where every code change passes through multiple quality, security, deployment, and monitoring stages before reaching the production environment.

The architecture is designed to ensure that only secure, validated, and tested application versions are deployed to Kubernetes.

---

## 📊 Architecture Diagram

![Architecture Diagram](ADD_ARCHITECTURE_DIAGRAM_LINK_HERE)

---

## 🔄 End-to-End Workflow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins CI/CD Pipeline
    │
    ├── Clean Workspace
    │
    ├── Source Code Checkout
    │
    ├── SonarQube Analysis
    │
    ├── Quality Gate Validation
    │
    ├── npm Audit
    │
    ├── OWASP Dependency Check
    │
    ├── Trivy Filesystem Scan
    │
    ├── Docker Image Build
    │
    ├── Trivy Image Scan
    │
    ├── Docker Hub Push
    │
    ▼
K3s Kubernetes Cluster
    │
    ├── Frontend Deployment
    │
    ├── Backend Deployment
    │
    ├── Service Creation
    │
    ├── Ingress Routing
    │
    └── HPA Validation
    │
    ▼
Application Available
    │
    ▼
Prometheus Monitoring
    │
    ▼
Grafana Dashboards
    │
    ▼
Email Notification
```

---

## 🏢 Infrastructure Components

### GitHub

GitHub serves as the central source code repository. Developers push code changes to GitHub, which automatically triggers the Jenkins pipeline using GitHub Webhooks.

### Jenkins

Jenkins acts as the CI/CD orchestrator responsible for:

* Source Code Checkout
* Security Validation
* Docker Build Automation
* Deployment Automation
* Notification Management

### SonarQube

SonarQube performs static code analysis and evaluates:

* Bugs
* Vulnerabilities
* Security Hotspots
* Code Smells
* Maintainability Issues

### OWASP Dependency Check

OWASP Dependency Check performs Software Composition Analysis (SCA) to identify vulnerable third-party dependencies used within the application.

### Trivy

Trivy scans both the source code filesystem and Docker images for:

* Known Vulnerabilities
* Secrets
* Misconfigurations
* Package Security Issues

### Docker

Docker packages the frontend and backend applications into lightweight and portable containers that can be deployed consistently across environments.

### Docker Hub

Docker Hub acts as the container registry used to store and distribute application images.

### K3s Kubernetes

K3s is used as the orchestration platform responsible for:

* Container Scheduling
* High Availability
* Scaling
* Self-Healing
* Rolling Updates

### NGINX Ingress Controller

NGINX Ingress Controller manages incoming traffic and routes requests to the appropriate backend services.

### Prometheus

Prometheus continuously collects infrastructure and application metrics.

### Grafana

Grafana provides centralized dashboards for visualizing system health, resource utilization, and application performance.

---

## 🎯 Security Flow

The project follows a Shift-Left Security approach.

```text
Code Commit
    ↓
SonarQube Analysis
    ↓
npm Audit
    ↓
OWASP Dependency Check
    ↓
Trivy Filesystem Scan
    ↓
Docker Build
    ↓
Trivy Image Scan
    ↓
Deployment
```

This ensures that security vulnerabilities are identified and addressed before reaching production.


# 🏆 Project Highlights

This project demonstrates the implementation of a complete **Enterprise DevSecOps CI/CD Pipeline** for a React and Django based Ecommerce Inventory Management Application.

### Implemented Features

✅ GitHub Webhook Integration

✅ Jenkins CI/CD Automation

✅ SonarQube Static Code Analysis

✅ Quality Gate Validation

✅ npm Audit Security Checks

✅ OWASP Dependency Check

✅ Trivy Filesystem Scanning

✅ Trivy Docker Image Scanning

✅ Docker Image Build & Push

✅ Docker Hub Integration

✅ K3s Kubernetes Deployment

✅ NGINX Ingress Controller

✅ Horizontal Pod Autoscaler (HPA)

✅ Prometheus Monitoring

✅ Grafana Dashboard

✅ Node Exporter Metrics

✅ Automated Smoke Testing

✅ HTML Email Notifications

---

# 💼 Resume Highlights

### DevSecOps Engineer Project

* Designed and implemented an end-to-end DevSecOps CI/CD pipeline using Jenkins, SonarQube, OWASP Dependency Check, Trivy, Docker, Kubernetes, Prometheus, and Grafana.
* Automated code quality analysis, security scanning, container image creation, Docker Hub publishing, Kubernetes deployment, and deployment verification.
* Deployed React and Django applications on a K3s Kubernetes cluster using NGINX Ingress Controller.
* Configured Horizontal Pod Autoscaling (HPA) for automatic workload scaling.
* Implemented monitoring and observability using Prometheus, Grafana, Node Exporter, and kube-state-metrics.
* Integrated automated email notifications for build success and failure reporting.
* Applied DevSecOps best practices by shifting security left in the CI/CD pipeline.

---

# 🎯 Skills Demonstrated

### Cloud & Infrastructure

* AWS EC2
* Linux Administration
* Networking
* Security Groups

### CI/CD & DevSecOps

* GitHub
* Jenkins
* SonarQube
* OWASP Dependency Check
* Trivy
* DevSecOps

### Containerization & Orchestration

* Docker
* Docker Hub
* Kubernetes (K3s)
* NGINX Ingress Controller
* HPA

### Monitoring

* Prometheus
* Grafana
* Node Exporter
* kube-state-metrics

### Development

* React.js
* Django
* REST APIs
* JWT Authentication

---

# 🚀 Future Enhancements

* Deploy on AWS EKS
* Use AWS RDS instead of SQLite
* Configure HTTPS using Let's Encrypt
* Implement Slack Notifications
* Configure Kubernetes Alert Manager
* Add GitOps using ArgoCD
* Multi-Environment Deployments (Dev, QA, Prod)

---

# 👨‍💻 Author

### Umesh Sahu

**Cloud & DevOps Engineer**

📧 Email: umeshkumar637825@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/sahu-umesh/

🐙 GitHub: https://github.com/UmeshSahu15

---

<div align="center">

### ⭐ If you found this project useful, please consider giving it a star.

### 🚀 Happy Learning & Happy DevOps!

</div>


