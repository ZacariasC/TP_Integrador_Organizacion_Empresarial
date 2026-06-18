# Simulador de chatbot para solicitud de vacaciones
# Empresa: La Chispa Motos - taller y venta de artículos para motos

empleados = [
    {"legajo": 1001, "nombre": "Zacarias Cabral", "cargo": "Mecánico", "dias": 30},
    {"legajo": 1002, "nombre": "Milagros Ayala", "cargo": "Vendedora", "dias": 10},
    {"legajo": 1003, "nombre": "Martin Sosa", "cargo": "Encargado de depósito", "dias": 20},
    {"legajo": 1004, "nombre": "Lupe Cabral", "cargo": "Administrativa", "dias": 20},
    {"legajo": 1005, "nombre": "Roman Sosa", "cargo": "Mecánico", "dias": 15}
]


def buscar_empleado(legajo):
    for empleado in empleados:
        if empleado["legajo"] == legajo:
            return empleado
    return None


def pedir_legajo():
    while True:
        try:
            legajo = int(input("Bot: Ingrese su número de legajo: "))
            return legajo
        except ValueError:
            print("Bot: Error. El legajo debe ser un número.")


def pedir_dias():
    while True:
        try:
            dias = int(input("Bot: ¿Cuántos días de vacaciones desea solicitar?: "))

            if dias <= 0:
                print("Bot: Error. La cantidad de días debe ser mayor a cero.")
            else:
                return dias

        except ValueError:
            print("Bot: Error. Debe ingresar una cantidad numérica.")


def procesar_solicitud(empleado, dias_solicitados):
    if dias_solicitados <= empleado["dias"]:
        empleado["dias"] -= dias_solicitados
        print("Bot: Solicitud aprobada.")
        print(f"Bot: Le quedan {empleado['dias']} días disponibles.")
    else:
        print("Bot: Solicitud rechazada.")
        print("Bot: No posee suficientes días disponibles.")


def iniciar_chatbot():
    print("Bot: Bienvenido al sistema de solicitud de vacaciones.")
    print("Bot: Este sistema pertenece a la empresa LA CHISPA MOTOS taller y venta de artículos.")

    legajo = pedir_legajo()
    empleado = buscar_empleado(legajo)

    if empleado is None:
        print("Bot: Error. No se encontró un empleado con ese legajo.")
    else:
        print(f"Bot: Hola {empleado['nombre']}.")
        print(f"Bot: Cargo registrado: {empleado['cargo']}.")
        print(f"Bot: Días disponibles: {empleado['dias']}.")

        dias_solicitados = pedir_dias()
        procesar_solicitud(empleado, dias_solicitados)

    print("Bot: Fin del proceso.")


while True:

    iniciar_chatbot()

    continuar = input("\n¿Desea realizar otra solicitud? (s/n): ").lower()

    if continuar != "s":
        print("Bot: Gracias por utilizar el sistema.")
        break