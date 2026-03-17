# Alerting

## CloudWatch Alarms

CloudWatch alarms were configured to detect abnormal system behavior.

These alarms continuously monitor system metrics and trigger when thresholds are exceeded.

Examples of monitored conditions include:

- high CPU utilization
- increased request latency
- abnormal error rates

---

## Alarm Thresholds

Thresholds were selected to represent values that indicate potential system issues.

For example, a sudden increase in latency may indicate performance degradation or increased load.

By defining these thresholds in advance, the system can automatically detect unusual conditions.

---

## Notification System

When an alarm is triggered, CloudWatch sends a notification through Amazon SNS.

SNS distributes alerts to subscribers so that issues can be investigated.

This automated alerting mechanism ensures that problems can be detected and addressed quickly.