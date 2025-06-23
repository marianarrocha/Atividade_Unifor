import pandas as pd

class TransformarCustomerReport:
    def __init__(self):
        self.nome = "TransformarCustomerReport"

    def executar(self, df):
        print(f"{self.nome} iniciada...")

        df = df.dropna(subset=['customer_key'])

        df = df.drop_duplicates(subset=['customer_key'])

        df['active_customer'] = df['recency'] < 90

        df = df[df['avg_monthly_value'] > 100]

        print(f"{self.nome} concluída. Total de linhas após tratamento: {len(df)}")

        return df
