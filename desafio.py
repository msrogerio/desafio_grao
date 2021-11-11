"""
João está começando a investir e semanalmente, ele vai investir com a Grão R$ 100,00 
e queremos mostrar para João quanto ele terá poupado e quanto o seu dinheiro terá 
rendido daqui 36 semanas. 

Para isso temos algumas regras:
 - Consideramos que a Taxa Selic seja de 4,25% ao ano
 - Pagamos 100% da Taxa Selic
 - Que o ano tem 252 dias úteis
 - Só rentabilizamos dias úteis (não se preocupe com feriados)
 - Desconsiderar Impostos sobre os investimentos

A fórmula para o cálculo da rentabilidade é ```M = P . (1 + i) ^ t/252```
"""

# Valor investido pelo João ao longo de 36 semanas 
total_investido = 100*36 

# Decrementa dois dias (sábado e domingo) para cada semana do total des dias resultantes
# das semanas
dias_uteis_de_investimento = (36*7)-(36*2) 

# Monta a proporção dos juros com base nos dias de investimento 
# e valor integral da Taxa Selic
taxa_de_juros_considerada = (dias_uteis_de_investimento*4.25)/252

# Calcula a porcentagem do investimento total
valor_rendido = total_investido*(taxa_de_juros_considerada/100)

# Soma ao valor investido
valor_pos_investimento = total_investido+valor_rendido


# %.2f arredonda o valor para duas casas decimais
print('Investimento inicial: R$ %.2f' % total_investido)
print('Prazo de investimento: %d meses' % ((365/7)/12))
print('Total de ganhos: R$ %.2f' % valor_rendido)
print('Retorno Total: R$ %.2f' % valor_pos_investimento)