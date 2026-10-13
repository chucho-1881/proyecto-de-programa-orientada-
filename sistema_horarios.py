
class SistemaHorarios:
    def __init__(self):
        self.__horarios = []

    
    def convertir_hora(hora):
        try:
            partes = hora.split(":")
            if len(partes) != 2:
                return None

            horas = int(partes[0])
            minutos = int(partes[1])

            if not (0 <= horas <= 23 and 0 <= minutos <= 59):
                return None

            return horas * 60 + minutos
        except ValueError:
            return None

    def agregar_horario(self, nuevo):
        inicio = self.convertir_hora(nuevo.hora_inicio)
        fin = self.convertir_hora(nuevo.hora_fin)

        if inicio is None or fin is None or inicio >= fin:
            print("Error: las horas no son validas.")
            return

        for horario in self.__horarios:
            if horario.dia.lower() == nuevo.dia.lower():
                otro_inicio = self.convertir_hora(
                    horario.hora_inicio
                )
                otro_fin = self.convertir_hora(
                    horario.hora_fin
                )

                # Detectar cruce de horarios
                if inicio < otro_fin and fin > otro_inicio:
                    print(
                        "Error: el horario se cruza con "
                        "otra clase de ese dia."
                    )
                    return

        self.__horarios.append(nuevo)
        print("Horario agregado correctamente.")

    def mostrar_todos(self):
        if not self.__horarios:
            print("No hay horarios registrados.")
            return

        for horario in self.__horarios:
            horario.mostrar_horario()

    def buscar_por_dia(self, dia):
        encontrados = [
            h for h in self.__horarios
            if h.dia.lower() == dia.lower()
        ]

        if not encontrados:
            print(f"No hay clases registradas el {dia}.")
            return

        for horario in encontrados:
            horario.mostrar_horario()


def main():
    sistema = SistemaHorarios()

    profesor1 = Profesor(
        "Carlos Mendoza",
        "PROF001",
        "Programacion"
    )

    profesor2 = Profesor(
        "Maria Lopez",
        "PROF002",
        "Base de Datos"
    )

    estudiante1 = Estudiante(
        "Juan Perez",
        "EST001",
        "Desarrollo de Software"
    )

    materia1 = Materia(
        "Programacion Orientada a Objetos",
        "Laboratorio 2",
        profesor1
    )

    materia2 = Materia(
        "Base de Datos",
        "Aula 3",
        profesor2
    )

    horario1 = Horario(
        "Lunes",
        "08:00",
        "10:00",
        materia1
    )

    horario2 = Horario(
        "Martes",
        "10:00",
        "12:00",
        materia2
    )

    print("=" * 42)
    print("   SISTEMA DE HORARIOS ACADEMICOS")
    print("=" * 42)

    print("\n--- DATOS DEL PROFESOR ---")
    profesor1.mostrar_datos()

    print("\n--- DATOS DEL ESTUDIANTE ---")
    estudiante1.mostrar_datos()

    print("\n--- REGISTRO DE HORARIOS ---")
    sistema.agregar_horario(horario1)
    sistema.agregar_horario(horario2)

    print("\n--- TODOS LOS HORARIOS ---")
    sistema.mostrar_todos()

    print("\n--- BUSCAR HORARIOS DEL LUNES ---")
    sistema.buscar_por_dia("Lunes")

    print("\nSistema finalizado.")


if __name__ == "__main__":
    main()
