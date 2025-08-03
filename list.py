def principal():
 
     while True:
         print('[1] Adiconar número')
         print('[2] Procurar número')
         print('[3] Mostrar lista')   
         print('[4] Ordenar crescente')
         print('[5] Ordenar decrescente')
         print('[6] Sair')

         opcao = input("Selecione sua opção para prosseguir: ")

         if opcao == '1':
            add_Numero(lista)
         elif opcao == '2':
            procurar_Numero(lista)
         elif opcao == '3':
            mostrar_Lista(lista) 
         elif opcao == '4':
            ordenar_Crescente(lista)
         elif opcao == '5':
            ordenar_Decrescente(lista)
         elif opcao == '6':
             print("Saindo...")
         
      
lista = []

def add_Numero(lista):
    try:
        numero = input('Digite os números desejados, separado por espaços: ').split()
        for num in numero:
            lista.append(int(num))
        print("Número adicionado a lista com sucesso:")
    except ValueError:
        print("Erro, por favor digite número inteiro.")


def procurar_Numero(lista):
       numero= int(input ("Digite o número que desejar procurar: "))
       if numero in lista: 
              print (f'O número {numero} se encontra na lista')
       else:
              print(f"O número {numero} não se encontra na lista.")

def mostrar_Lista(lista):
     if lista:
       print("Números da lista:")
       for numero in lista:
        print(numero)
     else:
      print("A lista se encontra vazia")

def ordenar_Crescente(lista):    
      lista.sort()
      print("Lista em ordem crescente", lista)      

def ordenar_Decrescente(lista):
         lista.sort(reverse=True)
         print("Lista ordenada de forma decrescente", lista)


if __name__ == "__main__":

    principal()
