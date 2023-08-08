#Version 1.6
from flask import Blueprint, request

from http import HTTPStatus
import sqlalchemy.exc
import werkzeug
from datetime import datetime
from src.database import db
from src.models.garment import Garment,garment_schema,garments_schema

garments = Blueprint("garments",__name__,url_prefix="/api/v1/garments")
###############################CRUD BASICO##########################
#Endpoint que se encarga de listar todas las prendas que se encuentran en la BD.
@garments.get("/")
def read_all():
    garments = Garment.query.order_by(Garment.brand).all()
    return {"data": garments_schema.dump(garments)}, HTTPStatus.OK
#Endpoint que se encarga de mostrar la información de una ropa en especifico a partir de su id.
@garments.get("/<int:id>")
def read_one(id):
    garment = Garment.query.filter_by(id=id).first()
    if(not garment):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    return {"data": garment_schema.dump(garment)}, HTTPStatus.OK
#Endpoint que se encarga de crear un registro de una ropa en la BD.
@garments.post("/")
def create():
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Post body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    # Garment.id is auto increment! 
    garment = Garment(brand = request.get_json().get("brand", None),
        colour = request.get_json().get("colour", None),
        size = request.get_json().get("size", None),
        user_id = request.get_json().get("user_id", None))

    try:
        db.session.add(garment)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST

    return {"data": garment_schema.dump(garment)}, HTTPStatus.CREATED
#Endpoint que se encarga de actualizar uno o varios datos de una ropa en especifico. Esto en base al id.
@garments.put('/<int:id>')
@garments.patch('/<int:id>')
def update(id):
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Put body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    garment = Garment.query.filter_by(id=id).first()
    if(not garment):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    
    garment.brand = request.get_json().get("brand", garment.brand)
    garment.colour = request.get_json().get("colour", garment.colour)
    garment.size = request.get_json().get("size", garment.size)
    garment.user_id = request.get_json().get("user_id", garment.user_id)
    
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": garment_schema.dump(garment)}, HTTPStatus.OK

@garments.delete("/<int:id>")
def delete(id):
    garment = Garment.query.filter_by(id=id).first()
    if(not garment):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    try:
        db.session.delete(garment)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Resource could not be deleted","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": ""}, HTTPStatus.NO_CONTENT
###############################################################
##########ENDPOINTS ADICIONALES################################
@garments.get("/search")
def read_for_aspect():
    return "Reading all garments for a aspect"

