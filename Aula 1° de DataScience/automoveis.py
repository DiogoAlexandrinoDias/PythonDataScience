nome = str(input("Digite o nome do Veículo: "))
precoOriginal = float(input("Digite o preço do Veículo: "))

desconto = int(input("Escolha entre 60%, 30% ou 0% de desconto:"))

if desconto == 0:
    print(f"Preço original: {precoOriginal}")
elif desconto == 30:
    precoFinal = precoOriginal * 0.3
    print(f"Preço original: {precoOriginal}")
    print(f"O preço com desconto é: {precoFinal}")
elif desconto == 60:
    precoFinal = precoOriginal * 0.6
    print(f"Preço original: {precoOriginal}")
    print(f"O preço com desconto é: {precoFinal}")
