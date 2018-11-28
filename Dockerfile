# Use an official Python runtime as a parent image
FROM python:3.5

ARG BRANCH=master

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in setup.py
# RUN apt-get update && apt-get install -y git
RUN python setup.py install

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "consumer.py"]

ONBUILD RUN pip install git+git://github.com/Mariamjamal32/gwrapper_consumer@${BRANCH}
