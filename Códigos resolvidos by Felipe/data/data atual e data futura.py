""" Carregue a data atual do computador e,
 com base na data atual, apresente a data de dois dias no futuro - Código by felipe"""

from datetime import datetime, timedelta

data_atual = datetime.now()
data_futura = data_atual + timedelta(2)
print("A data atual e {} a data daqui 2 dias sera {}".format(data_atual, data_futura))

