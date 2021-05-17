# set base image (host OS)
FROM python:3.7-alpine

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
# COPY requirements.txt 
COPY app .

# install dependencies
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8081

CMD [ "python3" , "./main.py"]