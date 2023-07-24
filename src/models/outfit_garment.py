#version 1.1

#Importación de Librerias
from src.database import db, ma
from datetime import date,datetime

class OutfitGarment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    source = db.Column(db.String(60),nullable=False)
    outfit_id = db.Column(db.Integer,db.ForeignKey('outfit.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    garment_id = db.Column(db.Integer,db.ForeignKey('garment.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    start_date = db.Column(db.DateTime,nullable=False)
    end_date = db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def __init__(self, **fields):
        super().__init__(**fields)
        
    def __repr__(self) -> str:
        return f"OutfitGarment >>> {self.source}"

class OutfitGarmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = OutfitGarment
        include_fk = True

user_schema = OutfitGarment()
users_schema = OutfitGarment(many=True)