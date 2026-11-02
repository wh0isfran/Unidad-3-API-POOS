from views.main_view import MainView
from controllers.paciente_controller import PacienteController
from controllers.departamento_controller import DepartamentoController
from controllers.farmacia_controller import FarmaciaController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.paciente_controller = PacienteController()
        self.departamento_controller = DepartamentoController()
        self.farmacia_controller = FarmaciaController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.paciente_controller.ejecutar()
            elif opcion == 2:
                self.departamento_controller.ejecutar()
            elif opcion == 3:
                self.farmacia_controller.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema de la Clínica. ¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje("Opción no válida. Por favor, intente nuevamente.")
