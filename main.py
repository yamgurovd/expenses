import uvicorn
from fastapi import FastAPI
from src.api.currency import currency_router as currency_router
from src.api.category import category_router as category_router

app = FastAPI(
    title="Expenses",
    description="Приложение Expenses",
)

app.include_router(currency_router)
app.include_router(category_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
