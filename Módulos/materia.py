
class Materia:
    def __init__(self, nom, doc, year):
        """El argumento doc es un objeto Persona, est es un objeto
        Estudiante"""
        self.nom = nom
        self.est = []
        self.doc = [doc]
        self.nota = {}
        self.year = year

    """Llamar directamente a otra clase puede crear problemas si
    se modifica esa otra clase. Por ejemplo, si se añaden atributos
    a la clase, puede añadirse que tenga un valor determinado. Esto
    no es una solución adecuada.
    Otra mejor solución es que el argumento de aggEst sea un objeto
    Estudiante. Así se desacoplan Materia y Estudiante. Siempre es
    buena práctica desacoplar las clases"""

    def aggEst(self, est):
        """El argumento est es un objeto Estudiante"""
        self.est.append(est)

    def aggDoc(self, per):
        """El argumento per es un objeto Persona"""
        self.doc.append(per)

    def aggNota(self, nota, est):
        '''est es un personaje Estudiante'''
        self.nota[est.nombre] = nota

    def prntEst(self):
        for nm in self.est:
            print(f"{nm.nombre}, {nm.edad}, {nm.carr}", end="; ")

    def prntDoc(self):
        for nm in self.doc:
            print(f"{nm.nombre}, {nm.edad}", end="; ")
