import requests

class AIClient:
    URL_IA = "http://127.0.0.1:8001/predict"
    
    @staticmethod
    def solicitar_analisis(datos_mediciones: list): # type: ignore
        try:
            # Enviamos el historial al microservicio de IA
            response = requests.post(AIClient.URL_IA, json={"historial": datos_mediciones}) # type: ignore
            if response.status_code == 200:
                return response.json()
            return {"error": "Servicio de IA no disponible"}
        except Exception as e:
            return {"error": str(e)}