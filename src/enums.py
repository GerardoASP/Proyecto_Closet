#version 1.4

import enum
class TypeDocument(enum.Enum):
    cedula = "c.c"
    tarjeta_identidad = "t.i"
    cedula_extranjeria = "c.e"

class DailyRecommendation(enum.Enum):
    CASUAL = 'Casual'
    FORMAL = 'Formal'
    DEPORTIVO = 'Deportivo'
    TRABAJO = 'Trabajo'
    FIESTA = 'Fiesta'