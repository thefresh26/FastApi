from fastapi import FastAPI
from pydantic import BaseModel, Field #se crea para utilizar los items de manera interactiva
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

class notas(BaseModel):
    id: int
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
class nota(BaseModel):
    id: int
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
class nota_create(BaseModel):
    id: Optional[int] = None
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
    
class nota_update(BaseModel):
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float

notas: List[nota_mejorada] = []

@app.get('/home', tags=['home'])
def getCalificacion() -> List[nota_mejorada]:
    return notas

@app.get('/notas', tags=['Notas'])
def getCalificaciones() -> List[nota]:
    return notas
    

@app.get('/ObtenerConId/{id}', tags=['Notas'])
def getCalificacion(id: int) -> nota:
    
    for nota in notas:
        if nota['id'] == id:
            return nota
        
    return []
    
    
@app.get('/Obetener_estado/', tags=['Notas'])
def get_calificacion(Estado: str):
    
    resultado = []
    
    for calificacion in notas:
        if calificacion['estado'].lower() == Estado.lower():
            resultado.append(calificacion)

    return resultado



@app.post('/Agregar_notas', tags=['Notas']) 

def agregar(notes: notas) -> List[nota]:

    promedio = (
        notes.matematicas +
        notes.español + 
        notes.ed_fisica +
        notes.sociales
    )/4
    estado = 'aprobado' if promedio >= 3.0 else 'reprobado'
    
    nueva = notes
    nueva['promedio'] = promedio
    nueva['estado'] = estado
    
    notas.append(nueva)
    return notas

@app.put('/update/{id}', tags=['Notas'])

def update(id: int, note: nota_update) -> List[nota]:
    
    for nota in notas:
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

    notas.append(nueva)
    return notas

@app.delete('/notas/{id}', tags=['Notas'])
def delete(id: int) -> List[nota]:
    
    for nota in notas:
        if nota['id'] == id:
            notas.remove(nota)
            
    return notas