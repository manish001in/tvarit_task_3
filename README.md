Tvarit Assignment Task 3

Problem Statement: 
Dockerize the application is Task 2

Assuming that docker has been previously installed in user's system.
I have created a dockerfile that should take care of the creating an image which can be run by the user.

The following commands can be used.
For creating the image: "sudo docker build -t tvarit_img1 ."  , to be run in the directory where Dockerfile is present
For running the image in a container: "sudo docker run -p 5000:5000 tvarit_img1" , can be run anywhere.

After running the image, the server will be ready to accept requests at url: 127.0.0.1:5000 or 0.0.0.0:5000

