Característica: Agregar una nueva cuenta bancaria
Como usuario quiero poder registrar 
una nueva cuenta bancaria en el sistema

Escenario: Registro de una cuenta bancaria
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace Cuentas Bancarias
Y luego clik en el boton de agregar cuenta
Y escribo el id de la cuenta "20"
Y escribo el responsable de la cuenta "Ana Garcia"
Y escribo el limite de prepuestario de la cuenta "3000000"
Y selecciono el proyecto de la cuenta "Sistema de fertilizantes"
Cuando presiono el boton guardar
Entonces puedo ver el id de la cuenta "20" en la lista de cuentas bancarias
