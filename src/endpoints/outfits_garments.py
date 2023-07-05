#Version 1.0
from flask import Blueprint, request

outfits_garments = Blueprint("outfits_garments",__name__,url_prefix="/api/v1/outfits_garments")

@outfits_garments.get("/")
def read_all():
    return "Reading al outfits_garments ... soon"

@outfits_garments.get("/<int:id>")
def read_one(id):
    return "Reading a outfit_garment ... soon"

@outfits_garments.post("/")
def create():
    return "Creating a outfit_garment ... soon"

@outfits_garments.put('/<int:id>')
@outfits_garments.patch('/<int:id>')
def update(id):
    return "Updating a outfit_garment ... soon"

@outfits_garments.delete("/<int:id>")
def delete(id):
    return "Removing a outfit_garment ... soon"

@outfits_garments.get("/outfits_in_use")
def read_outfits_in_use():
    return "AAAAAAAAAOUTFIT"

@outfits_garments.get("/garments_in_use")
def read_garments_in_use():
    return "AAAAAAAAAGARMENT"

@outfits_garments.get("/outfits/<int:id_outfit>/garments/<int:id_garment>/usage_dates")
def obtain_dates(id_outfit,id_garment):
    return "these dates"

@outfits_garments.get("/outfits/<int:id_outfit>/garments")
def read_garments_of_outfit(id_outfit):
    return "garments of the outfit"