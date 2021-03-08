from src import app
from src.models.productos import ProductosModel
from flask import render_template, request, redirect, url_for

@app.route('/productos')
def productos():
    productosModel = ProductosModel()
    productos=productosModel.traerTodos()


    return render_template('productos/index.html', productos=productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    #esta funcion me sirve para mostrar el formulario de creacion
    #y tambien me sirve para crear un nuevo producto
    #estos pasos se identifican con los metodos
    if request.method == 'GET':
        #mostramos el formulario de creacion
        return render_template('productos/crear.html')
        #campo a recuperar
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
    precio_compra = request.form.get('precio_compra')
    estado = request.form.get('estado')
    ganancia = request.form.get('ganancia')

    productosModel= ProductosModel()

    productosModel.crear(nombre, descripcion, precio_venta, ganancia, precio_compra, estado)


    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    if request.method == 'GET':
        #mostramos el formulario de creacion
        return render_template('productos/editar.html')
        #campo a recuperar
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
    precio_compra = request.form.get('precio_compra')
    estado = request.form.get('estado')
    ganancia = request.form.get('ganancia')

    productosModel= ProductosModel()

    productosModel.editar(id, nombre, descripcion, precio_venta, ganancia, precio_compra, estado)


    return redirect(url_for('productos'))

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):

    productosModel= ProductosModel()

    productosModel.eliminar(id)


    return redirect(url_for('productos'))

    