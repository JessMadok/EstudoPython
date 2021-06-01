MENU = {
    "espresso": {
        "ingredients": {
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
    "money": 0,
}


def report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${resources['money']}")



def contando_dinheiro (quarter,dime,nickel,penny):
    total_quarter = quarter * 0.25
    total_dime = dime * 0.10
    total_nickel = nickel * 0.05
    total_penny = penny * 0.01
    total_dinheiro = total_quarter + total_dime + total_nickel + total_penny
    return total_dinheiro




def verificando_dinheiro(dinheiro_colocado, custo):
    if dinheiro_colocado < custo:
        print("Dinheiro insuficiente, tente novamente")
    elif dinheiro_colocado > custo:
        troco = dinheiro_colocado - custo
        print(f"Seu troco é de ${troco}")
        resources['money'] += custo
    else:
        resources['money'] += custo


def meus_recursos (agua, leite, cafe):
    if agua > resources['water']:
        print("Desculpe não há água o suficiente para o seu pedido")
    elif leite > resources['milk']:
        print("Desculpe mas não há leite o suficiente para o seu pedido")
    elif cafe > resources['coffee']:
        print("Desculpe mas não há café suficiente para o seu pedido")
    else:
        resources['water'] -= agua
        resources['milk'] -= leite
        resources ['coffee'] -= cafe


tipo_cafe = input("Qual café você gostaria? (espresso/latte/cappuccino) ")
if tipo_cafe == "espresso":
    agua = MENU['espresso']['ingredients']['water']
    leite = 0
    cafe = MENU['espresso']['ingredients']['coffee']
elif tipo_cafe == "latte":
    agua = MENU['latte']['ingredients']['water']
    leite = MENU['latte']['ingredients']['milk']
    cafe = MENU['latte']['ingredients']['coffee']
elif tipo_cafe == "cappuccino":
    agua = MENU['cappuccino']['ingredients']['water']
    leite = MENU['cappuccino']['ingredients']['milk']
    cafe = MENU['cappuccino']['ingredients']['coffee']
elif tipo_cafe == "report":
    report()

