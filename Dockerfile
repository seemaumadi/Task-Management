FROM python:3.8-slim-buster


ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /django

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Create a non-root user and switch to it
RUN useradd -ms /bin/sh appuser
USER appuser

# Copy project files
COPY . .

# Run the Django server
CMD gunicorn taskly.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
