
class Producto(object):
    """
    Clase que permite crear un producto.
    """

    iva = 0.15
    def __init__(self, codigo:str, nombre:str, precio:float, stock:int=0, costo:float=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__proveedor = 'N/D'
        self.__costo = costo

    @property
    def codigo(self):
        return self.__codigo

    # @codigo.setter
    # def codigo(self, nuevo_codigo):
    #     self.__codigo = nuevo_codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError('Precio no valido')
        self.__precio = nuevo_precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock <= 0:
            raise ValueError('Stock no valido')
        self.__stock = nuevo_stock

    @property
    def proveedor(self):
        return self.__proveedor

    @proveedor.setter
    def proveedor(self, nuevo_proveedor):
        self.__proveedor = nuevo_proveedor

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, nuevo_costo):
        if nuevo_costo <= 0:
            raise ValueError('Costo no valido')
        self.__costo = nuevo_costo

    def __str__(self):
        return f'Producto {self.__dict__.__str__()}'

    def vender(self, cantidad:int):
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True

    def reponer(self, cantidad:int):
        if cantidad <= 0:
            return False
        self.stock += cantidad
        return True

    def valor_inventario(self):
        return self.precio * self.stock

    def precio_venta(self):
        return round(self.precio * (1 + Producto.iva), 2)

if __name__ == '__main__':
    # arroz = Producto(codigo='A001', nombre='Arroz 2Kg.', precio=2.10)
    # arroz.precio = 2.10
    # # arroz.stock = 5
    # print(arroz.valor_inventario())
    # azucar = Producto(codigo='A002', nombre='Azucar 2Kg.', precio=3.20, stock=10)
    # print(azucar.valor_inventario())
    #
    # cafe = Producto(precio=8.50, stock=23, codigo='C001', nombre='Cafe')
    # print(cafe.valor_inventario())
    #
    # arroz.reponer(20)
    # azucar.vender(8)
    # cafe.vender(22)
    #
    # print('*'.center(50,"*"))
    # print(arroz.valor_inventario())
    # print(azucar.valor_inventario())
    # print(cafe.valor_inventario())
    # print(arroz.iva)

    arroz = Producto(codigo='A001', nombre='Arroz 2Kg.', precio=2.10, stock=10, costo=1.9)
    print(arroz.precio)
    arroz.precio = 5.10
    print(arroz.precio)
    print(arroz.stock)
    arroz.stock = 15
    print(arroz.stock)
    print(arroz.__str__())
    print(arroz)
    print(f'El precio + IVA es: {arroz.precio_venta()}')
    # print(arroz.nombre)
    # print(arroz.precio)
    # print(arroz.stock)
    #
    # print(arroz._proveedor)
    # # print(arroz.__costo)
    # arroz.__costo = 1.5
    # print(arroz._Producto__costo)
    # arroz.precio = -3.2
    # arroz.stock = -3
    # print(arroz.precio)
    # print(arroz.stock)

