from fastapi import FastAPI, Depends, status
from fastapi.exceptions import HTTPException
from sqlmodel import SQLModel, create_engine, Session
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
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

@app.___("/api/v1/productes", response_model=)
def create_product(producte: , db: Session = Depends()):
    # Afegir funcionalitat

    return 



#ACTIVITAT 3 - READ: Posar el codi necessari aqui
''' READ - Path: "/api/v1/productes" 
 Funcionalitat: Lectura de la taula productes i mostrar el client aquesta la informació demanada.
'''


# ACTIVITAT 4 - UPDATE: Posar el codi necessari aqui
'''UPDATE: Path: "/api/v1/productes/{producte_id}" 
Funcionalitat: Modificació total o parcial (PUT/PATCH)
Es demana una resposta indicant que s'ha fet la modificació correctament.
'''