# Best practices for docker

1. Avoid running processes in the container as root.

2. Don't bind to a specific UID.

3. Make root the owner of the executable files and prevent these files from being modified.

4. Use multi-stage builds.

5. Using a minimal base image when building a Dockerfile.

6. Use proven base images.

7. Keep your images up to date.

8. Every open port in your container is an open door to your system. Leave only ports open that your applications really need.

9. The order in the Dockerfile instructions is very important.

10. Use linters.
