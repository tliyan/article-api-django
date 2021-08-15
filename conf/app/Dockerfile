FROM python:3

WORKDIR /code

# Copy Python dependency list
COPY requirements.txt /code/
COPY requirements.dev.txt /code/

# Install Packages 
RUN pip install -r requirements.txt -r requirements.dev.txt