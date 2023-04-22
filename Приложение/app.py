import flask
from flask import render_template
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
import gunicorn

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if flask.request.method == 'POST':
        with open('my_model1.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        angle = int(flask.request.form['angle'])
        step = float(flask.request.form['step'])
        density = float(flask.request.form['density'])
        elasticity_module = float(flask.request.form['elasticity_module'])
        hardener_quantity = float(flask.request.form['hardener_quantity'])
        epoxy_group = float(flask.request.form['epoxy_group'])
        temperature = float(flask.request.form['temperature'])
        surface_density = float(flask.request.form['surface_density'])      
        elasticity_module2 = float(flask.request.form['elasticity_module2'])
        tensile_strength = float(flask.request.form['tensile_strength'])
        resin_consumption = float(flask.request.form['resin_consumption'])
        patch_density = float(flask.request.form['patch_density'])

        y_pred = loaded_model.predict([[angle, step, patch_density, density, elasticity_module, hardener_quantity, epoxy_group, temperature,
                                        surface_density, elasticity_module2, tensile_strength, resin_consumption]])
        
        return render_template('main.html', result = y_pred)

 
app.run()   