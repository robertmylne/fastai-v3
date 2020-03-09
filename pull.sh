git pull
docker build -t fastai-v3 .
docker container stop dog_breeds_ai
docker run --rm -d -p 5000:5000 --name dog_breeds_ai  fastai-v3