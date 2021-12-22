from flask import Flask,render_template,request,redirect
from pymysql import NULL
import controllers.controlador_login as controlador

app = Flask(__name__)
@app.route('/route_name')
def method_name():
    pass

@app.route("/")
@app.route("/home_login")
def inicio():
#   juegos = controlador_juegos.obtener_juegos()
    return render_template("Login.html")

@app.route("/loguearse",methods=["POST"])
def loguearse():
    correo = request.form["correo"]
    contraseña = request.form["contraseña"]
    lista = controlador.obtener_usuario(contraseña,correo)
    #validamos la existencia del arreglo lista, si retorna o no un valor
    if(lista):
        return render_template("admin.html",lista=lista)
    else:
        return redirect("/home_login")
    

@app.route("/admin")
def admin(lista):
    return render_template("admin.html",lista=lista)

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
