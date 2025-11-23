# **Docker + Containers**

---

## Containers
### What are containers?
- Lightweight, portable units for running an application.
- Bundles the app, runtime, libraries, and all dependancies.
- "But it works on my machine?" - Containers help solve this.

### Why does it matter?
- Consistent behaviour across development, testing, and production.
- Apps are isolated, so one container doesn't affect another.
- More efficient that virtual machines because they *share* the host OS.

### Containers Architecture:
- **Infrastructure:** Physical/virtual hardware (your machine).
- **Host OS:** The operating system running on the hardware.
- **Docker Engine:** Builds, runs, and manages containers.
- **Containers:** Each container contains an app and its required binaries/libraries.

### Key benefits:
- **Isolation:** Each container has it's own environment, prevents conflicts.
- **Consistency:** App behaves the same across all environments, carries everything needed to run.
- **Efficiency:** Share the host OS kernel and Docker engine, faster startups.

Containers are like *shipping containers* -> Everything the app needs is inside, easy to move across environments.

---


## Docker
### Purpose:
- Simplifies container management and deployment.
- Open platform for building, shipping, and running applications inside containers.

### Why Docker Matters:
- **Simplified Deployment:** 
    - App runs the same locally and in production.
    - Removes environment issues.

- **Efficiency:**
    - Lightweight and fast (shares host kernel).
    - Great for quick testing and scaling.

- **Collaboration:**
    - Everyone uses the same environment.
    - Faster onboarding.

- **CI/CD:**
    - Works smoothly with automated pipelines.
    - Build → test → deploy becomes consistent.

### Core components:
- **Docker Engine:** Main service that runs and manages containers. 
- **Docker Hub:** Online repository for container images.
- **Docker Compose:** Defines and runs multi-container applications.

---

## Images & Containers
### Docker Images
- Blueprints/templates for containers.
- Immutable → you rebuild them to update.
- Ensure consistent environments.

### Docker Containers
- Running instances of images.
- What actually execute your application.
- You can start/stop, and interact with them.

### Dockerfile
- File that defines how to build a *Docker Image*.
- Contains step-by-step instructions.
- *Docker* reads the *Dockerfile* to assemble the final image.

---

## VM vs Containers

| Topic | Virtual Machines (VMs) | Containers |
|-------|--------------------------|-------------|
| **Isolation** | Full OS isolation (stronger) | Process-level isolation (lighter) |
| **OS Requirements** | Each VM runs its own full OS | Share host OS kernel |
| **Performance** | Heavier, slower startup | Lightweight, fast startup |
| **Resource Usage** | High (RAM + CPU overhead) | Low (only app + dependencies) |
| **Portability** | Less portable (depends on guest OS) | Highly portable across environments |
| **Use Cases** | Running multiple different OSes or legacy systems | Microservices, distributed systems, scalable apps |
| **Boot Time** | Seconds to minutes | Milliseconds |
| **Image Size** | Large (GBs) | Small (MBs) |

*VMs = strong isolation. heavier*
*Containers = lighter, faster, portable*

---

## Basic Docker workflow:
- **Build Image**
```
docker build -t hello-flask .
```

- **Run Container**
```
docker run -d -p 5002:5002 --name hello-flask hello-flask
```

- **Useful Commands**
```
docker ps          # list running containers
docker stop <id>   # stop a container
docker rm <id>     # remove container
docker images      # list images
docker rmi <id>    # remove image
docker system prune  # clean unused resources
```

---

## Docker Networking
- **Bridge** -> Default private network between containers.
- **Host** -> Container uses host network directly.
- **None** -> No networking.

---

## Docker Compose
- **Purpose**:
Run multi-container apps easily.

- **Why is it useful:**
- One command to start full stack apps.
- Consistent environments for teams.
- Easy onboarding.

- **Compose File:**
- Uses a `docker-compose.yml` file to define services, networks, and volumes.

- **Key Commands**
```
docker-compose up
docker-compose up -d
docker-compose down
docker-compose logs -f
docker compose down -v   # removes volumes too
```

---

## Docker Registries
- Store and share images (Docker Hub, AWS ECR).
- Used for deployments across environments.

- **Flow**
1. Build
2. Test
3. Push
4. Pull in production