from fastapi import FastAPI
import uvicorn

app = FastAPI()

array = []

@app.post('/postdistancia')
def post_distancia(distancia: float):
    """
    Envia a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        array.append(distancia)
    except:
        return {401:'Bad Request'}
    else:
        return {200:'OK'}

@app.get('/getdistancia')
def get_distancia():
    """
    Obtem a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        return {"Sucesso": array[-1]}
    except:
        return {401:'Bad Request'}
