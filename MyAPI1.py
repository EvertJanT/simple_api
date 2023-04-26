from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

import random

kleuren = ['rood','geel', 'groen', 'blauw']

# maak een  FastAPI app
EJapp = FastAPI()

# API endpoint
@EJapp.get('/')
def hello():
    return {'message': 'met /kleur kun je de API veschillende kleuren laten kiezen'}

# nieuw endpoint
@EJapp.get('/kleur')
def kleur():
    kleur = str(genereer_kleur())
    return {'message': 'Ik kies voor ' + kleur}

# een simpel request body model
class EJModel(BaseModel):
    invul_veld1: str

# een POST endpoint met de request body
@EJapp.post('/extra_kleur')
def extra_kleur(data: EJModel):
    nieuwe_kleur = str(data.invul_veld1)
    kleur_toevoegen(nieuwe_kleur)
    return {'message': kleuren}

# maak de OpenAPI specificatiebereikbaar via '../doc' of '../redoc'
def custom_openapi():
    openapi_schema = get_openapi(
        title="Evert Jan's kleuren API",
        version="1.0",
        description="Dit is een beschrijving van mijn kleuren API",
        routes=EJapp.routes,
    )
    return openapi_schema

def genereer_kleur():
    random_kleur = random.choice(kleuren)
    return random_kleur

def kleur_toevoegen(nieuwe_kleur):
    kleuren.append(nieuwe_kleur)
    

EJapp.openapi = custom_openapi

# Run 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(EJapp, host='localhost', port=8080)


   
