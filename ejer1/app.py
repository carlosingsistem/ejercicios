from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = "b7f9e2c4d8a1f0g3h6j9k2l5m8n0p4q"

@app.route("/", methods=['GET','POST'])
def carrito():
    if 'productos' not in session:
        session['productos'] = []
    if request.method == 'POST':
        producto = request.form['name_pro']
        if producto:
            session["productos"].append(producto)
            session.modified = True
        return redirect("/")
    return render_template('index.html', productos=session['productos'])

@app.route("/vaciar_carrito")
def clear_session():
    session.clear()
    return render_template('index.html', msg="Se limpio la session")

@app.route("/pop/<int:index>")
def pop(index):
    if len(session['productos']) != 0:
        session['productos'].pop(index)
        session.modified = True
        return redirect("/")
    return render_template('index.html', productos=session['productos'])

if __name__ == "__main__":
    app.run(debug=True)
    