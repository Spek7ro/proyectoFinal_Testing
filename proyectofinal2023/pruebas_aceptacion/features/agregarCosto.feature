Característica: Agregar un nuevo costo
Como usuario quiero poder registrar 
un nuevo costo en el sistema

Escenario: Registro de un costo 
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace costos
Y luego clik en el boton de agregar costo
Y escribo el la descripcion del costo "Se compro un fertilizante"
Y escribo el costo del costo "300"
Y selecciono el proyecto del costo "Sistema de fertilizantes"
Cuando presiono el boton agregar
Entonces puedo ver la descripcion del costo "Se compro un fertilizante" en la lista de costos
