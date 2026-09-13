
def calcular_desconto():
    # Solicita o valor total da compra
    try:
        valor_compra = float(input("Digite o valor total da compra (R$): "))
        if valor_compra <= 0:
            print("Digite um valor maior que zero.")
            return
    except ValueError:
        print("Entrada inválida. Digite apenas números para o valor da compra.")
        return

    # Determina a porcentagem de desconto com base nas regras progressivas
    if valor_compra < 200.00:
        percentual_desconto = 0.05  # 5%
    elif valor_compra < 300.00:
        percentual_desconto = 0.10  # 10%
    else:
        percentual_desconto = 0.15  # 15%

    # Calcula os valores finais sem repetições de fórmulas
    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    # Exibe os resultados para o usuário
    print("\n" + "=" * 30)
    print("RESUMO DA COMPRA")
    print("=" * 30)
    print(f"Valor original:       R$ {valor_compra:8.2f}")
    print(f"Desconto ({int(percentual_desconto * 100)}%):       R$ {valor_desconto:8.2f}")
    print("-" * 30)
    print(f"Valor total a pagar:  R$ {valor_final:8.2f}")
    print("=" * 30)

# Executa o programa
if __name__ == "__main__":
    calcular_desconto()
