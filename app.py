from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def index_page():
    """Renders html template that includes some JS - NOT PART OF JSON API!"""
    # cupcakes = Cupcake.query.all()
    # return render_template("index.html", cupcakes = cupcakes)
    
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

# *****************************
# RESTFUL TODOS JSON API
# *****************************

@app.route("/api/cupcakes")
def list_cupcakes():
    """return json with all cupcakes"""
    all_cupcake = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcake)


@app.route("/api/cupcakes/<int:cupcake.id>")
def single_cupcake():
    """Returns JSON for one todo in particular"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=['POST'])
def create_cupcake():
    """Creates a new cupcake and returns JSON of that created cupcake"""
    new_cupcake = Cupcake(flavor=request.json("flavor"), size= request.json("size"), rating=request.json("rating"), 
                          image= request.json("image"))
    db.session.add(new_cupcake)
    db.session.commit()
    
    response_json = jsonify(cupcake = new_cupcake.serialize())
    return (response_json, 201)


@app.route("/api/cupcakes/<int:cupcake.id>", method=['PATCH'])
def update_cupcake(id):
    """Updates a particular cupcale and responds w/ JSON of that updated cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake.id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = 'cupcake deleted!')