from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Restart App using uvicorn
import uvicorn
app = FastAPI()
# Import routes as
from routes.api import router as api_router

# ENV Conf.
import dotenv
dotenv.load_dotenv()

# Enable CORS for development (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/working")
async def isRunning():
    return {"message":"working"}


app.include_router(api_router)


if __name__=="__main__":
    uvicorn.run('main:app', reload=True)