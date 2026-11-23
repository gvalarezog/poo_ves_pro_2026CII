#comentario
from datetime import date

from producto import Producto
from producto_digital import ProductoDigital
from producto_perecible import ProductoPerecible

arroz = Producto(codigo='A001', nombre='Arroz 2Kg.', precio=2.10, stock=10, costo=1.9)
yogurt = ProductoPerecible(nombre='Yogurt 15 ml', codigo='Y001',
                           precio=2.03, stock=15,
                           fecha_vencimiento=date(2026, 11, 18))
retiro = ProductoDigital(nombre='Retiro Banco del Barrio',
                             codigo='PD001', precio=1,
                             url='http://www.bg.com')
av = ProductoDigital(nombre='Antivirus',
                     codigo='PD002', precio=10,
                     url='http://www.avg.com')
print(arroz)
print(yogurt)
print(retiro)
print(av)

productos = [arroz, yogurt, retiro, av]

for producto in productos:
    if isinstance(producto, ProductoPerecible):
        print(f'Se esta procesando un Producto Perecible')
    elif isinstance(producto, ProductoDigital):
        print(f'Se esta procesando un Producto Digital')
    elif isinstance(producto, Producto):
        print(f'Se esta procesando un Producto')
    else:
        print(f'Se esta procesando un Producto desconocido')
    print(f'Producto: {producto.nombre}, '
          f'su precio con iva y descuento es: {producto.precio_venta()},'
          f'precio + IVA: { round(producto.precio * (1 + Producto.iva),2)}')