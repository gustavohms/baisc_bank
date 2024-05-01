class Bicicleta:
    #Construtor
    def __init__(self, cor, modelo, ano, valor):
        #Atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #Métodos são funções que estão dentro de classes
    def buzinar(self):
        print("Plim Plim")

    def parar(sef):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("Vrummmm...")

    #Código útil para fazer representações de classes de amaneira automática
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1)

#20:42 min vídeo
