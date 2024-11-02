import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from tqdm import tqdm

def gerar_dados(num_registros):
    # Criar uma lista de máquinas
    maquinas = [f"maquina{i}" for i in range(1, 10)]
    # Gerar datas aleatórias entre hoje e 4 dias atrás
    hoje = datetime.now()
    datas = []
   

    # Gerar registros
    registros = []
    for i in tqdm(range(num_registros), desc="Gerando"):
        data_aleatoria = hoje - timedelta(days=np.random.randint(0, 5))
        # Gerar horas, minutos e segundos aleatórios
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        segundo = random.randint(0, 59)
        # Combinar data e horário
        data_hora = data_aleatoria.replace(hour=hora, minute=minuto, second=segundo)
        registro = {
            "maquina": np.random.choice(maquinas),
            "data": data_hora,
            "temperatura": round(random.uniform(10.0, 80.0), 4)
        }
        registros.append(registro)

    return registros

def main():
    num_registros = 3000000  # 3 milhões de registros
    dados = gerar_dados(num_registros)

    # Criar um DataFrame do pandas
    df = pd.DataFrame(dados)

    # Salvar em um arquivo CSV
    df.to_csv('../dados/registros.csv', index=False)

    print("CSV gerado com sucesso!")

if __name__ == "__main__":
    main()
