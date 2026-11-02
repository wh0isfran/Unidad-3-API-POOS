from views.utils import leer_numero

class MainView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "="*50)
        print("     CLÍNICA SANITARIA - MENÚ PRINCIPAL")
        print("="*50)
        print("1.- Gestión de Pacientes")
        print("2.- Gestión de Departamentos")
        print("3.- Farmacia y Recetas Médicas (Consumo de API)")
        print("0.- Salir del Sistema")
        print("="*50)
        return leer_numero("Seleccione una opción: ")

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"\n[SISTEMA] {mensaje}")
