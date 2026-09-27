# Empresa: TudoWeb Marketing
# Projeto: Pesquisa de Satisfação no Atendimento ao Cliente

def main():
    TOTAL_ENTREVISTADOS = 50  # Quantidade final definida no enunciado

    qtd_excelente = 0
    qtd_bom = 0
    qtd_ruim = 0

    print("=============================================")
    print("   PESQUISA DE SATISFAÇÃO - TUDOWEB MARKETING   ")
    print("=============================================\n")

    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        
        nome = input("Digite o nome: ").strip()
        
        while True:
            try:
                idade = int(input("Digite a idade: "))
                if idade > 0:
                    break
                else:
                    print("Por favor, digite uma idade válida (maior que 0).")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro para a idade.")

        while True:
            print("Qual a sua opinião sobre o atendimento prestado?")
            print("1 - EXCELENTE")
            print("2 - BOM")
            print("3 - RUIM")
            
            opcao = input("Digite a opção (1, 2 ou 3): ").strip()

            if opcao == "1":
                qtd_excelente += 1
                break
            elif opcao == "2":
                qtd_bom += 1
                break
            elif opcao == "3":
                qtd_ruim += 1
                break
            else:
                print("\n[ERRO] Opção inválida! Escolha apenas 1, 2 ou 3.\n")

        print("-" * 35 + "\n")

    print("=============================================")
    print("            RESULTADO DA PESQUISA            ")
    print("=============================================")
    print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
    print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
    print(f"   (Quantidade de respostas 'BOM': {qtd_bom})")
    print("=============================================")

if __name__ == "__main__":
    main()