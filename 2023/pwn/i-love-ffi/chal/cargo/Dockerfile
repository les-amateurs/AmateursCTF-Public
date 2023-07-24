FROM buildpack-deps@sha256:8f28bd087741849791b564aea220968c88f2cace4063336681cd238858e05a79

RUN wget https://static.rust-lang.org/dist/rust-1.70.0-x86_64-unknown-linux-gnu.tar.gz && \
    tar -xf /rust-1.70.0-x86_64-unknown-linux-gnu.tar.gz
RUN cd /rust-1.70.0-x86_64-unknown-linux-gnu && ./install.sh