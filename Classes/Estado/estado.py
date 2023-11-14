class Estado:
    def __init__(self, nombre: str):
        self.__nombre = nombre

# Getter fecha_hora_inicio
    @property
    def nombre(self):
        # Executes this code when object.att
        return self.__nombre 

    # Setter fecha_hora_inicio
    @nombre.setter
    def fecha_hora_inicio(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__nombre = value



if __name__ == "__main__":
    pass