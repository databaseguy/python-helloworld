from fastapi import FastAPI
import psutil  # Assuming you are using psutil for CPU monitoring

app = FastAPI()

# Route to get CPU usage information
@app.get("/cpu")
async def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)  # Returns CPU usage as a percentage
    return {"cpu_usage": cpu_usage}

# Route to get CPU core information
@app.get("/cpu/cores")
async def get_cpu_cores():
    core_usage = psutil.cpu_percent(interval=1, percpu=True)  # Returns usage per core
    return {"core_usage": core_usage}

# Route to get CPU frequency information
@app.get("/cpu/frequency")
async def get_cpu_frequency():
    frequency = psutil.cpu_freq()  # Returns CPU frequency info
    return {
        "current": frequency.current,
        "min": frequency.min,
        "max": frequency.max
    }
