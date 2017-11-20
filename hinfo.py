#!/usr/bin/env python3

import psutil
import colorama
import tabulate

# Constants
GREEN = colorama.Fore.GREEN
GRAY = colorama.Style.DIM
CYAN = colorama.Fore.CYAN
BLUE = colorama.Fore.BLUE
RED = colorama.Fore.RED
RT = colorama.Style.RESET_ALL

# CPU
cpu_cores = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current / 1000
cpu_summary = GRAY+"CPU:"+RT+" {} cores {} GHz".format(cpu_cores, cpu_freq)
print(cpu_summary)

# RAM
ram_total = round(psutil.virtual_memory().total / (1024 * 1024))
ram_used = round(psutil.virtual_memory().used / (1024 * 1024))
ram_free = round(psutil.virtual_memory().available / (1024 * 1024))
ram_percent = round((ram_total - ram_free) / ram_total * 100)
ram_summary = GRAY+"RAM:"+RT+" {}/{} MB ({}%)".format(ram_used, ram_total, ram_percent)
print(ram_summary)

# Swap
swap_total = round(psutil.swap_memory().total / (1024 * 1024))
swap_used = round(psutil.swap_memory().used / (1024 * 1024))
swap_free = round(psutil.swap_memory().free / (1024 * 1024))
swap_percent = round((swap_total - swap_free) / swap_total * 100)
swap_summary = GRAY+"Swap:"+RT+" {}/{} MB ({}%)".format(swap_used, swap_total, swap_percent)
if swap_total:
    print(swap_summary)

# Network interfaces
print()
print(GRAY+"Network:"+RT)
for interface in sorted(psutil.net_if_stats()):
    if interface in ('lo' 'localhost'):
        # skip local interface
        continue
    status = GREEN+"●" if psutil.net_if_stats()[interface].isup else RED+"○"
    print(status, interface, RT)
    for snic in psutil.net_if_addrs()[interface]:
        # mac
        if snic.family == 17:
            color = BLUE
            prefix = GRAY+"mac: "+RT
        # ipv6
        elif snic.family == 10:
            color = CYAN
            prefix = GRAY+"ipv6:"+RT
        # ipv4
        elif snic.family == 2:
            color = RT
            prefix = GRAY+"ipv4:"+RT
        print(' ', prefix, color+snic.address.split('%')[0], RT)

# Disk info
print()
head = [GRAY+'Device', 'mount', 'fs', 'use', 'used/total (GB)'+RT]
disk_table = []
for partition in sorted(psutil.disk_partitions()):
    space = psutil.disk_usage(partition.mountpoint)
    used = str(round(space.used / (1024 * 1024 * 1024), 2))
    total = str(round(space.total / (1024 * 1024 * 1024), 2))
    percent = str(round(space.percent))+"%"
    disk_table.append([GREEN+partition.device+RT, partition.mountpoint, partition.fstype, CYAN+percent+RT, BLUE+used+RT+"/"+BLUE+total+RT])

print(tabulate.tabulate(disk_table, headers=head, tablefmt="plain"))
print()
