FROM pytorch/pytorch:latest 
# above gives 6.4 gb image
#FROM python:3.11.4-slim-buster #this gives over 7+ gb image

# update bins
RUN apt-get update && apt-get -y install build-essential curl git \
libexpat1-dev libfreetype6-dev

#add rust
RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# add svm
RUN rustup override set nightly && cargo install svm-rs
# install solc
RUN svm install 0.8.20

RUN pip install onnx ezkl