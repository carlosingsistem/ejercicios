from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = "b7f9e2c4d8a1f0g3h6j9k2l5m8n0p4q"

# GET: mostrar lista de contactos
@app.route("/")
def listar_contactos():
    if "contactos" not in session:
        session["contactos"] = []
    return render_template("index.html", contactos=session["contactos"])

# POST: crear nuevo contacto
@app.route("/crear")
def crear_contacto():
    return render_template("crear.html")

@app.route("/save", methods=["POST"])
def save():
    if "contactos" not in session:
        session["contactos"] = []
    nuevo = {
        "id": len(session.get("contactos")) + 1,
        "nombre": request.form.get("nombre"),
        "correo": request.form.get("correo"),
        "celular": request.form.get("celular")
    }
    session.setdefault("contactos", []).append(nuevo)
    session.modified = True
    return redirect(url_for("listar_contactos"))

# PUT: actualizar contacto
@app.route("/editar/<int:id>")
def editar_contacto(id):
    contacto = next(c for c in session["contactos"] if c['id'] == id)
    return render_template("editar.html", contacto=contacto)

@app.route("/update", methods=["POST"])
def actualizar_contacto():
    id = int(request.form.get("id"))
    nombre = request.form.get("nombre")
    correo= request.form.get("correo")
    celular = request.form.get("celular")
    for c in session['contactos']:
        if c["id"] == id:
            c["nombre"] = nombre
            c["correo"] = correo
            c["celular"] = celular
            session.modified = True
            break
    return redirect("/")

# DELETE: eliminar contacto
@app.route("/eliminar/<int:id>")
def eliminar_contacto(id):
    session["contactos"] = [c for c in session.get("contactos", []) if c["id"] != id]
    session.modified = True
    return redirect("/")

@app.route("/vaciar")
def clear_session():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    