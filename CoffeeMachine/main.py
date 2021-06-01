MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost": 0,
}

# TODO: 1. Implementar a função de reportar a quantidade de insumos.


def report():
    print(f" water: {resources['water']}ml")
    print(f" milk: {resources['milk']}ml")
    print(f" coffee: {resources['coffee']}g")
    print(f" caixa: ${resources['cost']}")


# TODO: 2. Implementar a função para verificar se a quantidade de insumo é suficiente para o café requisitado.


def insumos(water, milk, coffee):
    if resources['water'] < water:
        print("Desculpe mas não há água suficiente para o seu pedido")
    elif resources['milk'] < milk:
        print("Desculpe mas não há leite o suficiente para o seu pedido")
    elif resources['coffee'] < coffee:
        print("Desculpe mas não há café o suficiente para o seu pedido")


# TODO: 3. Implementar a função para contagem de dinheiro.


def contagem_dinheiro(quarters, dimes, nickles, pennies):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01
    total_dinheiro = total_quarters + total_dimes + total_nickles + total_pennies
    return total_dinheiro


# TODO: 4. Implementar função para a transação de dinheiro.


def transacao_dinheiro(custo, total_dinheiro):

    if total_dinheiro < custo:
        ("Desculpe não há dinheiro suficiente")

    elif total_dinheiro > custo:
        troco = total_dinheiro - custo
        print(f"Aqui está seu troco de ${troco}.")
        print(f"Preparando seu café")

    else:
        print("Preparando seu café")


#TODO 5. Atualizando inventario.


def atualizar_inventario(agua, leite, cafe, custo):
    resources['water'] -= agua
    resources['milk'] -= leite
    resources['coffee'] -= cafe
    resources['cost'] += custo

maquina_funcionando = True


while maquina_funcionando == True:

    tipo_cafe = input("Qual café você gostaria? (Espresso/Latte/Cappuccino): ").lower()
    if tipo_cafe == 'espresso':
        agua = MENU['espresso']['ingredients']['water']
        leite = MENU['espresso']['ingredients']['milk']
        cafe = MENU['espresso']['ingredients']['coffee']
        custo = MENU['espresso']['cost']
    elif tipo_cafe == 'latte':
        agua = MENU['latte']['ingredients']['water']
        leite = MENU['latte']['ingredients']['milk']
        cafe = MENU['latte']['ingredients']['coffee']
        custo = MENU['latte']['cost']
    elif tipo_cafe == 'cappuccino':
        agua = MENU['cappuccino']['ingredients']['water']
        leite = MENU['cappuccino']['ingredients']['milk']
        cafe = MENU['cappuccino']['ingredients']['coffee']
        custo = MENU['cappuccino']['cost']
    elif tipo_cafe == 'report':
        report()
        continue
    else:
        maquina_funcionando = False

    insumos(agua, leite, cafe)
    print("Insira suas moedas")
    quarters = int(input("Quantos quarters?($0.25): "))
    dimes = int(input("Quantos dimes?($0.10): "))
    nickles = int(input("Quantos nickles?($0.05): "))
    pennies = int(input("Quantas pennies?($0.01): "))

    transacao_dinheiro(custo, contagem_dinheiro(quarters, dimes, nickles, pennies))
    atualizar_inventario(agua, leite, cafe, custo)
    print(f"Aqui está seu {tipo_cafe}. Aproveite!")