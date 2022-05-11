from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_name',methods=['GET'])
def name(): 
  
    name_choice = random.choice(["High Elf", "Human", "Dwarf","Barbarian", "Wood Elf", "Erudite", "Half Elf","Halfling" ])

    
    return Response(f"{name_choice}", mimetype="text/plain")

   