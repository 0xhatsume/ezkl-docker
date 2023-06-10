FROM python:3.11.4-slim-buster

# update bins
RUN apt-get update && apt-get -y install build-essential curl git \
libexpat1-dev libfreetype6-dev

# add pyezkl to home
RUN git clone https://github.com/zkonduit/pyezkl.git /home/pyezkl

# shift bindings etc...