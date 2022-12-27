#./app/app.py

from bson.json_util import dumps
from pymongo import MongoClient
from bson import ObjectId
from flask import Flask, Response, request, jsonify, render_template
from flask_restful import Resource, Api
import json

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

# *********************************************************
# *                         P 2.1                         *
# *********************************************************

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_de/<cocktail>')
def recetas_de(cocktail):
    cocktail = cocktail.replace('_', '-')
    # Expresión regular para buscar palabras de forma case insentive
    regex = '(?i)' + cocktail
    # Le indico a la query que va a usar una expresión regular
    myquery = { 'slug': {'$regex': regex} }
    recipe = db.recipes.find(myquery)
    
    resJson = dumps(recipe)
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_con/<searched_ingredient>')
def recetas_con(searched_ingredient):
    searched_ingredient = searched_ingredient.replace('_', ' ')
    regex = '(?i)' + searched_ingredient
    myquery = { 'ingredients': { '$elemMatch' : { 'name': { '$regex': regex } } } }
    recipes = db.recipes.find(myquery)
    
    resJson = dumps(recipes)
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_compuestas_de/<int:number>/ingredientes')
def recetas_compuestas_ingredientes(number):
    myquery = { 'ingredients': { '$size' : number } }
    recipes = db.recipes.find(myquery)
    
    resJson = dumps(recipes)
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_compuestas_de/<int:number>/instrucciones')
def recetas_compuestas_instrucciones(number):
    myquery = { 'instructions': { '$size' : number } }
    recipes = db.recipes.find(myquery)
    
    resJson = dumps(recipes)
    return Response(resJson, mimetype='application/json')

# *********************************************************
# *                         P 2.2                         *
# *********************************************************

def find(id):
    return db.recipes.find_one({'_id':ObjectId(id)})

# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        
        # Coge el parámetro de la URL
        searched_ingredient = request.args.get('con')

        if searched_ingredient:
            searched_ingredient = searched_ingredient.replace('_', ' ')
            regex = '(?i)' + searched_ingredient
            myquery = { 'ingredients': { '$elemMatch' : { 'name': { '$regex': regex } } } }
            recipes = db.recipes.find(myquery)
            
            resJson = dumps(recipes)
            return Response(resJson, mimetype='application/json')
        else:
            lista = []
            buscados = db.recipes.find().sort('name')
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)
    
    if request.method == 'POST':
        creado = db.recipes.insert_one(json.loads(request.data))
        resJson = dumps(find(creado.inserted_id))
        return Response(resJson, mimetype='application/json')
    
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    
    buscado = find(id)
    
    if buscado:
        if request.method == 'GET':
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            resJson = dumps(buscado)
            return Response(resJson, mimetype='application/json')
            
        if request.method == 'PUT':
            db.recipes.update_one({'_id':ObjectId(id)}, { "$set": json.loads(request.data) })
            buscado = find(id)
            buscado['_id'] = str(buscado['_id'])
            resJson = dumps(buscado)
            return Response(resJson, mimetype='application/json')
            
        if request.method == 'DELETE':
            db.recipes.delete_one(buscado)
            return  jsonify({"_id": str(buscado['_id'])})
            
    return jsonify({'error':'Not found'}), 404


# ********************************************************
# *                        API V2                        *
# ********************************************************

api = Api(app)

class Recipes(Resource):
    def get(self):
        # Coge el parámetro de la URL
        searched_ingredient = request.args.get('con')
        if searched_ingredient:
            searched_ingredient = searched_ingredient.replace('_', ' ')
            regex = '(?i)' + searched_ingredient
            myquery = { 'ingredients': { '$elemMatch' : { 'name': { '$regex': regex } } } }
            recipes = db.recipes.find(myquery)
            
            resJson = dumps(recipes)
            return Response(resJson, mimetype='application/json')
        else:
            lista = []
            buscados = db.recipes.find().sort('name')
            for recipe in buscados:
                recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
                lista.append(recipe)
            return jsonify(lista)
        
    def post(self):
        creado = db.recipes.insert_one(json.loads(request.data))
        creado = find(creado.inserted_id)
        resJson = dumps(creado)
        return Response(resJson, mimetype='application/json')
    
class RecipesWithID(Resource):
    def get(self, id):
        buscado = find(id)
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            resJson = dumps(buscado)
            return Response(resJson, mimetype='application/json')
        
        return {'error':'Not found'}, 404
    
    def put(self, id):
        buscado = find(id)
        if buscado:
            db.recipes.update_one({'_id':ObjectId(id)}, { "$set": json.loads(request.data) })
            buscado = find(id)
            buscado['_id'] = str(buscado['_id'])
            resJson = dumps(buscado)
            return Response(resJson, mimetype='application/json')
        
        return {'error':'Not found'}, 404
            
    def delete(self, id):
        buscado = find(id)
        if buscado:
            db.recipes.delete_one(buscado)
            return  jsonify({"_id": str(buscado['_id'])})
        
        return {'error':'Not found'}, 404

@app.route("/")
def index():
    return render_template('index.html')
        
api.add_resource(Recipes, '/api/v2/recipes')
api.add_resource(RecipesWithID, '/api/v2/recipes/<string:id>')