
## Docker Images 
https://hub.docker.com/r/amazon/aws-lambda-python
https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

### Steps

    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images$ sudo docker build . -t sample1
    
    venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ sudo docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
    bd9a729cb969        sample1             "/lambda-entrypoint.…"   29 seconds ago      Up 26 seconds       0.0.0.0:9000->8080/tcp   wonderful_benz
    

    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ sudo docker exec -it  bd9a729cb969 bash
    bash-4.2# ls
    app.py   
    
    csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
"Hello from AWS Lambda using Python3.8.16 (default, May  8 2023, 09:14:58) \n[GCC 7.3.1 20180712 (Red Hat 7.3.1-15)]!