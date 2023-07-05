#Version 1.0
from flask import Blueprint, request

users = Blueprint("users",__name__,url_prefix="/api/v1/users")

@users.get("/")
def read_all():
    return "Reading all users ... soon"

@users.get("/<int:id>")
def read_one(id):
    return "Reading a user ... soon"

@users.post("/")
def create():
    return "Creating a user ... soon"

@users.put('/<int:id>')
@users.patch('/<int:id>')
def update(id):
    return "Updating a user ... soon"

@users.delete("/<int:id>")
def delete(id):
    return "Removing a user ... soon"

@users.get("/<int:id>/garments")
def read_garments_of_user(id):
    return "Reading all garments of a user"

@users.get("/<int:id>/outfits")
def read_outfits_of_user(id):
    return "Reading all outfits of a user"