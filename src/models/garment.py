#version 1.2

#Importación de Librerias
from src.database import db, ma
from src.models.outfit_garment import OutfitGarment
from datetime import date,datetime

from sqlalchemy.orm import validates
import re

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
    
    #Sección de Validaciones
    
    @validates('id')
    def validate_id(self, key, value):
        if not value:
            raise AssertionError('No id provided')
        if not re.compile("^[-+]?[0-9]+$", value):
            raise AssertionError('The value must be an integer')
        if value <= 0:
            raise AssertionError('id invalid')
        if Garment.query.filter(Garment.id == value).first():
            raise AssertionError('Id is already in use') 
        
        return value
    
    @validates('brand')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No brand provided')
        if not value.isalnum():
            raise AssertionError('brand value must be alphanumeric')
        if len(value) < 5 or len(value) > 60:
            raise AssertionError('brand  must be between 5 and 50 characters')

        return value
    
    @validates('colour')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No colour provided')
        if not value.isalnum():
            raise AssertionError('colour value must be alphanumeric')
        if len(value) < 5 or len(value) > 30:
            raise AssertionError('colour  must be between 5 and 30 characters')

        return value
    
    @validates('size')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No size provided')
        if not value.isalnum():
            raise AssertionError('size value must be alphanumeric')
        if len(value) >= 3:
            raise AssertionError('size  must be 3 or less characters')

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
    
class GarmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = Garment
        include_fk = True

user_schema = GarmentSchema()
users_schema = GarmentSchema(many=True)

#Posible solución a la importación ciclica 
from src.models.user import User