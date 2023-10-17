# docker_debugpy
A method to debug a python script in a docker container using VsCode

# Mandatory requirements
- Docker
- VSCode
- 10 minutes

# Follow the next steps
1. Open this project folder
![01](images/01.png)

2. Execute:
```docker-compose up --build --force-recreate```
![02](images/02.png)

3. Look that the docker container is up and running
![03](images/03.png)

4. Go to the `debug` section and in the `RUN AND DEBUG` section choose `Remote attach`
![04](images/04.png)

5. Clic on `Debug Anyway`
![05](images/05.png)

6. Continue debugging, by default the script docker_debugpy.py will be debugged:
![06](images/06.png)

7. Continue debugging:
![07](images/07.png)

8. And continue debugging:
![08](images/08.png)

Congrats! You are ready for use this method in your docker projects.