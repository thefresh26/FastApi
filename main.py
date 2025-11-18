from fastapi import FastAPI


app = FastAPI()

notas = [
    
    {
        'id': 1,
        'matematicas': 2.5,
        'español': 3.9,
        'Ed fisica': 2.6,
        'sociales': 2.2,
        'Promedio': 2.8,
        'Estado': 'reprobado'
    },
        
    {
        'id': 2,
        'matematicas': 2.5,
        'español': 3.9,
        'Ed fisica': 4.6,
        'sociales': 4.3,
        'Promedio': 3.8,
        'Estado': 'aprobado'
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
    
    
@app.get('/ca/', tags=['Notas'])
def get_calificacion(Estado: str): 
    for calificacion in notas:
        if calificacion['Estado'] == Estado.lower():
            return calificacion

    return []


@app.post('/notas', tags=['Notas'])
def create_movie():
    pass