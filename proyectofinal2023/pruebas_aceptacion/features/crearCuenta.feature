Característica: Crear una cuenta
Como usuario quiero poder crear una cuenta
para poder ingresar al sistema del INIFAP.

Escenario: Ingreso de datos correctos 
Dado que ingreso a la url "http://localhost:8000/autenticacion/"
Y escribo mi nombre de usuario "Chapo701" 
Y escribo mi nombre "Juaquin" 
Y escribo mi apellido "Guzmán"
Y escribo mi correo electrónico "juaquin@gmail.com"
Y escribo mi contraseña "12345678"
Y confirmo mi contraseña "12345678"
Cuando presiono el botón de Registar
Entonces puedo ver en el banner mi nombre de usuario "chapo701"
