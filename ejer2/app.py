from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = "b7f9e2c4d8a1f0g3h6j9k2l5m8n0p4q"

@app.route("/")
def index():
    if "items" not in session:
        session["items"] = []
    total_general = round(sum(item["total"] for item in session["items"]), 2)
    return render_template("index.html", items=session["items"], total=total_general)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add", methods=['POST'])
def add_item():
    if "items" not in session:
        session["items"] = []
    producto = request.form.get("producto")
    precio = float(request.form.get("precio", 0))
    cantidad = int(request.form.get("cantidad", 1))
    item = {
        "id": len(session["items"]) + 1,
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad,
        "total": precio * cantidad
    }
    
    session['items'].append(item)
    session.modified = True
    return redirect("/")
    

@app.route("/vaciar_carrito", methods=['GET'])
def clear_session():
    session.clear()
    return redirect("/")

@app.route("/eliminar/<int:id>", methods=['GET'])
def eliminar_producto(id):
    if 'items' in session:
        session['items'] = [item for item in session['items'] if item['id'] != id]
        session.modified= True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    