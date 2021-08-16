FROM python:3

ARG ENV
ENV ENV ${ENV}

WORKDIR /code

# Copy Python dependency list
COPY conf/app/requirements.base.txt /code/
COPY conf/app/requirements.dev.txt /code/

# Install Packages 
RUN pip install -r requirements.${ENV}.txt