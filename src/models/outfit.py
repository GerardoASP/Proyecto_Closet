#version 1.2

#Importación de Librerias
from src.database import db, ma
from src.models.outfit_garment import OutfitGarment
from src.enums import DailyRecommendation
from datetime import date,datetime

from sqlalchemy.orm import validates
import re

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
    
    #Sección de Validaciones
    
    @validates('id')
    def validate_id(self, key, value):
        if not value:
            raise AssertionError('No id provided')
        if not re.compile("^[-+]?[0-9]+$", value):
            raise AssertionError('The value must be an integer')
        if value <= 0:
            raise AssertionError('id invalid')
        if Outfit.query.filter(Outfit.id == value).first():
            raise AssertionError('Id is already in use') 
        
        return value
    
    @validates('occasion')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No occasion provided')
        if not value.isalnum():
            raise AssertionError('occasion value must be alphanumeric')
        if len(value) < 5 or len(value) > 60:
            raise AssertionError('occasion  must be between 5 and 60 characters')

        return value
    
    @validates('daily_recommendation')
    def validate_rol_user(self, key, value):
        allowed_values = ["Casual", "Formal", "Deportivo","Trabajo","Fiesta"]
        if not value:
            raise AssertionError('No daily_recommendation')
        if value not in allowed_values:
            raise ValueError('El valor del campo "daily_recommendation" no es válido. Los valores permitidos son "Casual", "Formal", "Deportivo","Trabajo","Fiesta" ')
        return value
    
    @validates('user_id')
    def validate_id(self, key, value):
        if not value:
            raise AssertionError('No user_id')
        if not re.compile("^[-+]?[0-9]+$", value):
            raise AssertionError('The value must be an integer')
        if value <= 0:
            raise AssertionError('user_id invalid')
        if not User.query.filter_by(id=value).first():  # Verifica si el usuario con el "user_id" especificado existe
            raise AssertionError('User with the specified user_id does not exist')
        return value
    
class OutfitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = Outfit
        include_fk = True

user_schema = OutfitSchema()
users_schema = OutfitSchema(many=True)

#Posible solución a la importación ciclica 
from src.models.user import User