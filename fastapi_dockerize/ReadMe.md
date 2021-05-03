```docker
docker build -t fastapi:0.1 .

docker run -d --name api -p 8081:8081 fastapi:0.1
```

no go to the localhost:8081/docs

```
docker save -o fastapi:0.1.tar fastapi:0.1

docker load -i fastapi:0.1.tar

```