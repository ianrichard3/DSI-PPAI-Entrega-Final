import os
import sys
from datetime import date

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

import Classes.pregunta as pregunta


class Encuesta:
    def __init__(self, descripcion: str, fecha_fin_vigencia: date):
        # Atributos propios
        self.__descripcion = descripcion
        self.__fecha_fin_vigencia = fecha_fin_vigencia

        # Atributos referencia
        self.__preguntas = []

    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter descripcion
    @property
    def descripcion(self):
        # Executes this code when object.att
        return self.__descripcion

    # Setter descripcion
    @descripcion.setter
    def descripcion(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__descripcion = value


    # Getter fecha_fin_vigencia
    @property
    def fecha_fin_vigencia(self):
        # Executes this code when object.att
        return self.__fecha_fin_vigencia

    # Setter fecha_fin_vigencia
    @fecha_fin_vigencia.setter
    def fecha_fin_vigencia(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__fecha_fin_vigencia = value

    # Getter preguntas
    @property
    def preguntas(self):
        # Executes this code when object.att
        return self.__preguntas

    def add_pregunta(self, pregunta: pregunta.Pregunta):
        self.__preguntas.append(pregunta)



    # Metodos de CU

    
    # Mensaje 29
    def es_tu_respuesta(self, respuesta_cliente):
        """
        Primero busca (mensaje 30) todas las preguntas con sus respuestas
        Luego dada una respuesta de cliente busca entre las preguntas
        de la encuesta si coincide con alguna respuesta
        """
        # preguntas = self.buscar_preguntas()


        # Mensaje 30
        for pregunta in self.buscar_preguntas():
            # Mensaje 31.a
            for rta in pregunta.listar_respuestas_posibles():  
                # Debugging
                # input(f"Pregunta {pregunta.pregunta} - Para respuesta: {rta}...")

                if rta == respuesta_cliente:
                    # Debugging
                    # print(f"Encuesta '{self.descripcion}' -> '{respuesta_cliente}' Es mi respuesta")
                    
                    # Mensajes 32 y 33
                    return {"pregunta": pregunta.pregunta, "respuesta": respuesta_cliente, "encuesta": self.descripcion}
                
        # Debugging
        # print(f"Encuesta '{self.descripcion}' -> No es mi respuesta")
        return False




    # Mensaje 30
    def buscar_preguntas(self):
        return self.preguntas
    



if __name__ == "__main__":
    pass