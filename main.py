from CPF_CNPJ import Documento
from telefonesBR import TelefonesBR
from datasBR import DatasBR

from datetime import datetime, timedelta

# print(Documento.cria_documento("48936303000147"))
# print(Documento.cria_documento("49142929806"))
# print(TelefonesBR("5511993178823"))

# print(DatasBR().mes_cadastro() + " " + DatasBR().dia_semana())

print(DatasBR().tempo_cadastro())