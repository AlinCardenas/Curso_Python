try:
    10/0
except Exception as e:
    print(f'Courrio un error:  {e}')
else:
    print(f'Else: se ejecuta si no hay niguna excepción')
finally:
    print(f'Finally: siempre se ejecuta, no importa si se lanza excepción')