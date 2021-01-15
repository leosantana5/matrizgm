import tabula

def convert():
    pdf = input(f"Insira o nome do arquivo em pdf: ")
    csv = input(f"Insira o nome do arquivo convertido: ")
    nome_pdf = f"{pdf}.pdf"
    nome_csv = f"{csv}.csv"

    print("")
    print("Convertendo arquivo")
    tabula.convert_into(nome_pdf, nome_csv, pages="all")
    print(f"Arquivo convertido - {nome_csv}")


convert()