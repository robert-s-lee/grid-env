FROM python:3.9.6

# these two lines are mandatory
WORKDIR /gridai/project
COPY . .
