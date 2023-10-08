from django.core.exceptions import ValidationError

def validar_codigo(value):
    if len(value) <=1 :
        raise ValidationError("El codigo debe ser mayor a 1 caracter") 
    
def validar_login(value):
    if value.islower()==False:
        raise ValidationError("El login debe estar en minuscula") 
    