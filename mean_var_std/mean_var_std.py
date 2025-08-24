# mean_var_std.py
import numpy as np

def calculate(lst):
    # A FCC checa exatamente essa mensagem quando a lista não tem 9 números
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),   # por colunas
            arr.mean(axis=1).tolist(),   # por linhas
            arr.mean().item()            # flatten
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().item()
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().item()
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().item()
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().item()
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().item()
        ]
    }

    return calculations


if __name__ == "__main__":
    # Exemplo rápido (mesmo do enunciado da FCC)
    print(calculate([0,1,2,3,4,5,6,7,8]))
