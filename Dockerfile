# Based on Alpine, python image has the minimun footprint to run python apps.
FROM python:3.8

# Image metadata.
LABEL maintainer="dante-signal31 (dante.signal31@gmail.com)"
LABEL description="Image to run markdown2man GitHub Action."
LABEL homepage="https://github.com/dante-signal31/markdown2man"

# Abort on error.
RUN set -e

# Install Pandoc.
RUN apt-get update \
    && apt-get install pandoc -y

# Get markdown2man dependencies.
#WORKDIR /usr/src/markdown2man
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Set folder for our script.
ENV SCRIPT_PATH /script
# Update PYTHONPATH to find out lib.
ENV PYTHONPATH "${PYTHONPATH}:${SCRIPT_PATH}/"

# Copy markdown2man src.
COPY src/* $SCRIPT_PATH/
RUN chmod 755 $SCRIPT_PATH/markdown2man.py

# Set markdown2man as this image entrypoint.
ENTRYPOINT ["/script/markdown2man.py"]