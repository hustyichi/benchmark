
class FileMetrics(object):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        columns = ["memory_usage", "cpu_usage"]
        with open(self.file_path, "w") as file:
            raw_data = ",".join(columns)
            file.write(f"{raw_data}\n")

    def append_metric(self, metric_msg: str):
        with open(self.file_path, "a") as file:
            file.write(f"{metric_msg}\n")

    def append_monitor_metric(self, memory_usage: int, cpu_usage: float):
        metric = [str(memory_usage), str(cpu_usage)]
        print(f"Memory usage: {memory_usage}, cpu usage percent {cpu_usage}")
        raw_metric = ",".join(metric)
        self.append_metric(raw_metric)
