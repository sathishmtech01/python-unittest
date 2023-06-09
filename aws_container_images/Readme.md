
## Docker Images 
https://hub.docker.com/r/amazon/aws-lambda-python
https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

### Steps

    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images/aws_container_images_v1$ sudo docker build . -t sample2
    [sudo] password for csk:
    Sending build context to Docker daemon  6.656kB
    Step 1/5 : FROM public.ecr.aws/lambda/python:3.8
    ---> 6c2fe061ee7f
    Step 2/5 : COPY requirements.txt  .
    ---> Using cache
    ---> 00689db20a76
    Step 3/5 : RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
    ---> Using cache
    ---> 1a98adcc5b86
    Step 4/5 : COPY src ${LAMBDA_TASK_ROOT}
    ---> b4c8e2e9984c
    Step 5/5 : CMD [ "app.handler" ]
    ---> Running in b592f23fccca
    Removing intermediate container b592f23fccca
    ---> 64fc206483c0
    Successfully built 64fc206483c0
    Successfully tagged sample2:latest
    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images/aws_container_images_v1$ sudo docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
    bd9a729cb969        sample1             "/lambda-entrypoint.…"   14 minutes ago      Up 14 minutes       0.0.0.0:9000->8080/tcp   wonderful_benz
    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images/aws_container_images_v1$ sudo docker run -p 9000:8080 sample2
    docker: Error response from daemon: driver failed programming external connectivity on endpoint cranky_ramanujan (dd1b9d3c468886948147cfe185c154f8ef324207cf84b377fc8a0114ba9c5007): Bind for 0.0.0.0:9000 failed: port is already allocated.
    ERRO[0001] error waiting for container: context canceled
    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images/aws_container_images_v1$ sudo docker run -p 9001:8080 sample2
    09 Jun 2023 09:44:13,837 [INFO] (rapid) exec '/var/runtime/bootstrap' (cwd=/var/task, handler=)
    09 Jun 2023 09:45:02,988 [INFO] (rapid) extensionsDisabledByLayer(/opt/disable-extensions-jwigqn8j) -> stat /opt/disable-extensions-jwigqn8j: no such file or directory
    09 Jun 2023 09:45:02,989 [INFO] (rapid) Configuring and starting Operator Domain
    09 Jun 2023 09:45:02,989 [INFO] (rapid) Starting runtime domain
    09 Jun 2023 09:45:02,989 [WARNING] (rapid) Cannot list external agents error=open /opt/extensions: no such file or directory
    09 Jun 2023 09:45:02,989 [INFO] (rapid) Starting runtime without AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN , Expected?: false
    START RequestId: e811b9c6-9366-45ac-ae09-fc9937d4380e Version: $LATEST
    END RequestId: 327f1d9a-fb25-4572-a387-f8fdad0700fe
    REPORT RequestId: 327f1d9a-fb25-4572-a387-f8fdad0700fe  Init Duration: 0.19 ms  Duration: 113.86 ms     Billed Duration: 114 ms Memory Size: 3008 MB    Max Memory Used: 3008 MB
    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
    {"output": "hello"}


### Error scenario
    venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest/aws_container_images/aws_container_images_v3$ sudo docker run -p 9001:8080 sample4
    09 Jun 2023 09:58:16,623 [INFO] (rapid) exec '/var/runtime/bootstrap' (cwd=/var/task, handler=)
    09 Jun 2023 09:58:25,483 [INFO] (rapid) extensionsDisabledByLayer(/opt/disable-extensions-jwigqn8j) -> stat /opt/disable-extensions-jwigqn8j: no such file or directory
    START RequestId: 225bdba9-2460-4912-8951-db511aec09c0 Version: $LATEST
    09 Jun 2023 09:58:25,483 [INFO] (rapid) Configuring and starting Operator Domain
    09 Jun 2023 09:58:25,483 [INFO] (rapid) Starting runtime domain
    09 Jun 2023 09:58:25,483 [WARNING] (rapid) Cannot list external agents error=open /opt/extensions: no such file or directory
    09 Jun 2023 09:58:25,483 [INFO] (rapid) Starting runtime without AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN , Expected?: false
    Traceback (most recent call last): Unable to import module 'lambda_function.app': No module named 'lambda_function'
    END RequestId: 8a90e77a-35f6-4e5d-aa64-e1813693dfea
    REPORT RequestId: 8a90e77a-35f6-4e5d-aa64-e1813693dfea  Init Duration: 0.13 ms  Duration: 75.28 ms      Billed Duration: 76 ms  Memory Size: 3008 MB    Max Memory Used: 3008 MB

    csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'
    {"errorMessage": "Unable to import module 'lambda_function.app': No module named 'lambda_function'", "errorType": "Runtime.ImportModuleError", "stackTrace": []}

    csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ sudo docker ps
    [sudo] password for csk:
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
    8a8df668b374        sample4             "/lambda-entrypoint.…"   2 minutes ago       Up 2 minutes        0.0.0.0:9001->8080/tcp   blissful_saha
    bd9a729cb969        sample1             "/lambda-entrypoint.…"   32 minutes ago      Up 32 minutes       0.0.0.0:9000->8080/tcp   wonderful_benz
    (venv) csk@csk-ai-revolution:~/IdeaProjects/python-unittest$ sudo docker exec -it 8a8df668b374 bash
    bash-4.2# ls
    lambda_function  requirements.txt
    bash-4.2# cd lambda_function/
    bash-4.2# ls
    app.py
