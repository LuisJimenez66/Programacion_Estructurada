
from paquete1 import modulos

print(modulos.saludar("Saul"))
modulos.esperar()
modulos.borrar()
nombre,telefono=modulos.datos2()
print(f"\n\t..::: Agenda Telefonica:::...\n\t\tNombre: {nombre}\n\t\tTelefono: {telefono}")
modulos.esperar()