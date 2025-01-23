FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Export DEBIAN_FRONTEND to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python 
RUN apt-get update \ 
    && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch to vscode user (default in devcontainer images)
# USER vscode