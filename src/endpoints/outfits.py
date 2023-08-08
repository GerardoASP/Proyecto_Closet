#Version 1.5
from flask import Blueprint, request

from http import HTTPStatus
import sqlalchemy.exc
import werkzeug
from datetime import datetime
from src.database import db
from src.models.outfit import Outfit,outfit_schema,outfits_schema

outfits = Blueprint("outfits",__name__,url_prefix="/api/v1/outfits")

###############################CRUD BASICO##########################
#Endpoint que se encarga de listar todos los conjuntos de ropa que se encuentran en la BD.
@outfits.get("/")
def read_all():
    outfits = Outfit.query.order_by(Outfit.occasion).all()
    return {"data": outfits_schema.dump(outfits)}, HTTPStatus.OK
#Endpoint que se encarga de mostrar la información de un conjunto de ropa en especifico a partir de su id.
@outfits.get("/<int:id>")
def read_one(id):
    outfit = Outfit.query.filter_by(id=id).first()
    if(not outfit):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    return {"data": outfit_schema.dump(outfit)}, HTTPStatus.OK
#Endpoint que se encarga de crear un conjunto de ropa en la BD.
@outfits.post("/")
def create():
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Post body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    # Outfit.id is auto increment! 
    outfit = Outfit(occasion = request.get_json().get("occasion", None),
        user_id = request.get_json().get("user_id", None),
        daily_recommendation= request.get_json().get("daily_recommendation", None))

    try:
        db.session.add(outfit)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST

    return {"data": outfit_schema.dump(outfit)}, HTTPStatus.CREATED
#Endpoint que se encarga de actualizar uno o varios datos de un conjunto de ropa en especifico. Esto en base al id.
@outfits.put('/<int:id>')
@outfits.patch('/<int:id>')
def update(id):
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Put body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    outfit = Outfit.query.filter_by(id=id).first()
    if(not outfit):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    
    outfit.occasion = request.get_json().get("occasion", outfit.occasion)
    outfit.user_id = request.get_json().get("user_id", outfit.user_id)
    outfit.daily_recommendation = request.get_json().get("daily_recommendation", outfit.daily_recommendation)
    
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": outfit_schema.dump(outfit)}, HTTPStatus.OK
#Endpoint que se encarga de eliminar un conjunto de ropa de la BD
@outfits.delete("/<int:id>")
def delete(id):
    outfit = Outfit.query.filter_by(id=id).first()
    if(not outfit):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    try:
        db.session.delete(outfit)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Resource could not be deleted","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": ""}, HTTPStatus.NO_CONTENT

################################################################################