from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# "Base de datos" en memoria - ¡Súper simple!
tareas = [
    {"id": 1, "titulo": "Aprender Flask", "completada": False},
    {"id": 2, "titulo": "Practicar HTML", "completada": True}
]

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": request.form['titulo'],
        "completada": False
    }
    tareas.append(nueva_tarea)
    return redirect('/')

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = not tarea['completada']
            break
    return redirect('/')

@app.route('/api/tareas')
def api_tareas():
    return jsonify(tareas)

if __name__ == '__main__':
    app.run(debug=True)