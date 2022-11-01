# CALCUladora de idade com python, descubra sua idade com im simples codigo #

# imputs referentes ao ano mes e dia #
from datetime import datetime
ano_nasc = int (input('Digite o em que ano voçê nasceu ?'))
mes_nasc = int (input('Digite o mês voçê nasceu ?'))
dia_nasc = int(input(' Digite o dia em que voçê nasceu'))

data_nasc = datetime(ano_nasc, mes_nasc, dia_nasc)
data_atual = datetime.now ()

diff = data_atual - data_nasc
dias = diff . days 
anos, dia = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

# saida dos dados para a tela do usuário #
print(f'voçê tem {anos }anos , {meses}meses, e  {dias} dias !')

# by Flavio vinicio mota #
# @flavio.vms #