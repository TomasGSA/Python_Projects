class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, num_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f"""  
                    Infomarción del cliente:
        
                    Nombre : {self.nombre}
                    Apellido : {self.apellido}
                    Número de cuenta : {self.num_cuenta}
                    Balance Actual: ${self.balance}"""

    def depositar(self, monto):
        self.balance += monto
        print("Deposito realizado")

    def retirar(self, monto):

        if self.balance >= monto:
            self.balance -= monto
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")


def inicio():
    cliente = crear_cliente()
    print(cliente)
    opcion = 0
    while opcion != "$":
        print("Elije: Depositar (D), Retirar (R), Salir (S)")
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            cliente.retirar(monto_ret)
        else:
            print(cliente)
            print("Hasta luego!")
            break
        print(cliente)


def crear_cliente():
    nombre_cl = input("Ingre su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    num_cuenta = input("Ingrese su número de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, num_cuenta)
    return cliente


inicio()
