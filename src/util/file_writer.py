import csv

# En este módulo se aplica el principio de Single Responsibility,
# pues la clase solo se encarga de crear un archivo.
# También se aplica el principio de Dependency Inversion, ya que
# este modulo puede convertir cualquier objeto que se pueda convertir a
# diccionario a un archivo, no tiene que ser un objeto específicamente
# de algún tipo.
class FileWriter:
    def create_csv(self, filename, columns, data):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for item in data:
                writer.writerow(item.to_dict())