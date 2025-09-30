import os
class Processador: 
    def __init__(self, proc_modelo, proc_velocidade ):
        self.__modelo = proc_modelo
        self.__velocidade = proc_velocidade
    
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
    def __init__(self, PC_marca, PC_modelo, proc_modelo, proc_velocidade, ram_capacidade, ram_tipo, arm_tipo, arm_capacidade):
        self.__modelo = PC_modelo
        self.__marca = PC_marca
        self.__processador = Processador(proc_modelo, proc_velocidade)
        self.__memoriaRAM = MemoriaRam(ram_capacidade, ram_tipo)
        self.__armazenamento = Armazenamento(arm_tipo, arm_capacidade)

    def getPc_modelo(self):
        return self.__modelo
    
    def getPc_marca(self):
        return self.__marca
    
    def getProcessador(self):
        return self.__processador
    
    def getMemoria_ram(self):
        return self.__memoriaRAM
    
    def getArmazenamento(self):
        return self.__armazenamento

computador = Computador(PC_marca="Dell",PC_modelo="Windows10", proc_modelo="Intel ATOM", proc_velocidade= "3,5 ghz", ram_capacidade= "8GB", ram_tipo="DRAM", arm_tipo="SSD", arm_capacidade= "Terabytes")


def ligar(computador):
        print("Bem vindo!")
        os.system("pause")
        os.system("cls" \
        "")
        print(f"Computador: {computador.getPc_modelo()} - {computador.getPc_marca()}")
        print(f"Processador: {computador.getProcessador().getModelo()}- {computador.getProcessador().getVelocidade()}")
        print(f"Armazenamento: {computador.getArmazenamento().getCapacidade()} - {computador.getArmazenamento().getTipo()}")
        print(f"Memória RAM: {computador.getMemoria_ram().getCapacidade()} - {computador.getMemoria_ram().getTipo()}")

ligar(computador)
def __str__(self):
            return f"Bem vindo User!\nComputador:{self.__modelo} - {self.__marca}\nProcessador:\n{self.__processador}\nMemória Ram:{self.__memoriaRAM}\nArmazenamento:\n {self.__armazenamento}"

