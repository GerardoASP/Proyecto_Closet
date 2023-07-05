#Version 1.0
from flask import Blueprint, request

outfits = Blueprint("outfits",__name__,url_prefix="/api/v1/outfits")

@outfits.get("/")
def read_all():
    return "Reading al outfits ... soon"

@outfits.get("/<int:id>")
def read_one(id):
    return "Reading a outfit ... soon"

@outfits.post("/")
def create():
    return "Creating a outfit ... soon"

@outfits.put('/<int:id>')
@outfits.patch('/<int:id>')
def update(id):
    return "Updating a outfit ... soon"

@outfits.delete("/<int:id>")
def delete(id):
    return "Removing a outfit ... soon"
