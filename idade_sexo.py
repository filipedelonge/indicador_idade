def main():
    try:
        # Solicita que o usuário insira o sexo (M ou F) e converte para letras maiúsculas para evitar problemas de sensibilidade a maiúsculas/minúsculas.
        sexo = input("Digite o sexo (M ou F): ").strip().upper()
        # Solicita que o usuário insira a idade.
        idade = int(input("Digite a idade: "))

        # Verifica se a idade é menor ou igual a 9.
        if idade <= 9:
            if sexo == "M":
                print("É uma criança do sexo masculino.")
            elif sexo == "F":
                print("É uma criança do sexo feminino.")
            else:
                # Se o sexo não for 'M' nem 'F, exibe uma mensagem de erro.
                print("Sexo inválido. Por favor, digite 'M' ou 'F'.")
        else:
            # Se a idade não for menor ou igual a 9, a pessoa não é uma criança.
            print("Não é uma criança.")
    except ValueError:
        # Tratamento de erro se o usuário não inserir uma idade válida como número inteiro.
        print("Idade deve ser um número inteiro.")
    except KeyboardInterrupt:
        # Tratamento de erro se o usuário interromper a operação.
        print("\nOperação interrompida pelo usuário.")

if __name__ == "__main__":
    main()