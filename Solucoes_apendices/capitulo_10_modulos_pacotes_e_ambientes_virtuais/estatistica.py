def media(valores):
    return sum(valores) / len(valores)

def mediana(valores):
    v = sorted(valores)
    meio = len(v) // 2
    return v[meio] if len(v) % 2 else (v[meio - 1] + v[meio]) / 2

def main():
    dados = [3, 7, 1, 9, 4, 6]
    print("média:", media(dados), "mediana:", mediana(dados))

if __name__ == "__main__":
    main()      # só corre com: python estatistica.py
