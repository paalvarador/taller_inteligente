class AIHandler:
    @staticmethod
    def calcular_proyeccion(historial_mediciones: list, limite_critico: float = 2.0): # type: ignore
        """
        historial_mediciones: lista de dicts [{'km': 1000, 'valor': 10.0}, ...]
        """
        if len(historial_mediciones) < 2: # type: ignore
            return {"error": "Insuficientes datos para analizar"}
        
        # Ordenar por kilometraje
        h = sorted(historial_mediciones, key=lambda x: x['km']) # type: ignore
        
        p1 = h[0] # type: ignore
        p_ultima = h[-1] # type: ignore
        
        delta_km = p_ultima['km'] - p1['km'] # type: ignore
        delta_desgaste = p1['valor'] - p_ultima['valor'] # type: ignore
        
        if delta_km <= 0 or delta_desgaste <= 0:
            return {"error": "Desgaste no detectable o datos inconsistentes"}
        
        tasa_desgaste = delta_desgaste / delta_km # type: ignore
        mm_para_limite = p_ultima['valor'] - limite_critico # type: ignore
        
        km_restantes = int(mm_para_limite / tasa_desgaste) if tasa_desgaste > 0 else 0 # type: ignore
        
        return {
            "estado_actual": p_ultima['valor'],
            "tasa_desgaste_por_km": tasa_desgaste,
            "km_vida_util_restante": max(0, km_restantes),
            "alerta": "CRÍTICO" if p_ultima['valor'] <= limite_critico else "OK"
        } # type: ignore