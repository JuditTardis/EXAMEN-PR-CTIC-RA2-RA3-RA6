# EXAMEN PRÀCTIC — RA2, RA3, RA6

| Camp | Detall |
|---|---|
| **Mòdul** | Desenvolupament d'Aplicacions Web (DAW) |
| **RAs** | RA2, RA3, RA6 |
| **Data** | 2026-06-04 |
| **Temps** | 2 hores |
| **Modalitat** | Individual |

---

## DESCRIPCIÓ DE L'EXAMEN

Se't proporciona un projecte **FastAPI de gestió de productes d'una botiga**. El projecte pot tenir implementada una part i/o amb errors i, en alguns casos, caldrà acabar d'implementar el que calgui per a que l'activitat sigui funcional.

Cal llegir bé les activitats per tal d'entendre què es demana i quines funcions s'han d'implementar.

---

## DISSENY DE LA BASE DE DADES

El projecte treballa amb la taula:

###  `producte`

| Camp | Tipus | Restriccions |
|---|---|---|
| id | INTEGER | PK, autoincremental |
| nom | VARCHAR(100) |  |
| descripcio | TEXT | dada sensible |
| preu | DECIMAL(10,2) |  |
| stock | INTEGER |  default=0 |
| categoria | VARCHAR(50) |  |

---

## TASQUES A REALITZAR

Per a cada activitat revisar fitxers **.env**, **main.py**, **models**, **crud** i **service** per fer les modificacions marcades per activitat segons el que es demani a continuació:

> **Recordatori**: Si voleu provar el codi, es pot crear un entorn virtual i instal·lar-vos les dependències que ja estan a **requirements.txt**. Caldrà també iniciar el servei docker. 


### [ACTIVITAT 1]  - Completar els models.

Al completar els models, potser us trobeu que no podeu saber com definir un model fins que no feu alguna activitat futura, ja ho implementareu quan es demani en una activitat posterior. NO es demana cap gestió d'excepcions.

> **Indicacions**: Un cop acabada l'activitat 1, fer un commit de nom "Activitat 1 acabada". I procedir a realitzar la següent activitat.


### [ACTIVITAT 2] - Afegir un producte nou.

Recorda implementar tots les funcions en aquells fitxers on sigui necessari per a que l'activitat sigui funcional. NO es demana cap gestió d'excepcions.

> **Indicacions**: Un cop acabada l'activitat 2, fer un commit de nom "Activitat 2 acabada". I procedir a realitzar la següent activitat.

### [ACTIVITAT 3] - Lectura de la taula.

Recorda implementar tots les funcions en aquells fitxers on sigui necessari per a que l'activitat sigui funcional. NO es demana cap gestió d'excepcions.

> **Indicacions**: Un cop acabada l'activitat 3, fer un commit de nom "Activitat 3 acabada". I procedir a realitzar la següent activitat.

### [ACTIVITAT 4] - Modificació total o parcial

Recorda implementar tots les funcions en aquells fitxers on sigui necessari per a que l'activitat sigui funcional. NO es demana cap gestió d'excepcions.

> **Indicacions**: Un cop acabada l'activitat 4, fer un commit de nom "Activitat 4 acabada".


**Verificació del funcionament que farà el professorat**: amb la documentació interactiva de FastAPI (`localhost:8000/docs`):
   - Es probarà crear mínim **5 productes** de categories diverses.
   - Es verificarà que el GET de tots els productes funcioni correctament.
   - Es provarà la modificació parcial o total d'un producte (depenent del que hagiu implementat).

---

## PAS A PAS ORIENTATIU PER INICIAR L'EXAMEN

1. Crear entorn virtual amb Virtualenv (no és obligatòria però bona pràctica).
2. Habilitar l'entorn virtual.
3. Crear fitxer requirements.txt per a installar les dependències necessàries.
4. Crear el fitxer docker-compose.yml.
5. Crear el fitxer .env.
6. Començar a crear l'estructura de l'activitat i començar a programar.

## ESTRUCTURA DEL PROJECTE

```
fastapi_botiga/
├── main.py                  # Endpoints 
├── services/
│   ├── __init__.py
│   └── service_producte.py  # Lògica de negoci 
├── crud/
│   ├── __init__.py
│   └── crud_producte.py    # Consultes a la BD 
├── models/
│   ├── __init__.py
│   └── Producte.py          # Models SQLModel 
├── .env                     # Variables d'entorn 
├── docker-compose.yml       # Servei PostgreSQL 
└── requirements.txt         # Dependències
```
---
## CODI PROPORCIONAT

### `models/Producte.py`

```python
from sqlmodel import SQLModel, Field
from typing import Optional

# Activitat 1. 


# Taula de productes
class Producte():



# Model per rebre dades del client (sense id)
class ProducteRequest():



# Model per enviar dades al client (sense camps sensibles)
class ProducteResponse():

# Si creieu que cal crear algun model més segons funcionalitat teniu llibertat per a crear-ho.

```

---

### `main.py`

```python
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
```
### Services
```python

# ─── SERVEI PRODUCTES ────────────────────────────────────────────────────────

def crear_producte_service(db: Session):
    """Lògica de negoci: valida que el preu sigui positiu abans de crear i retorna un error de preu si és negatiu"""
    return


def get_productes_service(db: Session):
    '''implementar lògica de negoci per a obtenir els productes de la taula productes i tornar la resposta que s'ha de enviar al client'''
    return 



def update_producte_service(db: Session):
    """Lògica de negoci: valida que el preu sigui positiu abans d'actualitzar. i envia error si no és un valor positiu"""
    return
```
### Crud
```python

# ─── CRUD PRODUCTES ──────────────────────────────────────────────────────────

def crear_producte(db: Session):
    """
    Crea un nou producte a la base de dades.
    Retorna un missatge de confirmació.
    Recorda que cal convertir les dades, afegir l'objecte a la sessió i confirmar canvis.
    """
    return


def get_productes(db: Session):
    """
    Obté tots els productes de la base de dades.
    Retorna una llista d'objectes Producte.
    """
    return


def update_producte(db: Session):
    """
    Actualitza tots els camps d'un producte o un camp (el que vulguis).
    Retorna missatge d'actualització correcte o error si no existeix el producte.
    """
    return

```

---

## FITXERS DE CONFIGURACIÓ

### `.env`

```
DATABASE_URL=postgresql+psycopg2://_________:________@localhost:______/_______
```

### `docker-compose.yml`

```yaml
version: '3.1'
services:
  db:
    image: postgres:13
    container_name: db_botiga
    environment:
      - POSTGRES_DB=botiga_db
      - POSTGRES_PASSWORD=passwd
      - POSTGRES_USER=usuari
    ports:
      - "5432:5432"
    volumes:
      - local_pgdata:/var/lib/postgresql/data
  pgadmin:
    image: dpage/pgadmin4
    container_name: pg_botiga
    ports:
      - "80:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    volumes:
      - pgadmin-data:/var/lib/pgadmin
volumes:
  local_pgdata:
  pgadmin-data:
```

### `requirements.txt`

```
fastapi[standard]
sqlmodel
psycopg2-binary
python-dotenv
uvicorn
```

---


## CRITERIS D'AVALUACIÓ

Es realitzarà una revisió del codi i es provarà el funcionament de l'API. Cal intentar totes les activitats; no s'accepta completar només algunes per acumular punts. La nota es determina primer per la funcionalitat de cada activitat i, un cop avaluada, s'ajusta en funció d'errors menors de codi (noms incorrectes, camps que falten, status codes erronis, etc.).

| Criteri | Puntuació |
|---|---|
| `activitat 1`  | 25 pts |
| `activitat 2`  | 25 pts |
| `activitat 3`  | 25 pts |
| `activitat 4`  | 25 pts |
| **TOTAL**| **100 pts**|
