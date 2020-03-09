git pull
docker build -t fastai-v3 . 
docker run --rm -d -p 5000:5000 fastai-v3