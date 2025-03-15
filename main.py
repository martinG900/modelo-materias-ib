from Módulos.estudiantes import Estudiante, Persona
from Módulos.materia import Materia
from Módulos.admin import Admin

est1 = Estudiante("martin", "13", "Vocacional")
est2 = Estudiante("jose", "14", "Vocacional")
est3 = Estudiante("juan", "23", "Ingeniería Nuclear")

per = Persona("ivan", "56")

mat = Materia("math", per, 1990)

mat.aggEst(est1)
mat.aggEst(est2)
mat.aggEst(est3)

mat.aggNota(8, est1)
mat.aggNota(9, est2)
mat.aggNota(4, est3)

adm = Admin(mat)

adm.prntCert()
