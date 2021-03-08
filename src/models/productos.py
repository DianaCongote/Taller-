from src.config.db import DB

class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre, descripcion, precio_venta, ganancia, precio_compra, estado):
        cursor = DB.cursor()

        cursor.execute('insert into productos(nombre, descripcion, precio_venta, ganancia, precio_compra, estado) values(?,?,?,?,?,?)', (nombre, descripcion, precio_venta, ganancia, precio_compra, estado,))

        cursor.close()

    def editar(self, id, nombre, descripcion, precio_venta, ganancia, precio_compra, estado):
        cursor = DB.cursor()
        cursor.execute(""" UPDATE productos SET nombre = ?, descripcion = ?, precio_venta = ?, ganancia = ?, precio_compra = ?, estado = ?  WHERE id = ?""",(nombre, descripcion, precio_venta, ganancia, precio_compra, estado, id,))
        cursor.close()

    def eliminar(self, id):
        cursor = DB.cursor()
        cursor.execute("""DELETE FROM productos WHERE id = ? """,(id,))
        cursor.close()

