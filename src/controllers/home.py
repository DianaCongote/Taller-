from flask import render_template, request, redirect, url_for
from src import app
from src.config.db import CONEXION_PATH, mostrarbd
from os import path
import json
import src.config.globals as globals


@app.route('/')
def index():
    if(globals.DB == False):
        return render_template('instalacion.html')
    
    return render_template('index.html')

@app.route('/instalacion', methods=['POST'])
def muestra():
    mostrarbd()
