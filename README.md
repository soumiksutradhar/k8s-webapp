# ClusterVitals → Simple Kubernetes Web Application Deployment

## Overview

ClusterVitals is a simple Python web application deployed on a local Kubernetes cluster using **Minikube**.

This project demonstrates core Kubernetes concepts including:-

- Containerized application deployment
- Kubernetes Deployments
- NodePort Services
- Horizontal scaling of pods
- Self-healing containers
- Rolling updates using versioned Docker images

The application container image is hosted on **Docker Hub**, allowing Kubernetes to automatically pull and deploy it.

---

## Tech Stack

- Python (Flask)
- Docker
- Kubernetes (Minikube)
- kubectl
- Docker Hub (Image Registry)

---

## Container Image

The application image is available on Docker Hub:-

```
dopester03/k8s_webapp
```

Available versions:

```
v1
v2
v3
```

Kubernetes automatically pulls the image when the deployment is created.

You can manually verify the image by pulling it:-

```bash
docker pull dopester03/k8s_webapp:v3
```

---

## Prerequisites

Ensure the following tools are installed:-

- Docker
- Minikube
- kubectl

Verify installation:-

```bash
docker --version
kubectl version --client
minikube version
```

---

## Architecture

The application consists of:-

- A containerized Python web application
- A Kubernetes Deployment managing multiple replicas
- A NodePort Service exposing the application externally

Flow:-

```
User → NodePort Service → Deployment → Pods → Container
```

Each pod runs an instance of the web application.

---

## Features Demonstrated

### 1. Containerization

- Created a lightweight Docker image using Python slim base image
- Application exposed on port **5000**
- Image pushed to **Docker Hub**

---

### 2. Kubernetes Deployment

- Defined Deployment manifest with replica configuration
- Applied configuration using `kubectl`
- Kubernetes maintains the desired state automatically

---

### 3. Service Exposure

- Configured a **NodePort Service**
- Enables external access to the application
- Verified routing via browser and curl

---

### 4. Horizontal Scaling

Scale the number of pods:-

```bash
kubectl scale deployment k8s-webapp-deployment --replicas=<n>
```

Example:-

```bash
kubectl scale deployment k8s-webapp-deployment --replicas=5
```

Verify scaling:-

```bash
kubectl get pods
```

---

### 5. Self-Healing

Delete a running pod:-

```bash
kubectl delete pod <pod-name>
```

Kubernetes automatically recreates a new pod to maintain the desired replica count.

---

### 6. Rolling Updates

Update the container image version:-

```bash
kubectl set image deployment/k8s-webapp-deployment k8s-webapp=dopester03/k8s_webapp:v3
```

Monitor rollout status:-

```bash
kubectl rollout status deployment/k8s-webapp-deployment
```

This demonstrates **zero-downtime application updates**.

---

### 7. Web Application

The web interface displays:-

- Application version
- Runtime environment
- Pod hostname

The hostname changes depending on which pod handled the request, demonstrating **load balancing across replicas**.

---

## How to Run

### 1. Start Minikube

```bash
minikube start --driver=docker
```

---

### 2. Clone Repository

```bash
git clone https://github.com/<your-github-username>/ClusterVitals.git
cd ClusterVitals
```

---

### 3. Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify deployment:-

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

---

### 4. Access the Application

```bash
minikube service k8s-webapp-service
```

This command automatically opens the application in your browser.

---

## Key Learnings

- Understanding Kubernetes object hierarchy

```
Deployment → ReplicaSet → Pods
```

- Service-based load balancing
- Container registry integration with Docker Hub
- Debugging common Kubernetes issues:
  - `ImagePullBackOff`
  - networking issues
  - misconfigured services
- Observing Kubernetes reconciliation loop and desired state enforcement

---

## Folder Structure

```
ClusterVitals/
├── Dockerfile
├── README.md
├── app.py
├── deployment.yaml
├── service.yaml
└── requirements.txt
```
