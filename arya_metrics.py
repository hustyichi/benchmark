from app.utils.monitor import Monitor
from app.utils.save_metrics import FileMetrics


def save_arya_metrics():
    arya_tags = ["arya", ]

    while True:
        cpu_usage = Monitor.get_cpu_usage(arya_tags)
        memory_usage = Monitor.get_memory_usage(arya_tags)

        file_metrics = FileMetrics("arya_usage.csv")
        file_metrics.append_monitor_metric(memory_usage, cpu_usage)


if __name__ == "__main__":
    save_arya_metrics()
