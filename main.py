from fastapi import FastAPI, Body


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
    
    resultado = []
    
    for calificacion in notas:
        if calificacion['Estado'].lower() == Estado.lower():
            resultado.append(calificacion)

    return resultado



@app.post('/notas', tags=['Notas'])
def create_nota(
                id: int = Body(), 
                matematicas: float = Body(),
                español: float = Body(),
                Ed_fisica: float = Body(),
                sociales: float = Body(),
                Promedio: float = Body(),
                Estado: str = Body()
                ):
    
    notas.append({
        'id': id,
        'matematica': matematicas,
        'Epañol': español,
        'Ed_Fisica': Ed_fisica,
        'Sociales': sociales,
        'Promedio': Promedio,
        'Estado': Estado,
    })
    
    return notas 