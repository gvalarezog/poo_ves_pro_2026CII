

class Descontable:
    descuento = 0.10
    def aplicar_descuento(self, valor):
        return round(valor * (1 - self.descuento), 2)

    def __str__(self):
        return f'Se ha llamado a Descontable'