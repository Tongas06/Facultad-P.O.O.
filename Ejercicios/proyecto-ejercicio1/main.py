from correo import Email
import re

def test():
    # Test: crear instancia de Email
    email = Email("alumno", "gmail", "com", "clave1234")
    assert email.retorna_email() == "alumno@gmail.com"

    # Test: modificar contraseña (caso correcto)
    assert email.cambiar_contraseña("clave1234", "nueva_clave")

    # Test: modificar contraseña (caso incorrecto)
    assert not email.cambiar_contraseña("clave_erronea", "nueva_clave")

    # Test: crear cuenta a partir de dirección de correo
    email2 = Email("", "", "", "")
    email2.crear_cuenta("informatica.fcefn@gmail.com")
    assert email2.retorna_email() == "informatica.fcefn@gmail.com"

    # Test: validar direcciones de correo
    assert es_direccion_valida("test@example.com")
    assert not es_direccion_valida("test@example")


def es_direccion_valida(direccion):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, direccion)


def leer_direcciones_email(archivo):
    with open(archivo, 'r') as f:
        direcciones = f.read().split(',')
    return [direccion.strip() for direccion in direcciones]


def crear_cuentas_email(direcciones):
    cuentas = []
    for direccion in direcciones:
        if es_direccion_valida(direccion):
            cuenta_email = Email("", "", "", "")
            cuenta_email.crear_cuenta(direccion)
            cuentas.append(cuenta_email)
            print(f"Cuenta creada para la dirección {cuenta_email.retorna_email()}")
        else:
            print(f"Error: dirección de email incorrecta: {direccion}")
    return cuentas


def contar_cuentas_con_dominio(cuentas, dominio_buscado):
    contador = 0
    for cuenta in cuentas:
        if cuenta.get_dominio() == dominio_buscado:
            contador += 1
    return contador


def main():
    nombre = input("Ingrese el nombre: ")
    id_cuenta = input("Ingrese el id de cuenta: ")
    dominio = input("Ingrese el dominio: ")
    tipo_dominio = input("Ingrese el tipo de dominio: ")
    contraseña = input("Ingrese la contraseña: ")

    email_persona = Email(id_cuenta, dominio, tipo_dominio, contraseña)

    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {email_persona.retorna_email()}")

    contraseña_actual = input("Ingrese la contraseña actual: ")
    nueva_contraseña = input("Ingrese la nueva contraseña: ")
    
    if email_persona.cambiar_contraseña(contraseña_actual, nueva_contraseña):
        print("Contraseña modificada con éxito.")
    else:
        print("Contraseña incorrecta")


    # Inciso 4
    direcciones = leer_direcciones_email('emails.txt')
    cuentas_email = crear_cuentas_email(direcciones)
    

    # 4b: Ingresar un dominio e indicar cuántos objetos de la clase Email tienen dominio igual al ingresado
    dominio_ingresado = input("Ingrese un dominio: ")
    cantidad_emails = contar_cuentas_con_dominio(cuentas_email, dominio_ingresado)
    print(f"Se encontraron {cantidad_emails} objetos de la clase Email con dominio {dominio_ingresado}.")

    
if __name__ == "__main__":
    main()
    test()
