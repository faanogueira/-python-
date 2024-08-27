
nome = str( input( 'Digite o nome do cliente: ' ) )
dia_v = str( input( 'Digite o dia de vencimento: ' ) )
mes_v = str( input( 'Digite o mês de vencimento: ' ) )
valor = str( input( 'Digite o valor da fatura: ' ) )


print( 'Olá, {}'.format(nome))
print(f"A sua fatura com vencimento em {dia_v} de {mes_v}, no valor de R$ {valor} está fechada.")