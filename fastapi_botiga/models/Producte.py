from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Numeric
from typing import Optional

# Activitat 1. 


# Taula de productes
class Producte(SQLModel, table=True):
    id : int = Field(defaul = None, primary_key=True)
    nom : str 
    descripcio : str = Field(sa_column=Column(String(100)))  #dada sensible
    preu : float = Field(sa_column=Column(Numeric(10,2)))
    stock : int = Field(default = 0)
    categoria : str = Field(sa_column=Column(String(50)))


# Model per rebre dades del client (sense id)
class ProducteRequest():
    nom : str 
    descripcio : str 
    preu : float 
    stock : int 
    categoria : str 


# Model per enviar dades al client (sense camps sensibles)
class ProducteResponse():
    nom : str 
    preu : float 
    stock : int 
    categoria : str 
# Si creieu que cal crear algun model més segons funcionalitat teniu llibertat per a crear-ho.
