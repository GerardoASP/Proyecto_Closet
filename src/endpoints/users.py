#Version 1.4
from flask import Blueprint, request

from http import HTTPStatus
import sqlalchemy.exc
import werkzeug
from datetime import datetime
from src.database import db
from src.models.user import User, user_schema, users_schema
#from src.models.user import some_function
users = Blueprint("users",__name__,url_prefix="/api/v1/users")

###############################CRUD BASICO##########################
#Endpoint que se encarga de listar todos los usuarios que se encuentran en la BD.
@users.get("/")
def read_all():
    users = User.query.order_by(User.name).all()
    return {"data": users_schema.dump(users)}, HTTPStatus.OK
#Endpoint que se encarga de mostrar la información de un usuario especifico a partir de su id.
@users.get("/<int:id>")
def read_one(id):
    user = User.query.filter_by(id=id).first()
    if(not user):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    return {"data": user_schema.dump(user)}, HTTPStatus.OK
#Endpoint que se encarga de crear un usuario en la BD.
@users.post("/")
def create():
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Post body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    date_birth_request = request.get_json().get("date_birth", None)
    date_birth_response = datetime.strptime(date_birth_request, '%Y-%m-%d').date()
    # User.id is auto increment! 
    user = User(name = request.get_json().get("name", None),
        password = request.get_json().get("password", None),
        email = request.get_json().get("email", None),
        date_birth = date_birth_response,
        type_document= request.get_json().get("type_document", None))

    try:
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST

    return {"data": user_schema.dump(user)}, HTTPStatus.CREATED

@users.put('/<int:id>')
@users.patch('/<int:id>')
def update(id):
    post_data = None
    try:
        post_data = request.get_json()
    except werkzeug.exceptions.BadRequest as e:
        return {"error": "Put body JSON data not found","message": str(e)}, HTTPStatus.BAD_REQUEST
    user = User.query.filter_by(id=id).first()
    if(not user):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    
    date_birth_request = request.get_json().get("date_birth", None)
    date_birth_response = datetime.strptime(date_birth_request, '%Y-%m-%d').date()
    
    user.name = request.get_json().get("name", user.name)
    user.password = request.get_json().get("password", user.password)
    user.email = request.get_json().get("email", user.email)
    user.date_birth =  date_birth_response
    user.type_document = request.get_json().get("type_document", user.type_document)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Invalid resource values","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": user_schema.dump(user)}, HTTPStatus.OK

@users.delete("/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    if(not user):
        return {"error": "Resource not found"}, HTTPStatus.NOT_FOUND
    try:
        db.session.delete(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        return {"error": "Resource could not be deleted","message": str(e)}, HTTPStatus.BAD_REQUEST
    return {"data": ""}, HTTPStatus.NO_CONTENT

################################################################################

##########ENDPOINTS ADICIONALES#################################################
#Endpoint que se encarga de listar las prendas de un usuario especifico
@users.get("/<int:id>/garments")
def read_garments_of_user(id):
    return "Reading all garments of a user"
#Endpoint que se encarga de listar los conjuntos de ropa de un usuario especifico
@users.get("/<int:id>/outfits")
def read_outfits_of_user(id):
    return "Reading all outfits of a user"