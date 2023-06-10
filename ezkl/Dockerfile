FROM ghcr.io/foundry-rs/foundry:latest 
# foundry for the solc

# update bins
RUN apk add --no-cache gmp-dev g++ gcc curl curl-dev expat freetype-dev fontconfig ttf-dejavu

# add rust
RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# add ezkl to home
RUN git clone https://github.com/zkonduit/ezkl.git /home/ezkl && \
cd /home/ezkl && rustup override set nightly && cargo install --force --path .
# cd /home/ezkl && rustup override set nightly && cargo build \
# --release --features render --bin ezkl
ENV PATH="/home/ezkl/target/release:${PATH}"