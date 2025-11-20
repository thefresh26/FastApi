from fastapi import FastAPI
from pydantic import BaseModel #se crea para utilizar los items de manera interactiva
from typing import Optional, List
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
        'promedio': (2.5 + 3.9 + 2.6 + 2.2)/4,
        'estado': 'reprobado'
    },
        
    {
        'id': 2,
        'matematicas': 2.5,
        'español': 3.9,
        'ed fisica': 4.6,
        'sociales': 4.3,
        'promedio': (2.5 + 3.9 + 4.6 + 4.3)/4,
        'estado': 'aprobado'
    }
    
]


@app.get('/home', tags=['home'])
def getCalificacion():
    return notas

@app.get('/notas', tags=['Notas'])
def getCalificaciones():
    return notas

@app.get('/ObtenerConId/{id}', tags=['Notas'])
def getCalificacion(id: int) -> Organized:
    
    for nota in notas:
        if nota['id'] == id:
            return nota
        
    return []
    
    
@app.get('/Obetener_estado/', tags=['Notas'])
def get_calificacion(Estado: str) -> Organized:
    
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

def update(id: int, note: Organized) -> List[Organized]:
    
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
def delete(id: int):
    
    for nota in notas:
        if nota['id'] == id:
            notas.remove(nota)
            
    return notas