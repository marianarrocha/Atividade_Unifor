import logging
import os

def configurar_logger(nome_arquivo='pipeline.log'):
    os.makedirs('logs', exist_ok=True)
    caminho_log = os.path.join('logs', nome_arquivo)

    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a' 
    )
    
    return logging.getLogger()

# src/logger.py