from datetime import datetime, timedelta

class DatasBR:
  def __init__(self):
    self.momento_cadastro = datetime.today()
    
  def mes_cadastro(self):
    meses_do_ano = [
      "Janeiro", "Fevereiro", "Março",
      "Abril", "Maio", "Junho", "Julho",
      "Agosto", "Setembro", "Outubro",
      "Novembro", "Dezembro"
    ]
    mes_cadastro = self.momento_cadastro.month - 1
    return meses_do_ano[mes_cadastro]
  
  def dia_semana(self):
    dias_da_semana = [
      "Segunda-feira", "Terça-feira",
      "Quarta-feira", "Quinta-feira",
      "Sexta-feira", "Sábado", "Domingo"
    ]
    dia_cadastro = self.momento_cadastro.weekday()
    return dias_da_semana[dia_cadastro]
  
  def formata(self):
    data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    return data_formatada
  
  def __str__(self):
    return self.formata()
  
  def tempo_cadastro(self):
    tempo = (datetime.today() + timedelta(weeks=3, days=30)) - self.momento_cadastro
    return str(tempo.days) + " dias"