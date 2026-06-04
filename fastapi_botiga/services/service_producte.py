from sqlmodel import Session
from crud.crud_producte import crear_producte, get_productes
# ─── SERVEI PRODUCTES ────────────────────────────────────────────────────────

def crear_producte_service(db: Session, dades):
    if dades.preu < 0:
        raise ValueError("El preu no pot ser negatiu")
    return crear_producte()


def get_productes_service(db: Session):
    '''implementar lògica de negoci per a obtenir els productes de la taula productes i tornar la resposta que s'ha de enviar al client'''
    return 



def update_producte_service(db: Session):
    """Lògica de negoci: valida que el preu sigui positiu abans d'actualitzar. i envia error si no és un valor positiu"""
    return