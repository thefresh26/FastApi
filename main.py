from fastapi import FastAPI, Body
from pydantic import BaseModel #se crea para utilizar los items de manera interactiva
from typing import Optional
app = FastAPI()



class Organized(BaseModel):
    id: Optional[int] = None
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
    
class NotasUpdate(BaseModel):
    id: Optional[int] = None
    matematicas: float
    español: float
    ed_fisica: float
    sociales: float
    
notas = [
    
    {
        'id': 1,
        'matematicas': 2.5,
        'español': 3.9,
        'ed fisica': 2.6,
        'sociales': 2.2,
    },
        
    {
        'id': 2,
        'matematicas': 2.5,
        'español': 3.9,
        'ed fisica': 4.6,
        'sociales': 4.3,
    }
    
]
        
@app.get('/Calificaciones', tags=['home'])
def getCalificacion():
    return notas

@app.get('/ObtenerConId/{id}', tags=['Notas'])
def getCalificacion(id: int):
    
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

def agregar(notes: Organized):
    global promedio
    global estado
    
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
    
    notas.append(nueva)
    return notas

@app.put('/update/{id}', tags=['Notas'])

def update(
    id: int, note: Organized
):
    
    for nota in notas:
        if nota['id'] == id:
            nota['matematicas'] = note.matematicas
            nota['español'] = note.español
            nota['ed fisica'] = note.ed_fisica
            nota['sociales'] = note.sociales
    
    return notas
    
    
@app.delete('/notas/{id}', tags=['Notas'])
def delete(
    id: int
):
    
    for nota in notas:
        if nota['id'] == id:
            notas.remove(nota)
            
    return notas