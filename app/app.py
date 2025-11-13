from flask import Flask, Response
import psutil
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Observability Stack!"

@app.route('/metrics')
def metrics():
    # Get real CPU and memory usage
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    
    # Add some randomness to simulate load
    response_time = random.uniform(0.1, 0.5)
    
    # Prometheus format metrics
    metrics_data = f"""# HELP app_cpu_usage CPU usage percentage
# TYPE app_cpu_usage gauge
app_cpu_usage {cpu}

# HELP app_memory_usage Memory usage percentage
# TYPE app_memory_usage gauge
app_memory_usage {memory}

# HELP app_response_time Response time in seconds
# TYPE app_response_time gauge
app_response_time {response_time}

# HELP app_up Application is up
# TYPE app_up gauge
app_up 1
"""
    return Response(metrics_data, mimetype='text/plain')

@app.route('/load')
def load():
    # Simulate CPU load
    start = time.time()
    while time.time() - start < 5:
        _ = sum(i**2 for i in range(10000))
    return "CPU load generated for 5 seconds"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
