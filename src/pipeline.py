from task import CustomerReport
from transformar import TransformarCustomerReport
from carregar import Carregar
from logger import configurar_logger

def executar_pipeline_customer_report():
    logger = configurar_logger()
    logger.info("Iniciando pipeline do CustomerReport...")

    extrair = CustomerReport()
    df = extrair.executar()

    transformar = TransformarCustomerReport()
    df_tratado = transformar.executar(df)

    carregar = Carregar()
    carregar.executar(df_tratado)

    logger.info("Pipeline finalizada com sucesso.")

    # python src/pipeline.py