from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field#se crea para utilizar los items de manera interactiva
from typing import Optional, List
import datetime

app = FastAPI()

class nota_mejorada(BaseModel):
    id: Optional[int] = None
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    profesor: str = Field(min_digits=6, max_length=15)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    
    model_config = {
        'json_schema_extra':{
            'example':{
                
                'id': 1,
                'year': 2025,
                'matematicas': 2.0,
                'español': 2.9,
                'ed_fisica': 2.3,
                'sociales': 1.9,
                'profesor': 'pancho',
            }   
        }
    }

class nota_actulizar(BaseModel):
    id: Optional[int] = None
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
class nota_sin_id(BaseModel):
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    year: int

    model_config = {
        'json_schema_extra': {
            'example':{
                'matematicas': 0,
                'español': 0,
                'ed_fisica': 0,
                'sociales': 0,
                'year': '1900 - 2025'
            }
        }
    }

base_notas: List[dict] = []

@app.get('/Todo', tags=['home'])
def getCalificacion() -> List[dict]:
    return base_notas

@app.get('/notas', tags=['Notas'])
def getCalificaciones() -> List[dict]:
    return base_notas
    

@app.get('/ObtenerConId/{id}', tags=['Notas'])
def getCalificacion(id: int = Path(gt=0)) -> dict:
    
    for nota in base_notas:
        if nota['id'] == id:
            return nota
        
    return []
    
    
@app.get('/Obetener_estado/', tags=['Notas'])
def get_calificacion(Estado: str = Query(min_length=6,max_length=15)) -> dict:

    
    
    for nota in base_notas:
        if nota['estado'] == Estado:
            return nota
        
    return {}


@app.post('/Agregar_notas', tags=['Notas']) 
def agregar(notes: nota_mejorada) -> List[dict]:

    promedio = (
        notes.matematicas +
        notes.español + 
        notes.ed_fisica +
        notes.sociales
    )/4
    estado = 'aprobado' if promedio >= 3.0 else 'reprobado'
    
    nueva = notes.model_dump()
    nueva['promedio'] = promedio
    nueva['estado'] = estado
    
    base_notas.append(nueva)
    return base_notas

@app.put('/update/{id}', tags=['Notas'])
def update(id: int, note: nota_sin_id) -> List[dict]:
    
    for nota in base_notas:
        if nota['id'] == id:
            nota['matematicas'] = note.matematicas
            nota['español'] = note.español
            nota['ed fisica'] = note.ed_fisica
            nota['sociales'] = note.sociales
    
    promedio = (
                note.matematicas + 
                note.español + 
                note.ed_fisica + 
                note.sociales
                ) / 4
    
    estado = 'aprobado' if promedio >= 3.0 else 'reprobado'

    nueva = note.model_dump()
    nueva['promedio'] = promedio
    nueva['estado'] = estado

    return base_notas

@app.delete('/notas/{id}', tags=['Notas'])
def delete(id: int) -> List[dict]:
    
    for nota in base_notas:
        if nota['id'] == id:
            base_notas.remove(nota)
            
    return base_notas