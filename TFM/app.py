from flask import Flask, render_template, request, flash

#"Cometer este error podria ser el equivalente en desarrollo web a dejar la llave debajo del tapete de entrada a una casa: cualquiera la encuentra si sabe donde buscar."""

app = Flask(__name__)
app.secret_key = "JFUJLUMCS_111"
rewardComplete= "ENHORABUENA! Esta es tu pieza: "
error = "La clave ingresada no fue correcta."
ingresar = "Responde la clave en el campo arriba para obtener tu recompensa!"
ejercicios = []
datos_exito = []
with open("static/ejercicios/Ejercicios.txt", "r") as file:
	for line in file:
		ejercicios.append(line.rstrip())
with open("static/ejercicios/Datos_Exito.txt", "r") as file:
	for line in file:
		datos_exito.append(line.rstrip())

def loader(index, index_datos, num_datos, id_name, id_number, clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		for i in range(0, num_datos):
			flash(datos_exito[index_datos + i], "assignment")	
		flash(rewardComplete + "3f", "reward")
	elif data != None:
		flash(ejercicios[index], "assignment")
		flash(ingresar, "waiting")
		flash(error, "error")
	else:
		flash(ejercicios[index], "assignment")
		flash(ingresar, "waiting")
	return id_name+id_number+".html"

def reward_state(clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		return "img/chest_open_bgl.png"
	else:
		return "img/chest_closed_bgl.png"


#@app.route("/")
#def landing():
	#return render_template(loader(0, "fugas", "1"), chest=reward_state())

@app.route("/fugas1", methods=["POST", "GET"])
def fugas1():
	clave="848d85f801e989c68a4df01d9d4c1e9e"
	return render_template(loader(0, 0, 3, "fugas", "1", clave), chest=reward_state(clave))

@app.route("/fugas2", methods=["POST", "GET"])
def fugas2():
	clave="d82c8d1619ad8176d665453cfb2e55f0"
	return render_template(loader(1, 3, 0, "fugas", "2", clave), chest=reward_state(clave))