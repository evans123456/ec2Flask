# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
# CMD [ "python", "./myec2.py" ]

CMD ["gunicorn", "-b", "0.0.0.0", "app:app"]

# CMD ["gunicorn", "-b", "0.0.0.0:8000", "myec2"]

# ENTRYPOINT ["./gunicorn.sh"]


#build the docker command
#--> docker build -t flask-container .

#run the flask app locally
#--> docker run -p 5000:5000 flask-container

# docker build -t snow .
# docker run -d snow
# docker images
# sudo docker run -i -t snow:latest
# docker run -i -t 8dbd9e392a96