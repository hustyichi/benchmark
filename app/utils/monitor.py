from typing import List

import psutil


class Monitor(object):
    @staticmethod
    def _check_related_process(tag: str, proc: psutil.Process) -> bool:
        if tag in proc.name():
            return True

        for cmd in proc.cmdline():
            if tag in cmd:
                return True

        return False

    @staticmethod
    def _get_pids_by_tags(tags: List[str]) -> List[int]:
        pids: List[int] = []

        for proc in psutil.process_iter():
            for tag in tags:
                if Monitor._check_related_process(tag, proc):
                    pids.append(proc.pid)

        return pids

    @staticmethod
    def get_memory_usage(tags: list = ["arya", ]) -> int:
        pids = Monitor._get_pids_by_tags(tags)

        total_mem = 0
        for pid in pids:
            try:
                mem = psutil.Process(pid).memory_info().rss
            except Exception as e:
                mem = 0

            total_mem += mem

        return total_mem

    @staticmethod
    def get_cpu_usage(tags: list = ["arya", ]) -> float:
        pids = Monitor._get_pids_by_tags(tags)

        total_cpu = 0
        for pid in pids:
            try:
                cpu = psutil.Process(pid).cpu_percent(0.1)
            except Exception as e:
                cpu = 0

            total_cpu += cpu / psutil.cpu_count()

        return total_cpu / 100
