aws ecr get-login-password --region AWS_REGION | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com
if [[ $(docker ps -a | awk 'NR > 1{print $NF}') == "CONTAINER_NAME" ]]; then 
        docker stop CONTAINER_NAME
        echo "container was stoped"
        docker rm CONTAINER_NAME
        echo "container was deleted"
        docker ps -a 
fi
if [[ $(docker images | awk 'NR > 1 {print $2}') == "main-latest" ]]; then 
                docker images | awk 'NR > 1{print $3}' | xargs docker rmi
                echo "the image was deleted"
                docker images
fi      

echo "pulling the new container"
docker pull AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/ECR_REPOSITORY:main-latest
docker images
docker run -d --name CONTAINER_NAME AWS_ACCOUTN_ID.dkr.ecr.AWS_REGION.amazonaws.com/ECR_REPOSITORY:main-latest
echo "running the new container
