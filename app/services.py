import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    return psutil.net_io_counters().bytes_sent

def get_virtual_memory_usage():
    return psutil.virtual_memory().percent