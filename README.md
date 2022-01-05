# Using Celery with Flask for Cropping Images

This explains how to configure Flask, Celery, RabbitMQ and Redis, together with Docker to build a web service that dynamically generates content and loads this contend when it is ready to be displayed. We'll focus mainly on Celery and the servies that surround it. Docker is a bit more straightforward.


To create and run the container, use:

    docker-compose build
    docker-compose up

To run multiple instances of our Celery consumers, do:

    docker-compose scale worker=N

where N is the desired number of backend worker nodes.

Visit http://localhost:5000 to view our complete application.
