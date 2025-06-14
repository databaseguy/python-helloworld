from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/memory")
async def get_memory_usage():
    """Returns virtual memory usage metrics."""
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "percent": memory.percent
    }

@app.get("/memory/swap")
async def get_swap_memory_usage():
    """Returns swap memory usage metrics."""
    swap = psutil.swap_memory()
    return {
        "total": swap.total,
        "used": swap.used,
        "free": swap.free,
        "percent": swap.percent,
        "sin": swap.sin,
        "sout": swap.sout
    }
