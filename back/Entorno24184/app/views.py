from flask import jsonify, request
from app.models import Pizza

def index() :
    return jsonify({'message': 'Hello World API Pizza_Francesco'})

def create_pizza():
    data = request.json
    new_pizza = Pizza(variedad=data['variedad'], ingredientes=data['ingredientes'], tamanio=data['tamanio'], precio_salon=float(data['precio_salon']), precio_delivery=float(data['precio_delivery']))
    new_pizza.save()
    return jsonify({'message': 'Pizza created successfully'}), 201

def get_all_pizzas():
    pizzas = Pizza.get_all()
    return jsonify([pizza.serialize() for pizza in pizzas])

def get_pizza(pizza_id):
    pizza = Pizza.get_by_id(pizza_id)
    if not pizza:
        return jsonify({'message': 'Pizza not found'}), 404
    return jsonify(pizza.serialize())

def update_pizza(pizza_id):
    pizza = Pizza.get_by_id(pizza_id)
    if not pizza:
        return jsonify({'message': 'Pizza not found'}), 404
    data = request.json
    pizza.variedad = data['variedad']
    pizza.ingredientes = data['ingredientes']
    pizza.tamanio = data['tamanio']
    pizza.precio_salon = float(data['precio_salon'])
    pizza.precio_delivery = float(data['precio_delivery'])
    pizza.save()
    return jsonify({'message': 'Pizza updated successfully'})

def delete_pizza(pizza_id):
    pizza = Pizza.get_by_id(pizza_id)
    if not pizza:
        return jsonify({'message': 'Pizza not found'}), 404
    pizza.delete()
    return jsonify({'message': 'Pizza deleted successfully'})

