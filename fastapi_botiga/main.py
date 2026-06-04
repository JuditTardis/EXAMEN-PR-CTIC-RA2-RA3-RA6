from fastapi import FastAPI, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel import SQLModel, create_engine, Session
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models.Producte import Producte, ProducteRequest, ProducteResponse
from services.service_producte import crear_producte_service, get_productes_service
import os


# 1. Carregar variables d'entorn
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# 2. Crear taules
SQLModel.metadata.create_all(engine)

app = FastAPI()

# Sessió de BD
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


# ─── ENDPOINTS PRODUCTES ────────────────────────────────────────────────────

# ACTIVITAT 2 - CREATE: Modificar el codi per a que sigui funcional:

@app.post("/api/v1/productes", response_model=ProducteResponse)
def create_product(producte: ProducteRequest, db: Session = Depends()):
    return crear_producte_service(db, producte)



#ACTIVITAT 3 - READ: Posar el codi necessari aqui
@app.get("/api/v1/productes", response_model=ProducteResponse)
def read_product(db: Session = Depends()):
    return get_productes_service(db)


# ACTIVITAT 4 - UPDATE: Posar el codi necessari aqui
'''UPDATE: Path: "/api/v1/productes/{producte_id}" 
Funcionalitat: Modificació total o parcial (PUT/PATCH)
Es demana una resposta indicant que s'ha fet la modificació correctament.
'''