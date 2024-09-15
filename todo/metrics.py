import time
from prometheus_client import Counter, Gauge, Summary, generate_latest, CollectorRegistry

# Define a counter to track HTTP requests
REQUESTS = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint'])

# Define a gauge to track the current time in seconds
CURRENT_TIME = Gauge('current_time_seconds', 'Current time in seconds')

# Define a summary to track request duration
REQUEST_DURATION = Summary('http_request_duration_seconds', 'Duration of HTTP requests in seconds', ['endpoint'])

# Function to increment the request counter
def increment_request_counter(method, endpoint):
    REQUESTS.labels(method=method, endpoint=endpoint).inc()

# Function to set the current time gauge
def set_current_time():
    CURRENT_TIME.set(time.time())
    
def track_http_requests(method, endpoint):
    """
    Increment the counter for HTTP requests.
    """
    REQUESTS.labels(method=method, endpoint=endpoint).inc()
# Function to observe request duration
def observe_request_duration(endpoint, duration):
    REQUEST_DURATION.labels(endpoint=endpoint).observe(duration)

# Function to generate metrics data
def generate_metrics():
    registry = CollectorRegistry()
    return generate_latest(registry)

# Example of updating metrics (to be used in your views or application logic)
def update_metrics(request_method, request_endpoint, request_duration):
    increment_request_counter(request_method, request_endpoint)
    observe_request_duration(request_endpoint, request_duration)
    set_current_time()
