#version 1.1
from sqlalchemy import Enum

class TypeDocument(Enum):
    cedula = 'c.c'
    tarjeta_identidad = 't.i'
    cedula_extranjeria = 'c.e'

class DailyRecommendation(Enum):
    CASUAL = 'Casual'
    FORMAL = 'Formal'
    DEPORTIVO = 'Deportivo'
    TRABAJO = 'Trabajo'
    FIESTA = 'Fiesta'