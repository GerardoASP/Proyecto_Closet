#version 1.1

#Importación de Librerias
from src.database import db, ma
from src.models.outfit_garment import OutfitGarment
from datetime import date,datetime

class Garment(db.Model):
    #Atributos
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(60),nullable=False)
    colour = db.Column(db.String(30),nullable=False)
    size = db.Column(db.String(3),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    outfit_garments_g = db.relationship('OutfitGarment', backref="owner")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    #Métodos
    def __init__(self, **fields):
        super().__init__(**fields)
        
    def __repr__(self) -> str:
        return f"Garment >>> {self.brand}"
    
class GarmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = Garment
        include_fk = True

user_schema = GarmentSchema()
users_schema = GarmentSchema(many=True)