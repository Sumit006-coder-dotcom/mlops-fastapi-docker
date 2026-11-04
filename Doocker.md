Interview Questions
Q1. What is Docker?

Docker is a containerization platform used to package and run applications with their dependencies in isolated environments.

Q2. What is a Docker image?

A Docker image is a read-only template used to create containers.

Q3. What is a Docker container?

A Docker container is an isolated running instance of a Docker image.

Q4. What is a Dockerfile?

A Dockerfile is a text file containing instructions to build a Docker image.

Q5. Why is Docker important in MLOps?

Docker ensures consistent environments, simplifies ML model deployment, and improves application portability.

Q6. What is Docker Hub?

Docker Hub is a cloud-based registry used to store and distribute Docker images.

Q1. What is a Docker image?

A Docker image is a read-only template used to create containers.

Q2. What is a Docker container?

A Docker container is an isolated instance of a Docker image.

Q3. What is the difference between docker run and docker start?

docker run creates and starts a new container, whereas docker start starts an existing stopped container.

Q4. What is detached mode?

Detached mode runs a container in the background without attaching its output to the terminal.

Q5. What is Docker Hub?

Docker Hub is a registry used to store and distribute Docker images.

Q1. What is Docker build?

Docker build creates a Docker image using instructions defined in a Dockerfile.

Q2. What is Docker build context?

Build context is the set of files and directories available to Docker during image building.

Q3. What is port mapping?

Port mapping connects a host machine port to a container port.

Q4. What does -d mean?

It runs a container in detached mode.

Q5. What is an image tag?

An image tag identifies a particular version of a Docker image.

Q1. What is a Docker Volume?
A Docker Volume is a persistent storage mechanism used to preserve data outside a container's writable layer.

Q2. What is the difference between a volume and a bind mount?
A volume is managed by Docker, whereas a bind mount directly maps a host filesystem path into a container.

Q3. Why are volumes useful in ML applications?
They help preserve datasets, model files, logs, and other application data across container restarts and removals.

Q1. What is Docker Compose?
Docker Compose is a tool for defining and running multi-container applications using a YAML configuration file.

Q2. What is docker-compose.yml?
It is a YAML file that defines services, images, ports, volumes, and other container configurations.

Q3. What is the difference between docker compose up and docker compose down?
up creates and starts services, while down stops and removes the containers and networks created by Compose.

Q1. Why do we use Docker for ML deployment?
Docker packages an ML application with its dependencies into a portable container.

Q2. What is the purpose of EXPOSE 8000?
It documents the port on which the application listens inside the container.

Q3. Why use 0.0.0.0 instead of 127.0.0.1 inside Docker?
It allows the application to accept connections from outside the container.

Q4. What is the difference between an image and a container?
An image is a packaged template, while a container is a running instance of that image.

Q5. What is containerization?
Containerization packages an application and its dependencies into an isolated, portable environment.