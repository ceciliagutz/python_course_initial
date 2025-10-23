"""Inteccion de depenmccias por constructor"""

# class RepositorioBD:
#     def guardar(self, pedido):
#         print(f"Pedido {pedido} almacenado correctamente")

# class ServicioPedidos:
#     def __init__(self, repositorio: RepositorioBD):
#         self.repositorio = repositorio

#     def crear_pedido(self, pedido: str):
#         print("Notificacion por mensaje")
#         print("Impresion de orden")
#         self.repositorio.guardar(pedido)
#         print("Noificacion de almacenado")

# repo = RepositorioBD()
# service = ServicioPedidos(repo)

# service.crear_pedido("Hamburguesa")


##########################################################################


# """Inteccion de depenmccias por constructor"""

# class RepositorioBD:
#     def guardar(self, pedido):
#         print(f"Pedido {pedido} almacenado correctamente")

# class ServicioPedidos:
#     def set_repo(self, repositorio: RepositorioBD):
#         self.repositorio = repositorio

#     def crear_pedido(self, pedido: str):
#         print("Notificacion por mensaje")
#         print("Impresion de orden")
#         self.repositorio.guardar(pedido)
#         print("Noificacion de almacenado")

# repo = RepositorioBD()
# service = ServicioPedidos(repo)

# service.set_repo(repo)

# service.crear_pedido("Hamburguesa")

#############################################################


"""Interfaces con patrones"""

from abc import ABC, abstractmethod

class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}" )

class ServicioPedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repo = repositorio

    def crear_pedido(self, pedido:str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repo.guardar(pedido)
        print("Noificacion de almacenado")

# repoBD: IRepositorioBD = RepositorioBD()
# repoAPI: IRepositorioBD = ApiTercerosAdapter()


# service = ServicioPedido(repoAPI)

# service.crear_pedido("tacos")


##################################################################


"""Inyeccion manual de dependencias"""

class Container:
    def __init__(self):
        self._servicios = {}

    def register(self, nombre, creator):
        self._servicios[nombre] = creator

    def resolver(self, nombre):
        return self._servicios[nombre]()


container = Container()
container.register("repositorio", lambda: ApiTercerosAdapter())
container.register("service", lambda: ServicioPedido(container.resolver("repositorio")))

service = container.resolver("service")

service.crear_pedido("Crepas")