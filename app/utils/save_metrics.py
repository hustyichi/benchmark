
class FileMetrics(object):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        columns = ["memory_usage", "cpu_usage"]
        with open(self.file_path, "w") as file:
            raw_data = ",".join(columns)
            file.writelines([raw_data,])

    def append_metric(self, metric_msg: str):
        with open(self.file_path, "a") as file:
            file.writelines([metric_msg, ])

    def append_monitor_metric(self, memory_usage: int, cpu_usage: float):
        metric = [memory_usage, cpu_usage]
        raw_metric = ",".join(metric)
        self.append_metric(raw_metric)
