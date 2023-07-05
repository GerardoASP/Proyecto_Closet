#Version 1.0
from flask import Blueprint, request

garments = Blueprint("garments",__name__,url_prefix="/api/v1/garments")

@garments.get("/")
def read_all():
    return "Reading all garments ... soon"

@garments.get("/<int:id>")
def read_one(id):
    return "Reading a garment ... soon"

@garments.post("/")
def create():
    return "Creating a garment ... soon"

@garments.put('/<int:id>')
@garments.patch('/<int:id>')
def update(id):
    return "Updating a garment ... soon"

@garments.delete("/<int:id>")
def delete(id):
    return "Removing a garment ... soon"

@garments.get("/search")
def read_for_aspect():
    return "Reading all garments for a aspect"

