# Deployment Guide

## Application Deployment

The application is deployed on an EC2 instance and runs as a Flask web service.

Steps to deploy the application:

1. Connect to the EC2 instance using SSH.
2. Navigate to the application directory.
3. Install the required Python dependencies.
4. Start the Flask server.

Example command used to start the application:

python3 server.py

Once the server is running, the application exposes the following endpoints:

- /health – verifies that the application is running correctly
- /orders – simulates order creation and generates activity for logging and metrics

These endpoints are used to generate application traffic and produce logs and metrics for monitoring.

---

## Observability Setup

The system includes an observability stack built using AWS services.

The CloudWatch agent runs on the EC2 instance and is responsible for sending application logs and system metrics to CloudWatch.

The observability pipeline works as follows:

1. The application generates structured logs and metrics.
2. The CloudWatch agent collects this data from the instance.
3. Logs are sent to CloudWatch Logs.
4. Metrics are published to CloudWatch Metrics.
5. Dashboards visualize the metrics for monitoring.
6. CloudWatch alarms monitor the metrics and detect abnormal behavior.
7. When a threshold is exceeded, the alarm triggers a notification through Amazon SNS.

This setup allows the system to be monitored continuously and makes troubleshooting significantly easier if issues occur.