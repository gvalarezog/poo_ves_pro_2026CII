#Comentario para mostrar Git
from descontable import Descontable
from producto import Producto


class ProductoDigital(Producto, Descontable):
    """
    Permite crear clases de productos digitales
    """
    def __init__(self, nombre, codigo, precio, url):
        super().__init__(nombre=nombre, codigo=codigo, precio=precio)
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, nueva_url):
        self.__url = nueva_url

    # def __str__(self):
    #     return f'Producto Digital {self.__dict__.__str__()}'

    def precio_venta(self):
        return self.aplicar_descuento(super().precio_venta())

if __name__ == '__main__':
    retiro = ProductoDigital(nombre='Retiro Banco del Barrio',
                             codigo='PD001', precio=1,
                             url='http://www.bg.com')
    print(retiro)
    av = ProductoDigital(nombre='Antivirus',
                             codigo='PD002', precio=10,
                             url='http://www.avg.com')
    print(av)
    print(f'El precio del {av.nombre} es: {av.precio_venta()}')
    print(ProductoDigital.__mro__)