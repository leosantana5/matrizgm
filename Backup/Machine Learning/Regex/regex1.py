import re

pattern = r'^([0-9]{5,5})\-([A-Z ?]{22,22})([0-9]{4,4})\ ([0-9]{5,5})\ ([A-Z]{2,2})\ ([a-zA-Z-ÉÁÃÇÓ\/:? \s.]+)([0-9,]+)([0-9, ]{14,14})\ ([0-9\/]{10,10})\ ([0-9\/]{10,10})'

valor = "00052-EPI ?S SEMESTRAL      0039 02699 SP EPI ?S                                                                                                        150,00          0,00  01/11/2020 30/11/2020"


def linha_faturamento (string):
    string2 = re.findall(pattern, string)
    valores = string2[0]

    # codfreq = valores[0].strip()
    # descricaofreq = valores[1].strip()
    # reflinhafat = valores[2].strip()
    # cod_loja_exata = valores[4].strip()
    # uf_loja_exata = valores[6].strip()
    # cidade_loja_exata = valores[8].strip()
    # bairro_loja_exata = valores[10].strip()
    # logradouro_loja_exata = valores[12].strip()
    # cnpj_loja_exata = valores[14].strip()
    # valor_mensal_exata = (valores[16].strip().replace(",", "."))
    # valor_parcela_13 = (valores[18].strip().replace(",", "."))
    # valor_total_loja = valor_mensal_exata + valor_parcela_13
    # data_iniciofat_loja_exata = valores[20].lstrip()
    # data_fimfat_loja_exata = valores[22].lstrip()

    return valores

print(linha_faturamento(valor))