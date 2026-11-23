from datetime import date

from producto import Producto

class ProductoPerecible(Producto):
    """
    Permite crear clase de producto perecible
    """

    def __init__(self, codigo, nombre, precio, stock, fecha_vencimiento):
        super().__init__(codigo=codigo, nombre=nombre, precio=precio,
                         stock=stock)
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, nueva_fecha_vencimiento):
        self.__fecha_vencimiento = nueva_fecha_vencimiento

    def dias_por_vencer(self):
        return (self.__fecha_vencimiento - date.today()).days

    def precio_venta(self):
        base = super().precio_venta()
        if self.dias_por_vencer() <= 3:
            return round(base * 0.7, 2)
        else:
            return base

if __name__ == '__main__':
    yogurt = ProductoPerecible(nombre='Yogurt 15 ml', codigo='Y001',
                               precio=2.03, stock=15,
                               fecha_vencimiento=date(2026,12,28))
    print(yogurt)
    print(f'Dias por vencer del producto: {yogurt.dias_por_vencer()}')