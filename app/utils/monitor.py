from typing import Dict, List

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
    def _get_pids_by_tags(tags: List[str]) -> Dict[int, str]:
        pids_dict: Dict[int, str] = {}

        for proc in psutil.process_iter():
            include_pid = False
            cmds = proc.cmdline()
            cmd_detail = " ".join(cmds)

            for tag in tags:
                for cmd in cmds:
                    if tag in cmd:
                        include_pid = True
                        break

                if not include_pid and tag in proc.name():
                    include_pid = True
                    cmd_detail = proc.name()

            if include_pid:
                pids_dict[proc.pid] = cmd_detail

        return pids_dict

    @staticmethod
    def get_memory_usage(tags: list = ["arya", ]) -> tuple:
        pids_dict = Monitor._get_pids_by_tags(tags)
        rss_dict = {}

        total_mem = 0
        for pid, cmd_detail in pids_dict.items():
            try:
                mem = psutil.Process(pid).memory_info().rss
                rss_dict[pid] = {"cmd": cmd_detail, "rss": mem}
            except Exception as e:
                mem = 0

            total_mem += mem

        return total_mem, rss_dict

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
