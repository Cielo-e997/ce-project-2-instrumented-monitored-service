APP_NAME = "order-service"
APP_HOST = "0.0.0.0"
APP_PORT = 5000

LOG_LEVEL = "INFO"
LOG_FILE = "/home/ubuntu/app/app.log"

CLOUDWATCH_NAMESPACE = "OrderService"
AWS_REGION = "eu-central-1"

METRICS = {
    "request_count": "RequestCount",
    "error_count": "ErrorCount",
    "api_latency": "APILatency",
    "orders_created": "OrdersCreated"
}