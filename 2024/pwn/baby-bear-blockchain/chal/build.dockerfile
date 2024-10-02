FROM ubuntu:22.04

RUN apt-get update --fix-missing
RUN apt-get install -y \
    gcc libseccomp-dev