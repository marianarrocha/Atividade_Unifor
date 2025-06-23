import pandas as pd
import os

class Carregar:
    def __init__(self):
        self.nome = "Carregar"

    def executar(self, df, nome_arquivo=r'C:\Users\Maria\Desktop\portifolio\Data\dados tratados\customer_report_tratado.csv'):
        
        os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)

        df.to_csv(nome_arquivo, index=False)

        print(f"{self.nome} concluída. Dados salvos em: {nome_arquivo}")