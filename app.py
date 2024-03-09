import uvicorn

from src.app_initializer import initialize_data
from src.main import app

if __name__ == "__main__":
    initialize_data()
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5000,
    )
