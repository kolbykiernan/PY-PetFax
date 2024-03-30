from flask import (Blueprint, render_template)
import json

pets =json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<pet_id>')
def show(pet_id):
    pet_id = int(pet_id)
    if pet_id > 0 and pet_id <= len(pets):
        pet_index = pet_id - 1
    return render_template('show.html', pet=pets[pet_index])
