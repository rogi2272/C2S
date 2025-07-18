# ============================
# server/api.py
# ============================

from fastapi import FastAPI, Query
from typing import Optional
from database.db import get_session
from database.models import Veiculo
from server.handlers import aplicar_filtros

app = FastAPI()

@app.get("/veiculos")
def buscar_veiculos(
    marca: Optional[str] = Query(None),
    modelo: Optional[str] = Query(None),
    ano: Optional[int] = Query(None),
    motorizacao: Optional[float] = Query(None),
    combustivel: Optional[str] = Query(None),
    cor: Optional[str] = Query(None),
    quilometragem: Optional[int] = Query(None),
    portas: Optional[int] = Query(None),
    transmissao: Optional[str] = Query(None),
    preco_max: Optional[float] = Query(None),
):
    filtros = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "motorizacao": motorizacao,
        "combustivel": combustivel,
        "cor": cor,
        "quilometragem": quilometragem,
        "portas": portas,
        "transmissao": transmissao,        
        "preco_max": preco_max,
    }
    session = get_session()
    query = session.query(Veiculo)
    query = aplicar_filtros(query, filtros, Veiculo)

    resultados = query.all()
    return [
        {
            "marca": v.marca,
            "modelo": v.modelo,
            "ano": v.ano,
            "cor": v.cor,
            "quilometragem": v.quilometragem,
            "preco": v.preco,
        } for v in resultados
    ]