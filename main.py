from src.Extract import Extract
from src.load import Load

def iniciar():
    ext = Extract()
    ld = Load()
    ano = 2022

    for f in ["export", "import"]:
        print(f"[*] Coletando {f} de Recife...")
        dados = ext.extract_comex_recife(f, ano)
        ld.create_comex_table(dados, "comex_recife", "balanca_comercial", ano)

if __name__ == "__main__":
    iniciar()