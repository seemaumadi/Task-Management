FROM alpine:3.20

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /django

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy project files
COPY . .

# Run the Django server
CMD gunicorn taskly.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000