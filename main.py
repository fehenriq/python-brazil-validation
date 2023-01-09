from CPF_CNPJ import Documento
from telefonesBR import TelefonesBR
from datasBR import DatasBR
from acessoCEP import BuscaEndereco

cpf = "49142929806"
cnpj = "48936303000147"
celular = "5511993178823"
cep = "08625325"

print(Documento.cria_documento(cnpj))
print(Documento.cria_documento(cpf))
print(TelefonesBR(celular))
print(DatasBR())
print(DatasBR().mes_cadastro() + " " + DatasBR().dia_semana())
print(DatasBR().tempo_cadastro())
print(BuscaEndereco(cep))
print(BuscaEndereco(cep).acessa_via_cep())
