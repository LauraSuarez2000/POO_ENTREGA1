class Caja:
    def __init__(self):
        self.base_caja = 0
        self.monto_en_caja = 0

    def registrar_base_caja(self):
        self.base_caja = float(input("Ingrese la base de la caja: "))

    def registrar_monto_en_caja(self):
        self.monto_en_caja = float(input("Ingrese el monto actual en caja: "))

    def mostrar_estado_caja(self):
        print("Base de caja:", self.base_caja)
        print("Monto en caja:", self.monto_en_caja)


class Administrador:
    def __init__(self, nombre: str, identificacion: int):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_informacion(self):
        print("Nombre del administrador:", self.nombre)
        print("Identificación:", self.identificacion)


class Personal:
    CARGO_VENDEDOR = "cargo_vendedor"
    CARGO_AUXILIAR_BODEGA = "cargo_auxiliar_bodega"

    def __init__(self, nombre:str, identificacion:int, cargo:str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cargo = cargo


    @classmethod
    def registrar_personal(cls):
        # Lista para almacenar los empleados
        empleados = []

        while True:
            nombre = input("Ingrese el nombre del empleado: ")
            identificacion = int(input("Ingrese la identificación del empleado: "))
            cargo = input("Ingrese el cargo del empleado: ")

            empleado = cls(nombre, identificacion, cargo)
            empleados.append(empleado)

            otro_empleado = input("¿Desea registrar otro empleado? (Sí/No): ")
            if otro_empleado.lower() != 'sí' and otro_empleado.lower() != 'si':
                break

        return empleados
class GestionPersonal:
    administradores = []
    personal_a_cargo = []

    @classmethod
    def registrar_administrador(cls, nombre: str, identificacion: int):
        nuevo_administrador = Administrador(nombre, identificacion)
        cls.administradores.append(nuevo_administrador)

    @classmethod
    def mostrar_administradores(cls):
        print("Lista de Administradores:")
        for administrador in cls.administradores:
            administrador.mostrar_informacion()

    @classmethod
    def mostrar_personal(cls):
        print("Lista de Personal a Cargo:")
        for persona in cls.personal_a_cargo:
            print("Nombre:", persona.nombre)
            print("Identificación:", persona.identificacion)
            print("Cargo:", persona.cargo)


class Sede:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def mostrar_informacion(self):
        print("Nombre de la sede:", self.nombre)


class Venta:
    MEDIO_DE_PAGO_EFECTIVO = "efectivo"
    MEDIO_DE_PAGO_TRANSFERENCIA = "transferencia"
    ventas = []
    total_ventas = 0 

    def __init__(self, consecutivo: int, monto: float, medio_pago: str, observaciones: str):
        self.consecutivo = consecutivo
        self.monto = monto
        self.medio_pago = medio_pago
        self.observaciones = observaciones
        self.__class__.ventas.append(self) 
        self.__class__.total_ventas += monto 

    @classmethod
    def registrar_venta(cls, venta):
        cls.ventas.append(venta)

    @classmethod
    def calcular_venta_efectivo(cls):
        total_efectivo = sum(venta.monto for venta in cls.ventas if venta.medio_pago == cls.MEDIO_DE_PAGO_EFECTIVO)
        return total_efectivo

    @classmethod
    def calcular_venta_transferencia(cls):
        total_transferencia = sum(venta.monto for venta in cls.ventas if venta.medio_pago == cls.MEDIO_DE_PAGO_TRANSFERENCIA)
        return total_transferencia
    
    @classmethod
    def calcular_total_ventas(cls):
        return sum(venta.monto for venta in cls.ventas)

    @classmethod
    def obtener_total_ventas(cls):
        return cls.calcular_total_ventas()

class Egreso:
    tipos_egreso = ['compra_proveedores', 'arqueo', 'otro']
    egresos = {tipo: [] for tipo in tipos_egreso}
    total_egresos = {tipo: 0 for tipo in tipos_egreso}  # Total egresos for each type

    def __init__(self, tipo: str, monto: float, observacion: str, orden_compra: str = None, num_factura: str = None):
        self.tipo = tipo
        self.monto = monto
        self.observacion = observacion
        self.orden_compra = orden_compra
        self.num_factura = num_factura

        self.__class__.egresos[tipo].append(self)  # Store the egreso in the class attribute
        self.__class__.total_egresos[tipo] += monto 
        Egreso.egresos[tipo].append(self)
    
    @classmethod
    def registrar_egresos(cls):
        tipo_egreso = input("Ingrese el tipo de egreso (compra_proveedores, arqueo u otro): ")
        monto_egreso = float(input("Ingrese el monto del egreso: "))
        observaciones_egreso = input("Ingrese observaciones del egreso: ")
        
        if tipo_egreso == 'compra_proveedores':
            orden_compra = input("Ingrese el número de orden de compra: ")
            num_factura = input("Ingrese el número de factura: ")
            cls(tipo_egreso, monto_egreso, observaciones_egreso, orden_compra, num_factura)
        else:
            cls(tipo_egreso, monto_egreso, observaciones_egreso)
    @classmethod
    def calcular_egresos_totales(cls):
        total_egresos_all = sum(sum(egreso.monto for egreso in cls.egresos[tipo]) for tipo in cls.tipos_egreso)
        return total_egresos_all

    @classmethod
    def obtener_total_egresos(cls):
        return cls.total_egresos
    
class NotaDeTraslado:
    def __init__(self, responsable_despacho:str, responsable_recepcion:str, bodega_destino:str):
        self.responsable_despacho = responsable_despacho
        self.responsable_recepcion = responsable_recepcion
        self.bodega_destino = bodega_destino


# Crear una instancia de la caja
caja = Caja()
# Registro de la sede
nombre_sede = input("Ingrese el nombre de la sede: ")
sede = Sede(nombre_sede)

# Registro de la base de la caja y el monto en caja
caja.registrar_base_caja()
caja.registrar_monto_en_caja()

# Registrar administrador
nombre_admin = input("Ingrese el nombre del administrador: ")
identificacion_admin = int(input("Ingrese la identificación del administrador: "))
GestionPersonal.registrar_administrador(nombre_admin, identificacion_admin)

# Registrar personal a cargo
print("Registro de personal a cargo:")
empleados_registrados = Personal.registrar_personal()
# Mostrar información de la sede
print("\nInformación de la sede:")
sede.mostrar_informacion()
# Mostrar información de los empleados registrados
GestionPersonal.mostrar_administradores()
print("\nInformación de los empleados registrados:")
for empleado in empleados_registrados:
    print("Nombre:", empleado.nombre)
    print("Identificación:", empleado.identificacion)
    print("Cargo:", empleado.cargo)
# Registro de ventas
num_ventas = int(input("Ingrese el número de ventas a registrar: "))
for i in range(num_ventas):
    print(f"\nRegistro de venta {i+1}:")
    consecutivo = int(input("Ingrese el consecutivo de la venta: "))
    monto = float(input("Ingrese el monto de la venta: "))
    medio_pago = input("Ingrese el medio de pago (efectivo o transferencia): ").lower()
    observaciones = input("Ingrese observaciones: ")

    venta = Venta(consecutivo, monto, medio_pago, observaciones)
    Venta.registrar_venta(venta)


# Registro de egresos
num_egresos = int(input("Ingrese el número de egresos a registrar: "))
for i in range(num_egresos):
    print(f"\nRegistro de egreso {i+1}:")
    Egreso.registrar_egresos()


# Mostrar estado de la caja
print("\nEstado de la caja:")
caja.mostrar_estado_caja()

# Calcular total de ventas por medio de pago
total_ventas_efectivo = Venta.calcular_venta_efectivo()
total_ventas_transferencia = Venta.calcular_venta_transferencia()
total_ventas = Venta.calcular_total_ventas()

print("Total de ventas en efectivo:", total_ventas_efectivo)
print("Total de ventas por transferencia:", total_ventas_transferencia)
print("Total de ventas:", total_ventas)

# Calcular total de egresos por tipo
print("Total de egresos por tipo:")
for tipo_egreso in Egreso.tipos_egreso:
    print(f"Total de egresos {tipo_egreso}:", sum(egreso.monto for egreso in Egreso.egresos[tipo_egreso]))

# Calcular total de egresos en general
total_egresos_all = Egreso.calcular_egresos_totales()
print("Total de egresos en general:", total_egresos_all)
# Mostrar información

