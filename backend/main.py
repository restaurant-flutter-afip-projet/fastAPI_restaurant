import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.api.endpoints.reservation import router_reservation
from backend.api.endpoints.menu import router_menu
from backend.api.endpoints.table import router_table

app = FastAPI(title="Restaurant API")

app.include_router(router_menu, prefix="/api/menu", tags=["Menu"])
app.include_router(router_reservation, prefix="/api/reservation", tags=["Reservations"])
app.include_router(router_table, prefix="/api/table", tags=["Tables"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)