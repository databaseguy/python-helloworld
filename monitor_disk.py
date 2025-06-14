from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/disk")
async def get_disk_usage():
    """Returns disk usage metrics for the root filesystem."""
    disk = psutil.disk_usage('/')
    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent
    }

@app.get("/disk/partitions")
async def get_disk_partitions():
    """Returns information about mounted disk partitions."""
    partitions = psutil.disk_partitions()
    partition_info = []
    for partition in partitions:
        partition_info.append({
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "fstype": partition.fstype,
            "opts": partition.opts
        })
    return {"partitions": partition_info}

@app.get("/disk/io")
async def get_disk_io():
    """Returns disk I/O statistics."""
    io_stats = psutil.disk_io_counters()
    return {
        "read_count": io_stats.read_count,
        "write_count": io_stats.write_count,
        "read_bytes": io_stats.read_bytes,
        "write_bytes": io_stats.write_bytes,
        "read_time": io_stats.read_time,
        "write_time": io_stats.write_time
    }
