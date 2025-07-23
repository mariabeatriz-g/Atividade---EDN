#Calculadora de Preço Total

#Informações do Produto

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = int(input("Insira a quantiade por favor: "))

#Cálculo de preço Total

preco_total = preco_unitario*quantidade

#Exibição das informações 

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço Total: R$", round(preco_total, 2)) 