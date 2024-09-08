import unittest

class MaquinaDeTejerExtensiones:
    def __init__(self):
        # Inicializa los atributos de la clase
        self.__TipoTrenza = ''  # Tipo de trenza seleccionada (privado)
        self.__longitud = 0     # Longitud de la extensión (privado)

    # Método estándar para representar el objeto como cadena
    def __str__(self):
        # Si ambos atributos están configurados, devuelve una descripción completa
        if self.__TipoTrenza and self.__longitud:
            return f"Maquina de Tejer lista para {self.__TipoTrenza} con longitud de {self.__longitud} cm."
        # Si no están configurados, indica que la máquina no está lista
        return "Maquina de Tejer no configurada."

    # Método para seleccionar el tipo de trenza que la máquina va a tejer
    def SeleccionarTipoTrenza(self, TipoTrenza: str): 
        TrenzasValidas = ["trenza simple", "trenza espiga", "trenza africana"]
        # Verifica si el tipo de trenza proporcionado es válido
        if TipoTrenza not in TrenzasValidas:
            raise ValueError(f"Tipo de trenza no válida: {TipoTrenza}")
        # Establece el tipo de trenza seleccionado si es válido 
        self.__TipoTrenza = TipoTrenza

    # Método para configurar la longitud dentro del rango permitido
    def ConfigurarLongitud(self, longitud: int):
        if 10 <= longitud <= 80:
            self.__longitud = longitud
        else:
            raise ValueError("La longitud debe estar entre 10 y 80 cm.")
        
    # Método para tejer la extensión según el tipo de trenza y la longitud elegida  
    def TejerExtension(self):
        if self.__TipoTrenza and self.__longitud:    
            # Devuelve un mensaje indicando la extensión que se está tejiendo
            return f"Tejiendo extensión de {self.__longitud} cm tejida con {self.__TipoTrenza}"
        else:
            raise ValueError("Debe seleccionar tipo de trenza y configurar longitud antes de tejer")


# Pruebas TDD: pruebas unitarias para la clase MaquinaDeTejerExtensiones
class TestMaquinaDeTejerExtensiones(unittest.TestCase):
    # Método que se ejecuta antes de cada prueba para inicializar un objeto de la clase
    def setUp(self):
        self.maquina = MaquinaDeTejerExtensiones()

    # Prueba unitaria para verificar un tipo de trenza inválido
    def test_seleccionar_tipo_trenza_invalido(self):
        with self.assertRaises(ValueError):
            self.maquina.SeleccionarTipoTrenza("trenza invisible")

    # Prueba unitaria para verificar una longitud no válida
    def test_configurar_longitud_invalida(self):
        with self.assertRaises(ValueError):
            self.maquina.ConfigurarLongitud(100)

    # Prueba unitaria para verificar que lanza un error si no se configuran los parámetros
    def test_tejer_extension_sin_configuracion(self):
        with self.assertRaises(ValueError):
            self.maquina.TejerExtension()

    # Prueba unitaria para verificar que la extensión se teje correctamente con configuraciones válidas 
    def test_tejer_extension_correcto(self):
        self.maquina.SeleccionarTipoTrenza("trenza espiga")
        self.maquina.ConfigurarLongitud(30)
        resultado = self.maquina.TejerExtension()
        self.assertEqual(resultado, "Tejiendo extensión de 30 cm tejida con trenza espiga")


# Interacción con el usuario
def main():
    trenzar = MaquinaDeTejerExtensiones()   # Crea un objeto de la clase MaquinaDeTejerExtensiones
    # Bucle para seleccionar el tipo de trenza
    while True:
        # Seleccionar tipo de trenza
        while True:
            tipo_trenza = input("Seleccione el tipo de trenza (trenza simple, trenza espiga, trenza africana): ")
            try:
                trenzar.SeleccionarTipoTrenza(tipo_trenza) # Intenta seleccionar el tipo de trenza
                break
            except ValueError as e:
                print(e)  # Nos muestra el error si la trenza no es válida

        # Bucle para configurar longitud de la extensión
        while True:
            try:
                longitud = int(input("Ingrese la longitud de la extensión (10-80 cm): "))
                trenzar.ConfigurarLongitud(longitud)   # Intenta configurar la longitud
                break     # Sale del bucle si la longitud es válida
            except ValueError as e:
                print(e)  # Muestra el error si la longitud no es válida

        # Tejer extensión con las configuraciones proporcionadas
        try:
            print(trenzar.TejerExtension())  # Muestra el mensaje de la extensión que se está tejiendo
        except ValueError as e:
            print(e)     # Muestra el error si no se configuraron correctamente los parámetros

        # Mostrar estado de la máquina
        print(trenzar) # Muestra la representación de la máquina
        
        # Mensaje final
        print("Listo, trenza terminada")
        break   # Termina el programa después de tejer la trenza

# Ejecuta las pruebas unitarias y la función principal
if __name__ == "__main__":
    # Ejecuta las pruebas unitarias
    unittest.main(exit=False) # exit=False permite que las pruebas no detengan la ejecución del programa

    # Ejecuta la interacción con el usuario
    main()


