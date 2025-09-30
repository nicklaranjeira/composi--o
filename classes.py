class Processador: 
    def __init__(self, modelo, velocidade ):
        self.__modelo = modelo
        self.__velocidade = velocidade
    
    def getModelo(self):
        return self.__modelo
    
    def getVelocidade(self):
        return self.__velocidade
    
    def __str__(self):
        return f"{self.__modelo} - {self.__velocidade}"

class MemoriaRam:
    def __init__(self, ram_capacidade, ram_tipo):
        self.__capacidade = ram_capacidade
        self.__tipo = ram_tipo

    def getCapacidade(self):
        return self.__capacidade
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"{self.__capacidade} - {self.__tipo}"
    
class Armazenamento:
    def __init__(self, arm_tipo, arm_capacidade ):
        self.__tipo = arm_tipo
        self.__capacidade = arm_capacidade

    def getCapacidade(self):
        return self.__capacidade
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"{self.__capacidade} - {self.__tipo}"
    
    
class Computador:
    def __init__(self, PC_marca, PC_modelo, modelo, velocidade, ram_capacidade, ram_tipo, arm_tipo, arm_capacidade):
        self.__modelo = PC_modelo
        self.__marca = PC_marca
        self.__processador = Processador(modelo, velocidade)
        self.__memoriaRAM = MemoriaRam(ram_capacidade, ram_tipo)
        self.__armazenamento = Armazenamento(arm_tipo, arm_capacidade)

    def __str__(self):
        return f"{self.__modelo} - {self.__marca} - {self.__processador} - {self.__memoriaRAM} - {self.__armazenamento}"
