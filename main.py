from fastapi import FastAPI
from routes.home import router as home_router
from routes.predict import router as predict_router
from routes.predicts import router as predicts_router
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(home_router)
app.include_router(predict_router)
app.include_router(predicts_router)

# Run the app with: uvicorn main:app --reload
