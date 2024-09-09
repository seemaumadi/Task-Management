# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install build dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . /app/

# Run database migrations
RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



