#!/usr/bin/env python3

import psutil
import time

# Date and time
print(time.strftime("%d %b %Y • %H:%M • %I:%M %p"))

# CPU
cpu_cores = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current / 1000
cpu_summary = "CPU: {} cores {} GHz".format(cpu_cores, cpu_freq)
print(cpu_summary)

# RAM
ram_total = round(psutil.virtual_memory().total / (1024 * 1024))
ram_used = round(psutil.virtual_memory().used / (1024 * 1024))
ram_free = round(psutil.virtual_memory().available / (1024 * 1024))
ram_percent = round((ram_total - ram_free) / ram_total * 100)
ram_summary = "RAM: {}/{} MB ({}%)".format(ram_used, ram_total, ram_percent)
print(ram_summary)

# Swap
swap_total = round(psutil.swap_memory().total / (1024 * 1024))
swap_used = round(psutil.swap_memory().used / (1024 * 1024))
swap_free = round(psutil.swap_memory().free / (1024 * 1024))
swap_percent = round((swap_total - swap_free) / swap_total * 100)
swap_summary = "Swap: {}/{} MB ({}%)".format(swap_used, swap_total, swap_percent)
if swap_total:
    print(swap_summary)


