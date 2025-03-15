def notaLetra(n):
    nota = int(round(n, 0))
    if nota == 1:
        return "Uno"
    elif nota == 2:
        return "Dos"
    elif nota == 3:
        return "Tres"
    elif nota == 4:
        return "Cuatro"
    elif nota == 5:
        return "Cinco"
    elif nota == 6:
        return "Seis"
    elif nota == 7:
        return "Siete"
    elif nota == 8:
        return "Ocho"
    elif nota == 9:
        return "Nueve"
    elif nota == 10:
        return "Diez"
    else:
        return None

class Admin:
    def __init__(self, Mat):
        """Mat es un objeto Materia"""
        self.nom = Mat.nom
        self.est = Mat.est
        self.nota = Mat.nota
        self.year = Mat.year

    def prntEst(self):
        print([est.nombre for est in self.est])

    def prntCert(self):
        with open("Certificado "+self.nom+".txt", "w") as file:
            certStr = self.nom + " " + str(self.year) + "\n"
            for a in self.nota.keys():
                certStr += (
                    a
                    + " "
                    + str(int(round(self.nota[a])))
                    + " ("
                    + notaLetra(self.nota[a])
                    + ")\n"
                )
            file.write(certStr)
