import os
import sys
from datetime import date

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

import Classes.cliente as cliente_class
import Classes.Estado.cambio_estado as cambio_estado
from Classes.respuesta_de_cliente import RespuestaDeCliente


class Llamada:
    def __init__(self, descripcion_operador: str, detalle_accion: str,
                 encuesta_enviada: bool, observacion_auditor: str, cliente: cliente_class.Cliente, primer_cambio_estado: cambio_estado.CambioEstado):
        # Validaciones
        # assert duracion > 0.0, "La duracion debe ser mayor a cero"

        # Atributos propios

        self.__descripcion_operador = descripcion_operador
        self.__detalle_accion = detalle_accion
        self.__encuesta_enviada = encuesta_enviada
        self.__observacion_auditor = observacion_auditor
        self.__duracion = 0.0

        # Atributos referencia
        self.__respuestas_de_encuesta = []
        self.__cambios_estado = [primer_cambio_estado]
        self.__cliente = cliente


    # -------------------
    # Getters & Setters -
    # -------------------

    # Getter descripcion_operador
    @property
    def descripcion_operador(self):
        # Executes this code when object.att
        return self.__descripcion_operador

    # Setter descripcion_operador
    @descripcion_operador.setter
    def descripcion_operador(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__descripcion_operador = value

    # Getter detalle_accion
    @property
    def detalle_accion(self):
        # Executes this code when object.att
        return self.__detalle_accion


    # Setter detalle_accion
    @detalle_accion.setter
    def detalle_accion(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__detalle_accion = value


    # Getter encuesta_enviada
    @property
    def encuesta_enviada(self):
        # Executes this code when object.att
        return self.__encuesta_enviada

    # Setter encuesta_enviada
    @encuesta_enviada.setter
    def encuesta_enviada(self, value):
        # Executes this code when object.att = value
        self.__encuesta_enviada = value


    # Getter observacion_auditor
    @property
    def observacion_auditor(self):
        # Executes this code when object.att
        return self.__observacion_auditor

    # Setter observacion_auditor
    @observacion_auditor.setter
    def observacion_auditor(self, value):
        # Executes this code when object.att = value
        if len(value) > 15:
            raise Exception("Muy largo")
        else:
            self.__observacion_auditor = value

    # Getter duracion
    @property
    def duracion(self):
        # Executes this code when object.att
        return self.__duracion

    # Setter duracion
    @duracion.setter
    def duracion(self, value):
        # Executes this code when object.att = value
        if value < 0.0:
            raise Exception("No puede ser negativo")
        else:
            self.__duracion = value

    # Getter duracion
    @property
    def cliente(self):
        # Executes this code when object.att
        return self.__cliente

    # Setter duracion
    @cliente.setter
    def cliente(self, value):
        # Executes this code when object.att = value
        self.__cliente = value

    # Getter respuestas_de_encuesta
    @property
    def respuestas_de_encuesta(self):
        # Executes this code when object.att
        return self.__respuestas_de_encuesta
    
    # Add respuesta de encuesta
    def add_respuesta_encuesta(self, respuesta_encuesta: RespuestaDeCliente):
        self.__respuestas_de_encuesta.append(respuesta_encuesta)

    # Getter cambio_estado
    @property
    def cambios_estado(self):
        # Executes this code when object.att
        return self.__cambios_estado
    
    # Add cambio de estado
    def add_cambio_estado(self, cambio_estado: cambio_estado.CambioEstado):
        # Puede ser que haga falta hacer un add in order
        self.__cambios_estado.append(cambio_estado)


    # Metodos

    def calcular_duracion(self):
        fecha_hora_inicio_llamada = self.cambios_estado[0].fecha_hora_inicio
        fecha_hora_fin_llamada = self.cambios_estado[-1].fecha_hora_inicio
        duracion = fecha_hora_fin_llamada - fecha_hora_inicio_llamada 
        return round(duracion.seconds/60, 2)
    
    def get_fecha_inicio(self):
        primer_cambio_estado = self.cambios_estado[0]
        fecha_inicio_llamada = primer_cambio_estado.fecha_hora_inicio.date()
        return fecha_inicio_llamada

    
    # Metodos de ejecucion de CU

    # mensaje 9
    def es_de_periodo(self, fecha_inicio_periodo: date, fecha_fin_periodo: date):
        fecha_inicio_llamada = self.get_fecha_inicio()
        # print(type(fecha_inicio_llamada))
        if fecha_inicio_periodo < fecha_inicio_llamada < fecha_fin_periodo:
            print(f"[ Llamada en periodo encontrada ] ")
            return True
        return False
    
    # mensaje 10   - y el mensaje 11 con el len
    def tiene_respuesta_encuesta(self):
        # Mensaje 11
        return len(self.respuestas_de_encuesta) > 0  
        # return self.respuestas_de_encuesta.existe_respuesta() (mensaje 11)
        # return self.respuestas_de_encuesta

    # mensaje 17
    def get_nombre_de_cliente(self):
        # Mensaje 18
        return self.cliente.nombre_completo

    # mensaje 20
    def buscar_ultimo_estado(self):
        # Mensaje 21      (Acceder al ultimo elemento de la lista cambios de estado)
        ultimo_cambio_estado = self.cambios_estado[-1]  
        # Mensaje 22
        return ultimo_cambio_estado.get_nombre_estado()
    



if __name__ == "__main__":
    pass