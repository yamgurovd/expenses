import uvicorn
from fastapi import FastAPI
from src.api.currency import router as currency_router

app = FastAPI(
    title="Expenses",
    description="Приложение Expenses",
)

app.include_router(currency_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
