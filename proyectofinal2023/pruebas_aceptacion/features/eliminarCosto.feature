Característica: Eliminar un costo
Como usuario quiero poder eliminar un
costo de la lista de costos del sistema

Escenario: Eliminar un costo
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace costos
Y luego doy clik en el boton de lista de costos
Y luego doy clik en el boton de eliminar costo
Cuando presiono el boton de confirmar eliminación del costo
Entonces no puedo ver la descripcion del costo "coca" en la lista de costos
