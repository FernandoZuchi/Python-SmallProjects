from datetime import datetime

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    diferenca = data_atual - data_nascimento
    idade = diferenca.days // 365
    return idade
    
def hello_python():
    print("Ola python")

def citeste_data_nascimento():
    while True:
        try:
            data = input("Introduza a data de nascimento (YYYY-MM-DD): ")
            data_nascimento = datetime.strptime(data, "%Y-%m-%d")
            return data_nascimento
        except ValueError:
            print("A data inserida não é valida.")

if __name__ == "__main__":
    data_nascimento = citeste_data_nascimento()
    idade = calcular_idade(data_nascimento)
    print(f"Você tem {idade} anos")