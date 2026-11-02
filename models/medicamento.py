class Medicamento:
    """
    Modelo de Dominio para representar un medicamento obtenido desde la API externa.
    """
    def __init__(
        self,
        nombre_comercial: str,
        nombre_generico: str = "",
        principio_activo: str = "",
        proposito: str = "",
        fabricante: str = ""
    ):
        self.nombre_comercial = nombre_comercial
        self.nombre_generico = nombre_generico
        self.principio_activo = principio_activo
        self.proposito = proposito
        self.fabricante = fabricante

    @property
    def nombre_comercial(self) -> str:
        return self._nombre_comercial

    @nombre_comercial.setter
    def nombre_comercial(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre comercial del medicamento no puede estar vacío.")
        self._nombre_comercial = valor.strip().title()

    @property
    def nombre_generico(self) -> str:
        return self._nombre_generico

    @nombre_generico.setter
    def nombre_generico(self, valor: str) -> None:
        self._nombre_generico = (valor or "No especificado").strip().title()

    @property
    def principio_activo(self) -> str:
        return self._principio_activo

    @principio_activo.setter
    def principio_activo(self, valor: str) -> None:
        self._principio_activo = (valor or "No especificado").strip().title()

    @property
    def proposito(self) -> str:
        return self._proposito

    @proposito.setter
    def proposito(self, valor: str) -> None:
        self._proposito = (valor or "Uso general").strip()

    @property
    def fabricante(self) -> str:
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor: str) -> None:
        self._fabricante = (valor or "Laboratorio no informado").strip()

    def __str__(self) -> str:
        return (
            f"Medicamento: {self.nombre_comercial} ({self.nombre_generico}) | "
            f"Activo: {self.principio_activo} | Fabricante: {self.fabricante}"
        )