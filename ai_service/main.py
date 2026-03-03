from fastapi import FastAPI
from pydantic import BaseModel
from analytics.predictor import AIHandler

app = FastAPI(title="AI Analytics Service")

class AnalisisRequest(BaseModel):
    historial: list[dict] # type: ignore

@app.post("/predict")
def predict_wear(data: AnalisisRequest): # type: ignore
    resultado = AIHandler.calcular_proyeccion(data.historial) # type: ignore
    
    return resultado # type: ignore

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)