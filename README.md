# Observability & Monitoring Stack

A minimal working implementation of an observability stack using Docker Compose, Prometheus, Grafana, and a demo Flask application.

## 🚀 Quick Start (Under 10 Minutes!)

### Prerequisites
- Docker Desktop installed and running
- Docker Compose available

### Setup & Run

1. **Clone and navigate to the directory:**
```bash
cd observability-stack
```

2. **Start all services:**
```bash
docker-compose up --build -d
```

3. **Wait 30 seconds for services to start**, then access:
   - **Demo App:** http://localhost:5000
   - **Prometheus:** http://localhost:9090
   - **Grafana:** http://localhost:3000 (user: `admin`, password: `admin`)
   - **Node Exporter:** http://localhost:9100

## 📊 Verify Setup

### Check Prometheus Targets
1. Go to http://localhost:9090/targets
2. All targets should show "UP" status

### View Grafana Dashboard
1. Login to Grafana at http://localhost:3000
2. Navigate to Dashboards
3. Open "App Monitoring Dashboard"
4. You should see CPU, Memory, App Status, and Response Time panels

### Check Alerts
1. Go to http://localhost:9090/alerts
2. You should see 2 alert rules configured:
   - `HighCPUUsage` - triggers when CPU > 70%
   - `AppDown` - triggers when app is unavailable

## 🔥 Trigger Alerts

### Generate CPU Load
```bash
# Visit this endpoint to simulate high CPU usage
curl http://localhost:5000/load
```

Then check http://localhost:9090/alerts to see the `HighCPUUsage` alert fire after ~30 seconds.

### Run Alert Dispatcher
```bash
# Start the alert dispatcher in a new terminal
./alert_dispatcher.sh
```

This script checks for active alerts every 30 seconds and logs them to `alert_logs.txt`.

## 📁 Project Structure

```
observability-stack/
├── docker-compose.yml          # Defines all services
├── prometheus.yml              # Prometheus configuration
├── alert.rules.yml             # Alert definitions
├── grafana-dashboard.json      # Grafana dashboard
├── alert_dispatcher.sh         # Alert logging script
├── app/
│   ├── app.py                  # Flask demo application
│   └── Dockerfile              # App container definition
└── README.md                   # This file
```

## 🎯 What's Monitored

The demo app exposes these metrics at `/metrics`:
- **app_cpu_usage** - CPU usage percentage
- **app_memory_usage** - Memory usage percentage
- **app_response_time** - Response time in seconds
- **app_up** - Application availability (1 = up, 0 = down)

## ⚙️ How It Works

1. **App Container:** Runs a Flask app that exposes Prometheus-format metrics
2. **Prometheus:** Scrapes metrics from the app and node-exporter every 15s
3. **Grafana:** Visualizes metrics in a dashboard
4. **Node Exporter:** Provides system-level metrics
5. **Alert Rules:** Monitor CPU usage and app availability
6. **Alert Dispatcher:** Logs active alerts to a file

## 🛑 Stop & Cleanup

```bash
# Stop all services
docker-compose down

# Remove volumes and images
docker-compose down -v --rmi all
```

## 🐛 Troubleshooting

**Grafana dashboard not showing data?**
- Wait 1-2 minutes for Prometheus to scrape metrics
- Check Prometheus targets are UP at http://localhost:9090/targets

**Alerts not firing?**
- Visit http://localhost:5000/load to generate CPU load
- Wait 30-60 seconds for alert evaluation

**Alert dispatcher not working?**
- Make sure jq is installed: `sudo apt-get install jq` (Linux) or `brew install jq` (Mac)
- Ensure Prometheus is accessible at http://localhost:9090

## 📸 Screenshots

Place your dashboard screenshots in `/screenshots/dashboard.png`

## 🎓 Learning Resources

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

---

**Created for Scenario 3: Observability & Monitoring Stack**
