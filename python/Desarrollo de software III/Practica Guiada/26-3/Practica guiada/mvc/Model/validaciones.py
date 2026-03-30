'''
Modulo de validaciones del dominio
Responsabilidad:
- Validar reglas simples relacionadas con el monto

Relacion con SOLID:
-SRP: este modulo solo contiene validaciones.
    No mezcla logica de negocio con presentacion ni con control
'''

def validar_monto(monto:float):
    '''Valida que el monto sea mahor que cero
    param: Monto: monto a validar
    raise ValieError: si el monto es menor o igual que cero
    '''

    if monto <= 0:
        raise ValueError('El monto debe ser mayor que cero')