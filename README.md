
<div align="center">


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
<img width="1536" height="1024" alt="ChatGPT Image Jun 19, 2026, 12_51_00 PM" src="https://github.com/user-attachments/assets/f271bc1b-c5c4-4d51-a348-02ac30061c1c" />

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

# 🛠️ Tools & Technologies Demonstration

This project integrates multiple DevSecOps, Security, Containerization, Orchestration, and Monitoring tools to automate the complete Software Development Lifecycle (SDLC).

---

# ☁️ AWS EC2

### Purpose

AWS EC2 instances were used to host:

* Jenkins Server
* SonarQube
* K3s Kubernetes Cluster
* Monitoring Stack

### Screenshot

<Img width="1920" height="1080" alt="2026-06-19 (1)" src="https://github.com/user-attachments/assets/8032b6b1-ec4a-44b7-88eb-c4e24de10f42" />


---

# 🐙 GitHub

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="80"/>

### Purpose

GitHub was used as the source code repository.

### Features Used

* Source Code Management
* GitHub Webhooks
* Branch Management

### Screenshot
### Screenshot
<img width="1920" height="1080" alt="2026-06-19 (4)" src="https://github.com/user-attachments/assets/647a69a0-f595-4c1f-ab15-867ed8557d92" />

![Screenshot](https://raw.githubusercontent.com/UmeshSahu15/Amazon-Clone-Ecommerce-Devsecops-DjangoReact-Project/main/Project_Screenshot/2026-06-19%20(1).png)
---

# 🔄 Jenkins

<img src="https://www.jenkins.io/images/logos/jenkins/jenkins.svg" width="90"/>

### Purpose

Jenkins automates the complete CI/CD workflow.

### Pipeline Stages

* Checkout
* SonarQube Analysis
* Security Scanning
* Docker Build
* Docker Hub Push
* Kubernetes Deployment

### Screenshot

![Jenkins Pipeline](images/jenkins-pipeline.png)

---

# 🔍 SonarQube

<img src="https://www.svgrepo.com/show/354365/sonarqube.svg" width="90"/>

### Purpose

Performs Static Application Security Testing (SAST).

### Analysis Includes

* Bugs
* Vulnerabilities
* Security Hotspots
* Code Smells
* Quality Gates

### Screenshot

![SonarQube Dashboard](images/sonarqube-dashboard.png)

---

# 📦 NPM Audit

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" width="100"/>

### Purpose

Scans frontend dependencies for known vulnerabilities.

### Validation

* Critical Vulnerabilities
* High Vulnerabilities
* Dependency Issues

### Screenshot

![NPM Audit](images/npm-audit.png)

---

# 🛡️ OWASP Dependency Check

<img src="https://owasp.org/assets/images/logo.png" width="90"/>

### Purpose

Performs Software Composition Analysis (SCA).

### Detects

* Vulnerable Dependencies
* Known CVEs
* Security Risks

### Screenshot

![OWASP Report](images/owasp-report.png)

---

# 🔒 Trivy

<img src="https://trivy.dev/v0.40/imgs/logo.png" width="120"/>

### Purpose

Performs vulnerability scanning.

### Scans

* Filesystem
* Docker Images
* Misconfigurations
* Secrets

### Screenshot

![Trivy Scan](images/trivy-report.png)

---

# 🐳 Docker

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="90"/>

### Purpose

Containerizes frontend and backend applications.

### Docker Images

```text
amazon-backend

amazon-frontend
```

### Screenshot

![Docker Build](images/docker-build.png)

---

# 📦 Docker Hub

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="90"/>

### Purpose

Stores Docker images.

### Published Images

```text
6378257556/amazon-backend:latest

6378257556/amazon-frontend:latest
```

### Screenshot

![Docker Hub](images/dockerhub-images.png)

---

# ☸️ K3s Kubernetes

<img src="https://raw.githubusercontent.com/k3s-io/k3s/master/docs/static/logo.png" width="90"/>

### Purpose

Hosts the production workloads.

### Features Used

* Deployments
* Services
* Ingress
* HPA

### Screenshot

![Kubernetes](images/kubernetes-cluster.png)

---

# 🌐 NGINX Ingress Controller

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" width="90"/>

### Purpose

Routes external traffic to frontend and backend services.

### Screenshot

![Ingress](images/nginx-ingress.png)

---

# 📈 Horizontal Pod Autoscaler (HPA)

### Purpose

Automatically scales application pods.

### Configuration

```text
Frontend:
Min: 1
Max: 5

Backend:
Min: 1
Max: 5
```

### Screenshot

![HPA](images/hpa-status.png)

---

# 📊 Prometheus

<img src="https://prometheus.io/assets/prometheus_logo_grey.svg" width="90"/>

### Purpose

Collects Kubernetes and infrastructure metrics.

### Screenshot

![Prometheus](images/prometheus-dashboard.png)

---

# 📉 Grafana

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/grafana/grafana-original.svg" width="90"/>

### Purpose

Visualizes monitoring metrics.

### Dashboard Includes

* CPU Usage
* Memory Usage
* Disk Usage
* Network Usage
* Kubernetes Metrics

### Screenshot

![Grafana Dashboard](images/grafana-dashboard.png)

---

# 📧 Email Notifications

### Purpose

Automatically sends pipeline execution status.

### Notification Types

* Success
* Failure
* Unstable

### Screenshot

![Email Notification](images/email-notification.png)

---

# 🌐 Running Application

### Purpose

Final production deployment running on K3s Kubernetes.

### Application URL

```text
http://15.206.14.85
```

### Screenshot

![Amazon Clone Application](images/application-dashboard.png)

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


