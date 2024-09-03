#Define función para imprimir variable
def print_variables():
    #Asigna dos numeros y una palabra a tres variables
    first_number = 8
    second_number = 10.5
    word = "Armiño"
    #Asigna las variables a un conjunto
    variables = {first_number, second_number, word}
    #Asigna el estado False a una variable
    is_complete = False
    list_of_variables = [variables, is_complete]
    #imprime lista de variables
    print(list_of_variables)

#Añade convención
if __name__ == "__main__":
    print_variables()