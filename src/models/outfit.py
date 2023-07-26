#version 1.1

#Importación de Librerias
from src.database import db, ma
from src.models.outfit_garment import OutfitGarment
from src.enums import DailyRecommendation
from datetime import date,datetime

class Outfit(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    occasion = db.Column(db.String(60),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    daily_recommendation = db.Column(db.Enum(DailyRecommendation),nullable=False,default=DailyRecommendation.CASUAL)
    outfit_garments_o = db.relationship('OutfitGarment', backref="owner")
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def __init__(self, **fields):
        super().__init__(**fields)
        
    def __repr__(self) -> str:
        return f"Outfit >>> {self.occasion}"

class OutfitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = Outfit
        include_fk = True

user_schema = OutfitSchema()
users_schema = OutfitSchema(many=True)