#version 1.2

#Importación de Librerias
from src.database import db, ma
from datetime import date,datetime
from sqlalchemy.orm import validates
import re
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
    
    #Sección de Validaciones
    
    @validates('id')
    def validate_id(self, key, value):
        if not value:
            raise AssertionError('No id provided')
        if not re.compile("^[-+]?[0-9]+$", value):
            raise AssertionError('The value must be an integer')
        if value <= 0:
            raise AssertionError('id invalid')
        if OutfitGarment.query.filter(OutfitGarment.id == value).first():
            raise AssertionError('Id is already in use') 
        
        return value
    
    @validates('source')
    def validate_name_user(self,key,value):
        if not value:
            raise AssertionError('No source provided')
        if not value.isalnum():
            raise AssertionError('source value must be alphanumeric')
        if len(value) < 5 or len(value) > 60:
            raise AssertionError('source  must be between 5 and 60 characters')

        return value

class OutfitGarmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields
        model = OutfitGarment
        include_fk = True

outfit_garment_schema = OutfitGarmentSchema()
outfits_garments_schema = OutfitGarmentSchema(many=True)

