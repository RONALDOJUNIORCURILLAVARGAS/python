from os import name
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def homepage():
    title="Home"
    orientacion="Bienvenidos a la pagina principal"
    return render_template("index.html",title=title,text=orientacion)

@app.route('/about')
def about():
    title="ABOUT"
    names =["ronaldo","Tatiane","Lucifero","Reyim"]
    return render_template("about.html",names=names,title=title)
    
@app.route('/stor')
def store():
    title="STORE"
    nombre_tienda="rudeos"
    return render_template("store.html",nombre=nombre_tienda,title=title)


if __name__=='__main__':
    app.run(debug=True)