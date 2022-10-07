#./app/app.py

from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, Response

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

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
