from .core.util import human_readable_size
import time


def print_progress_bar(done: int, total: int, start_time: float, bar_length: int = 20):
    percent = done / total if total else 0
    percent_display = round(percent * 100, 1)

    filled = int(bar_length * percent)
    bar = "█" * filled + "░" * (bar_length - filled)

    elapsed = time.time() - start_time
    speed = done / elapsed if elapsed > 0 else 0

    remaining = total - done
    eta = remaining / speed if speed > 0 else 0

    def fmt_time(sec):
        m, s = divmod(int(sec), 60)
        h, m = divmod(m, 60)
        if h:
            return f"{h:02}:{m:02}:{s:02}"
        return f"{m:02}:{s:02}"

    print(f"{percent_display}% {bar} | {human_readable_size(speed)}/s ETA {fmt_time(eta)}", end="\r")
    if percent_display >= 100:
        print()