from enum import Enum


def convCarr(c):
    if c == "Ingeniería Nuclear":
        return Carr.Nuc
    elif c == "Ingeniería Mecánica":
        return Carr.Mec
    elif c == "Ingeniería en Telecomunicaciones":
        return Carr.Tel
    elif c == "Física":
        return Carr.Fis
    elif c == "Vocacional":
        return Carr.Voc
    else:
        return "Carrera desconocida"


class Carr(Enum):
    Nuc = "Ingeniería Nuclear"
    Mec = "Ingeniería Mecánica"
    Tel = "Ingeniería en Telecomunicaciones"
    Fis = "Física"
    Voc = "Vocacional"

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, carr):
        super().__init__(nombre, edad)
        self.carr = convCarr(carr)
        if self.carr == None:
            print("Carrera inválida")
