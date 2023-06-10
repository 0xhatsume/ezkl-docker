FROM python:3.11.4-slim-buster

# update bins
RUN apt-get update && apt-get -y install build-essential curl git \
libexpat1-dev libfreetype6-dev

#add rust
RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# add ezkl to home
RUN git clone https://github.com/zkonduit/ezkl.git /home/ezkl && \
cd /home/ezkl && pip install -r requirements.txt

# pip install solc-select ?
# build python wheel with maturin 
RUN rustup override set nightly && \
maturin build --release --features python-bindings