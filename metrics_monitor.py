import argparse
import enum
import time

from app.utils.monitor import Monitor
from app.utils.save_metrics import FileMetrics


class Service(enum.Enum):
    ARYA = "arya"
    FATE = "fate"
    SECRET_FLOW = "secret_flow"


def save_arya_metrics(service: Service):
    if service == Service.ARYA:
        tags = ["arya", ]
    elif service == Service.FATE:
        tags = ["fate", ]
    else:
        tags = ["ray", ]

    file_metrics = FileMetrics(f"{service.value}_usage.csv")

    while True:
        cpu_usage = Monitor.get_cpu_usage(tags)
        memory_usage, rss_dict = Monitor.get_memory_usage(tags)

        file_metrics.append_monitor_metric(memory_usage, cpu_usage, rss_dict)
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--service', type=Service, default=Service.ARYA, required=False, help="check service")

    args = parser.parse_args()
    save_arya_metrics(args.service)
