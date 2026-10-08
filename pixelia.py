# ==========================================
# BIENVENIDA
# ==========================================

print("====================================")
print("   BIENVENIDO A AVENTURAS EN PIXELA")
print("====================================")

inicio = input("¿Quieres jugar? (s/n): ")

if inicio.lower() != "s":
    print("¡Hasta pronto!")
    exit()


# ==========================================
# CLASE PADRE
# ==========================================

class Entidad:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, danio):
        self.vida -= danio

        if self.vida < 0:
            self.vida = 0

        print(self.nombre, "recibió", danio, "de daño.")
        print("Vida:", self.vida)


# ==========================================
# CLASE JUGADOR
# ==========================================

class Jugador(Entidad):

    def __init__(self, nombre):
        super().__init__(nombre, 100)
        self.experiencia = 0
        self.monedas = 100
        self.inventario = []

    def atacar(self, enemigo):

        print("\n", self.nombre, "atacó a", enemigo.nombre)

        enemigo.recibir_danio(20)

        if enemigo.vida == 0:
            print("¡", enemigo.nombre, "fue derrotado!")
            self.experiencia += 50
            self.monedas += 20


# ==========================================
# CLASE ENEMIGO
# ==========================================

class Enemigo(Entidad):

    def __init__(self, nombre, vida, danio):
        super().__init__(nombre, vida)
        self.danio = danio

    def atacar(self, jugador):

        print(self.nombre, "atacó a", jugador.nombre)

        jugador.recibir_danio(self.danio)


# ==========================================
# CLASES HIJAS DE ENEMIGO
# ==========================================

class EnemigoBasico(Enemigo):
    pass


class EnemigoVolador(Enemigo):

    def volar(self):
        print(self.nombre, "está volando.")


class Jefe(Enemigo):

    def habilidad(self, jugador):
        print(self.nombre, "usó su habilidad especial.")
        jugador.recibir_danio(30)


# ==========================================
# NPC
# ==========================================

class NPC(Entidad):

    def hablar(self):
        print(self.nombre, ": ¡Bienvenido a Pixela!")


# ==========================================
# OBJETO
# ==========================================

class Objeto:

    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self):
        print("Usaste", self.nombre)


# ==========================================
# MISIÓN
# ==========================================

class Mision:

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True
        print("¡Misión completada!")

    def mostrar(self):

        if self.completada:
            estado = "Completada"
        else:
            estado = "Pendiente"

        print("Misión:", self.descripcion)
        print("Estado:", estado)


# ==========================================
# JUEGO
# ==========================================

def juego():

    nombre = input("\nEscribe el nombre de tu personaje: ")

    jugador = Jugador(nombre)

    goblin = EnemigoBasico(
        "Goblin",
        60,
        10
    )

    murcielago = EnemigoVolador(
        "Murciélago",
        50,
        15
    )

    jefe = Jefe(
        "Rey Goblin",
        100,
        25
    )

    npc = NPC(
        "Anciano",
        100
    )

    pocion = Objeto(
        "Poción de Vida"
    )

    mision = Mision(
        "Derrota al Goblin"
    )

    npc.hablar()

    while jugador.vida > 0:

        print("\n========== MENÚ ==========")
        print("1. Atacar Goblin")
        print("2. Atacar Murciélago")
        print("3. Atacar Jefe")
        print("4. Habilidad del Jefe")
        print("5. Ver misión")
        print("6. Recoger poción")
        print("7. Ver jugador")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":

            if goblin.vida > 0:
                jugador.atacar(goblin)

                if goblin.vida == 0:
                    mision.completar()
            else:
                print("El Goblin ya fue derrotado.")

        elif opcion == "2":

            if murcielago.vida > 0:
                jugador.atacar(murcielago)
            else:
                print("El Murciélago ya fue derrotado.")

        elif opcion == "3":

            if jefe.vida > 0:
                jugador.atacar(jefe)
            else:
                print("El jefe ya fue derrotado.")

        elif opcion == "4":

            if jefe.vida > 0:
                jefe.habilidad(jugador)
            else:
                print("El jefe ya fue derrotado.")

        elif opcion == "5":

            mision.mostrar()

        elif opcion == "6":

            jugador.inventario.append(pocion)

            print("Recogiste", pocion.nombre)

        elif opcion == "7":

            print("\n===== JUGADOR =====")
            print("Nombre:", jugador.nombre)
            print("Vida:", jugador.vida)
            print("Experiencia:", jugador.experiencia)
            print("Monedas:", jugador.monedas)

        elif opcion == "8":

            print("¡Gracias por jugar!")
            break

        else:

            print("Opción incorrecta.")

    if jugador.vida <= 0:
        print("\nGAME OVER")


# ==========================================
# INICIAR JUEGO
# ==========================================

juego()
