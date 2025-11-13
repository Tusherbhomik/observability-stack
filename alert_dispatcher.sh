#!/bin/bash

# Alert dispatcher script - queries Prometheus and logs active alerts

PROMETHEUS_URL="http://localhost:9090"
LOG_FILE="alert_logs.txt"

echo "Starting alert dispatcher..."
echo "Logging alerts to $LOG_FILE"

while true; do
    # Query Prometheus alerts API
    ALERTS=$(curl -s "${PROMETHEUS_URL}/api/v1/alerts" | \
             jq -r '.data.alerts[] | select(.state=="firing") | 
             "[\(.labels.alertname)] \(.annotations.summary) - \(.annotations.description)"' 2>/dev/null)
    
    if [ ! -z "$ALERTS" ]; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        echo "[$TIMESTAMP] ACTIVE ALERTS:" >> "$LOG_FILE"
        echo "$ALERTS" >> "$LOG_FILE"
        echo "---" >> "$LOG_FILE"
        echo "[$TIMESTAMP] Alert detected and logged"
    fi
    
    sleep 30
done
