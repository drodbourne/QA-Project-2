from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_class',methods=['GET'])
def name(): 
    class_choice = random.choice(["Cleric", 
    "Wizard", 
    "Rogue", 
    "Warrior",
    "Mage",
    "Ranger",
    "Enchanter",
    "Paladin",
    "Druid", 
    "Monk", 
    "Bard" ])
        
    return Response(f"{class_choice}", mimetype="text/plain")
