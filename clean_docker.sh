#!/run/current-system/sw/bin/bash

# Stop all running containers
echo "Stopping all running containers..."
docker ps -q | xargs -r docker stop

# Remove all containers
echo "Removing all containers..."
docker ps -aq | xargs -r docker rm

# Remove all images
echo "Removing all images..."
docker images -aq | xargs -r docker rmi -f

# Remove all volumes
echo "Removing all volumes..."
docker volume ls -q | xargs -r docker volume rm

# Remove all user-defined networks
echo "Removing all user-defined networks..."
docker network ls --filter type=custom -q | xargs -r docker network rm

# Remove dangling images
echo "Removing dangling images..."
docker images -f "dangling=true" -q | xargs -r docker rmi

# Prune system to remove unused data
echo "Pruning system..."
docker system prune -af

echo "Docker cleanup complete."

