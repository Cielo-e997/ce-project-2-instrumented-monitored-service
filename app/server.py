import uuid
import time
import logging
from datetime import datetime

import boto3
import structlog
from flask import Flask, request, jsonify

from config import CLOUDWATCH_NAMESPACE, AWS_REGION

app = Flask(__name__)

# CloudWatch client
cloudwatch = boto3.client("cloudwatch", region_name=AWS_REGION)

# Logging configuration
logging.basicConfig(level=logging.INFO)

logger = structlog.get_logger()


def publish_metric(name, value, unit="Count"):
    try:
        cloudwatch.put_metric_data(
            Namespace=CLOUDWATCH_NAMESPACE,
            MetricData=[
                {
                    "MetricName": name,
                    "Value": value,
                    "Unit": unit,
                    "Timestamp": datetime.utcnow()
                }
            ]
        )
    except Exception as e:
        print({"metric_error": str(e)})


@app.before_request
def before_request():
    request.start_time = time.time()
    request.correlation_id = str(uuid.uuid4())

    logger.info(
        "request_received",
        correlation_id=request.correlation_id,
        method=request.method,
        path=request.path
    )

    publish_metric("RequestCount", 1)


@app.after_request
def after_request(response):
    latency = (time.time() - request.start_time) * 1000

    logger.info(
        "request_completed",
        correlation_id=request.correlation_id,
        method=request.method,
        path=request.path,
        status_code=response.status_code,
        latency_ms=round(latency, 2)
    )

    publish_metric("APILatency", latency, "Milliseconds")

    if response.status_code >= 400:
        publish_metric("ErrorCount", 1)

    return response


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/orders", methods=["POST"])
def create_order():
    publish_metric("OrdersCreated", 1)

    logger.info(
        "order_created",
        correlation_id=request.correlation_id
    )

    return jsonify({"message": "order created"}), 201


@app.route("/")
def index():
    return jsonify({"message": "Order Service Running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)