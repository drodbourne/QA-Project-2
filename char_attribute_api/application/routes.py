from application import app 
from flask import Flask, request, Response 



@app.route('/get_attribute', methods=['POST'])
def attribute(): 
    
    char_name = request.get_json()["Name"]
    char_class = request.get_json()["Class"]
    
    char_weapon = {"Ranger" : "Bow & Arrow", 
    "Cleric" : "Healing Spells", 
    "Druid" : "Ice Spells", 
    "Wizard" : "Fire Spells", 
    "Mage" : "Elemental Pet", 
    "Enchanter" : "Charm Spells", 
    "Rogue" : "Dual Wield Daggers",
    "Monk" : "Dual Wield Clubs", 
    "Bard":"Musical Instruments", 
    "Paladin":"Sword & Shield",
    "Warrior":"Two Handed Sword"}

    char_attribute = {"Half Elf" : "+6", 
    "Wood Elf" : "+8", 
    "Dwarf" : "+6", 
    "High Elf" : "+9", 
    "Erudite" : "+7", 
    "Halfling" : "+4", 
    "Human":"+5",
    "Barbarian":"+4"}
    
    get_attribute = f"{char_attribute[char_name]} to {char_weapon[char_class]}"

    return Response(get_attribute, mimetype='text/plain')
