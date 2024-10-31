# Script for creating base training service image
#
# GENERATED DOCKERFILE - please ***DO*** modify.
#
# Generated from: templates/general-docker/training.docker.file.vm

ARG DOCKER_BASELINE_REPO_ID
ARG VERSION_AISSEMBLE

# Start build stage based on aiSSEMBLE extension of Nvidia base image
FROM ${DOCKER_BASELINE_REPO_ID}boozallen/aissemble-nvidia:${VERSION_AISSEMBLE}

ENV GIT_PYTHON_REFRESH=quiet
ENV DEBIAN_FRONTEND=noninteractive
ENV ENABLE_LINEAGE=true

RUN apt-get -y update \
    && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && add-apt-repository ppa:deadsnakes/ppa

# Install Python 3.11 and related packages, and perform cleanup
RUN apt-get -y update \
    && apt install python3.11 python3.11-distutils gcc python3.11-dev curl -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Ensure that any needed Krausening properties are copied and KRAUSENING_BASE environment variable is set!
ENV KRAUSENING_BASE /app/config
COPY target/krausening/base/ /app/config/
COPY src/main/resources/krausening/base/ /app/config/

# Install logistic-training dependencies
COPY target/logistic-training/dist/requirements.txt /installation/logistic-training/
RUN python3.11 -m pip install --ignore-installed -r /installation/logistic-training/requirements.txt

# Install logistic-training
COPY target/logistic-training/dist /modules/logistic-training
RUN set -e && \
    cd /modules/logistic-training; for x in *.whl; do pip install $x --no-cache-dir --no-deps; done

CMD python3.11 -m logistic_training.classification_training_driver
