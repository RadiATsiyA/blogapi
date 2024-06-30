# Pull base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /blogapi

# Install dependencies
COPY requirements.txt /blogapi/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /blogapi/