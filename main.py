from fastapi import FastAPI
from routes.home import router as home_router
from routes.predict import router as predict_router
from routes.predicts import router as predicts_router

# Initialize FastAPI
app = FastAPI()

# Include routers
app.include_router(home_router)
app.include_router(predict_router)
app.include_router(predicts_router)

# Run the app with: uvicorn main:app --reload
