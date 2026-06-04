from sqlmodel import Session, select
from models import Producte, ProducteRequest
# ─── CRUD PRODUCTES ──────────────────────────────────────────────────────────

def crear_producte(db: Session, producte: Producte):
    db.add(producte)
    db.commit()
    db.refresh(producte)
    return producte


def get_productes(db: Session):
    resultat = db.exec(select(Producte))
    return resultat.all()


def update_producte(db: Session, producte_id: int, dades: ProducteRequest):
    producte = db.get(Producte, producte_id)
    if producte is None:
        return None
    
    producte.sqlmodel_update(dades.model_dump(exclude_unset=True))

    db.add(producte)
    db.commit()
    db.refresh(producte)
    """
    Actualitza tots els camps d'un producte o un camp (el que vulguis).
    Retorna missatge d'actualització correcte o error si no existeix el producte.
    """
    return producte
