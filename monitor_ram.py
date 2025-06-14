from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/ram")
async def get_ram_usage():
    """Returns RAM usage in percentage."""
    return {"ram_usage": psutil.virtual_memory().percent}

# To run this application, use the following command:
# uvicorn <filename_without_py_extension>:app --reload
