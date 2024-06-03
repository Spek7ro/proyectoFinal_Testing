Característica: Eliminar una cuenta bancaria
Como usuario quiero poder eliminar una cuenta bancaria
del sistema.

Escenario: Eliminar una cuenta bancaria
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace Cuentas Bancarias
Y luego doy clik en el boton de lista de cuentas bancarias
Y luego doy clik en el boton de eliminar cuenta
Cuando presiono el boton de confirmar eliminación de la cuenta bancaria
Entonces no puedo ver el nombre el id "8" en la lista de cuentas
