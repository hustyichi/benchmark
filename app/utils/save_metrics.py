
class FileMetrics(object):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

        columns = ["memory_usage", "cpu_usage"]
        with open(self.file_path, "w") as file:
            raw_data = ",".join(columns)
            file.write(f"{raw_data}\n")

    def memory_format(self, memory: float) -> str:
        memory = memory / 1024 / 1024
        if memory < 1024:
            return f"{round(memory, 1)}M"

        return f"{round(memory / 1024, 1)}G"

    def append_monitor_metric(self, memory_usage: int, cpu_usage: float, rss_dict: dict = {}):
        metric = [self.memory_format(memory_usage), str(cpu_usage)]
        print(f"Memory usage: {self.memory_format(memory_usage)}, cpu usage percent {cpu_usage}")
        for pid, detail in rss_dict.items():
            print(f"Pid {pid}, {detail['cmd']}: {self.memory_format(detail['rss'])}")

        raw_metric = ",".join(metric)
        with open(self.file_path, "a") as file:
            file.write(f"{raw_metric}\n")
