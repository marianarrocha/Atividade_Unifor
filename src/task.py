import pandas as pd

class CustomerReport:
    def __init__(self):
        self.nome = "CustomerReport"

    def executar(self):
        df = pd.read_csv(r'C:\Users\Maria\Desktop\portifolio\Data\dados brutos\Customer_report_cleaned_data.csv',encoding='latin1')
        print(f"{self.nome} carregado com sucesso.")
        return df
