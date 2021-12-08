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

# Set folder for our script.
ENV SCRIPT_PATH /script

# Get markdown2man dependencies.
COPY requirements.txt $SCRIPT_PATH/
RUN pip install --no-cache-dir -r $SCRIPT_PATH/requirements.txt

# Copy markdown2man src.
COPY src/lib/* $SCRIPT_PATH/lib/
COPY src/markdown2man.py $SCRIPT_PATH/
RUN chmod 755 $SCRIPT_PATH/markdown2man.py

# Set markdown2man as this image entrypoint.
ENTRYPOINT ["/script/markdown2man.py"]