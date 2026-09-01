from desconto import Normal, Vip, Premium

desconto_normal = Normal()
desconto_vip = Vip()
desconto_premium = Premium()

valor = float(input("Digite o valor do produto: "))

if valor <= 100:
    desconto = desconto_normal.calcular(valor)
elif valor <= 500:
    desconto = desconto_vip.calcular(valor)
else:
    desconto = desconto_premium.calcular(valor)

valor_final = valor - desconto
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")