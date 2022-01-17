Overview

The final product (time_sharing) is a web application that brings together the people who wants to help each other by
giving various services such as teaching, doing shopping, cooking, pet care, etc. People become a member in the “time
sharing” system and offer their services. For every hour of help they give, they earn an hour’s credit from the system.
They can spend their time credit by receiving an hour of someone else’s time. Everyone’s time is valued equally: one
hour of sharing skills or helping others earns one time credit, whatever the skill or task.

Installation Instructions:

- Create a virtual environment in your directory: RUN $ python3 -m venv env
- Go to the env directory: RUN $ cd env
- Activate the virtual environment: RUN $ source bin/activate
- Install docker and git
- $ git init
- $ git clone https://github.com/alper-turgal/SWE-573.git
- Create an environmet file in the time_sharing_V3 directory named .env
- Copy the the content of .env file in this repo into the .env file you created in your local repo
- $ docker-compose up  (The containers are up and running).
- Go to http://localhost:80 in your development environment to use the app.

