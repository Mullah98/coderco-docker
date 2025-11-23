# Containers + Docker Module

## Overview
This repository documents my journey through the **Docker Module** at *CoderCo Academy*.  
I learned how to create, manage, and orchestrate Docker containers, build multi-stage **Docker images**, work with **Docker Hub** and **AWS ECR**, and manage multi-container applications using **Docker Compose**.

## Skills Learned
- Docker basics: images, containers, Dockerfile, and commands
- Building and running Docker containers locally
- Multi-stage Docker builds for optimized images
- Pushing and pulling Docker images to Docker Hub and AWS ECR
- Container networking and linking services (e.g., Flask + MySQL)
- Orchestrating multi-container applications with Docker Compose
- Debugging containers and using Docker logs

- **[First time with Docker](hello_flask/)**  
  Built a multi-stage Dockerfile for a simple Flask app to understand Dockerfile structure, image optimisation, and container lifecycle management.

## Assignment
- **[Flask + Redis App](my-flask-redis-docker-app/)**  
  I created a fully containerised Flask application that integrates with Redis.  
  **This included**:
  - Writing a clean Dockerfile for the Flask service  
  - Setting up a Redis container  
  - Creating a `docker-compose.yml` to orchestrate both services  
  - Testing interactions between the Flask app and Redis  
  - Understanding service-to-service networking in Docker  
  This project helped me understand real multi-container architectures and how to get services communicating inside a Docker environment.
![Assignment](/my-flask-redis-docker-app/assets/ezgif.com-optimize.gif)

## Notes
- **[Docker Notes:](notes.md)** Notes and commands I made throughout the Docker module for study and revision purposes.