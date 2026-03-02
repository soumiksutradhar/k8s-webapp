# ClusterVitals -> simple Kubernetes web application deployment

## Overview

This project demonstrates containerization and deployment of a Python web application on a local Kubernetes cluster using Minikube.  

The objective was to understand core Kubernetes concepts including Deployments, Services, scaling, self-healing and rolling updates.

---

## Tech Stack

- Python(Flask framework)
- Docker
- Kubernetes(Minikube)
- kubectl
- Docker Hub(Image Registry)

---

## Architecture

The application consists of:-

- A containerized Python web app
- A Kubernetes Deployment managing multiple replicas
- A NodePort Service exposing the application externally

Flow:

User → NodePort Service → Pods(ReplicaSet managed) → Container

---

## Features Demonstrated

### 1. Containerization
- Created a lightweight Docker image using Python slim base image
- Exposed application on port 5000
- Pushed image to Docker Hub

### 2. Kubernetes Deployment
- Defined Deployment manifest with replica configuration
- Applied configuration using `kubectl`
- Verified desired vs actual state reconciliation

### 3. Service Exposure
- Configured NodePort Service
- Enabled external access to the application
- Verified service routing using curl and browser

### 4. Horizontal Scaling
- Scaled replicas using:-
```bash
kubectl scale deployment k8s-webapp-deployment --replicas=<n>
```
- Here, n is the number of replica pods you require

### 5. Webpage
- Displays application version and runtime environment
- Detects Kubernetes runtime environment via environment variables
- Shows pod hostname to demonstrate load balancing

---

## How to Run

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Build Docker Image
```bash
docker build -t <dockerhub-username>/k8s_webapp:v1 .
```

### 3. Deploy to Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 4. Access Application
```bash
minikube service k8s-webapp-service
```

---

## Key Learnings

- Understanding Kubernetes object hierarchy(Deployment → ReplicaSet → Pods)
- Service-based load balancing
- Importance of correct image tagging and registry access
- Debugging ImagePullBackOff and networking issues
- Observing reconciliation loop and desired state enforcement


---

## Folder Structure

```
k8s_webapp/
├── Dockerfile
├── README.md
├── app.py
├── deployment.yaml
├── requirements.txt
└── service.yaml
```
