produto = {
    "nome": "Caderno",
    "preço": 15.90,
    "estoque": 100
}

print(f"Produto: {produto['nome']}")
print(f"Preço: R$ {produto['preço']:.2f}")

produto["estoque"] += 5

print(f"Dicionário atualizado: {produto}")