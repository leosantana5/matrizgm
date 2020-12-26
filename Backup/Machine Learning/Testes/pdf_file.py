import pandas as pd
import io
import re
import tabula

# df = tabula.read_pdf("batata.pdf", pages="all")
# tabula.convert_into("batata.pdf", "batata.csv", pages="all")
base = io.open("batata.csv", encoding='latin-1')
base2 = pd.DataFrame(base).to_numpy()
#
# pattern_empresa = r'^([\d A-ZÃÂÕÔÇÉÊÁÀÍ-]+)(Relatório)'
#
# pattern_loja = r'^([0-9]{5,5})\-([a-zA-Z0-9ÉÁÇ\/:, \s-]{21,21})([0-9]{4,4})([ ]{1,1})([0-9]{5,5})([ ]{1,1})([A-Z]{2,2})([ ]{1,1})([a-zA-ZÉÁÇ\/:, \s-]{25,25})([ ]{1,1})([a-zA-Z0-9ÉÁÃÓÇÓÍ\/:, \s-]{24,24})([ ]{1,1})([a-zA-Z0-9-ÉÁÃÇÓ\/:, \s.]{36,36})([ ]{1,1})([0-9 ]{14,14})([ ]{1,1})([0-9,. ]{12,12})([ ]{1,1})([0-9,. ]{13,17})([ ]{1,1})([0-9/,. ]{11,11})([ ]{1,1})([0-9/,. ]{10,10})'
#
# pattern_nome_da_rede = r'^(Rede No )([0-9]{4,4})( - )([\d A-ZÃÂÕÔÇÉÊÁÀÍ?-]+)'
#
# pattern_nome_do_cliente = r'^(Cliente: )([0-9 ]{5,8})(CNPJ: )([0-9.  \/-]{18,18})( - )([\d A-ZÃÂÕÔÇÉÊÁÀÍ\/]+)( - )([\d A-ZÃÂÕÔÇÉÊÁÀÍ\/]+)'
#
# pattern_epi = r'^([0-9]{5,5})\-([A-Z ?]{22,22})([0-9]{4,4})\ ([0-9]{5,5})\ ([A-Z]{2,2})\ ([a-zA-Z-ÉÁÃÇÓ\/:? \s.]+)([0-9,]+)([0-9, ]{14,14})\ +([0-9\/]{10,10})\ +([0-9\/]{10,10})'

pattern_lojas_exata = r"^([0-9 ]{6,6})\ (([0-9.\/-]{18,18}|[ ]{18,18})\ ([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&' 0-9-,\/.?]{37,37})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-,.]{50,50})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/|0-9-,.]{21,21})([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-|,.]{20,20})([A-Z]{2,2})\ |([ ]{1,1})([ ]{18,18})([ ]{1,1})([ ]{37,37})([ ]{50,50})([ ]{20,20})([ ]{20,20})([ ]{2,2})([ ]{1,1}))([a-zA-ZÂÃÁÍÓÕÔÈÉÊÇÚÜüñ()`´&'? \/0-9-,.]+)"
#
# empresa = ''
# rede = ''
# cliente = ''

for i in base2:

    a = str(i[0]).replace('?', "").replace("]", "")

    linha = re.findall(pattern_lojas_exata, a)


    if linha != []:
        linha = linha[0]
        codloja = linha[0]
        cnpj = linha[1]

        print(codloja, cnpj)


    else:
        print(f'{a} %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


    # if linha != []:
    #     linha = linha[0]
    #     codloja = int(linha[0])
    #     cnpj_loja = str(linha[1])
    #     nome_loja_exata = str(linha[2])
    #
    #     print(codloja, cnpj_loja)


# for i in base2:
#     a= str(i[0]).replace('\n', '').replace('"', '')
#
#     if re.findall(pattern_empresa, a) != []:
#         re_empresa = re.findall(pattern_empresa, a)
#         valores_empresa_faturada = re_empresa[0]
#         empresa = ''
#         empresa = valores_empresa_faturada[0].strip().replace('?', "")
#         linha = {
#             "empresa":valores_empresa_faturada[0].strip().replace('?', "")
#         }
#
#         print(linha)
#
#     elif re.findall(pattern_nome_do_cliente, a) != []:
#         re_nome_do_cliente = re.findall(pattern_nome_do_cliente, a)
#         valores_do_cliente = re_nome_do_cliente[0]
#         cliente = ''
#
#
#         linha = {
#             "codcliente":valores_do_cliente[1].strip(),
#             "cnpj":valores_do_cliente[3].strip(),
#             "razaosocial":valores_do_cliente[5].strip(),
#             "fantasia":valores_do_cliente[7].strip()
#         }
#         cliente = linha
#         print(linha)
#
#     elif re.findall(pattern_nome_da_rede, a) != []:
#         re_nome_da_rede = re.findall(pattern_nome_da_rede, a)
#         valores_da_rede = re_nome_da_rede[0]
#         rede = ''
#         rede = (valores_da_rede[3]).replace(' ?', "'")
#
#         linha = {
#             "codbandeira":valores_da_rede[1].strip().replace(' ?', "'"),
#             "bandeira":valores_da_rede[3].strip().replace(' ?', "'")
#
#         }
#         print(linha)
#
#     elif re.findall(pattern_epi, a) != []:
#         re_epi = re.findall(pattern_epi, a)
#         valores_epi = re_epi[0]
#
#         linha = {
#             "codtarefa":valores_epi[0].strip().replace(' ?', "'"),
#             "descricaotarefa":valores_epi[1].strip().replace(' ?', "'"),
#             "reflinhafat":valores_epi[2].strip().replace(' ?', "'"),
#             "epi":valores_epi[4].strip().replace(' ?', "'"),
#             "valorparcelaepi":valores_epi[5].strip().replace(' ?', "'").replace(",", "."),
#             "valor13epi":valores_epi[6].strip().replace(' ?', "'").replace(",", "."),
#             "data_iniciofat_epi_exata":valores_epi[7].strip().replace(' ?', "'"),
#             "data_fimfat_epi_exata":valores_epi[8].strip().replace(' ?', "'")
#
#         }
#         print(linha)
#
#
#
#
#     elif re.findall(pattern_loja, a) != []:
#         string2 = re.findall(pattern_loja, a)
#         valores = string2[0]
#
#         codfreq = valores[0].strip()
#         descricaofreq = valores[1].strip()
#         reflinhafat = valores[2].strip()
#         cod_loja_exata = valores[4].strip()
#         uf_loja_exata = valores[6].strip()
#         cidade_loja_exata = valores[8].strip()
#         bairro_loja_exata = valores[10].strip()
#         logradouro_loja_exata = valores[12].strip()
#         cnpj_loja_exata = valores[14].strip()
#         valor_mensal_exata = (valores[16].strip().replace(",", "."))
#         valor_parcela_13 = (valores[18].strip().replace(",", "."))
#         valor_total_loja = valor_mensal_exata + valor_parcela_13
#         data_iniciofat_loja_exata = valores[20].lstrip()
#         data_fimfat_loja_exata = valores[22].lstrip()
#
#         linha = {
#             "bandeira":rede,
#             "codfreq":codfreq,
#             "descricaofreq":descricaofreq,
#             "reflinhafat":reflinhafat,
#             "cod_loja_exata":cod_loja_exata,
#             "uf_loja_exata":uf_loja_exata,
#             "cidade_loja_exata":cidade_loja_exata,
#             "bairro_loja_exata":bairro_loja_exata,
#             "logradouro_loja_exata":logradouro_loja_exata,
#             "cnpj_loja_exata":cnpj_loja_exata,
#             "valor_mensal_exata":valor_mensal_exata,
#             "valor_parcela_13":valor_parcela_13,
#             "valor_total_loja":valor_total_loja,
#             "data_iniciofat_loja_exata":data_iniciofat_loja_exata,
#             "data_fimfat_loja_exata":data_fimfat_loja_exata,
#             "cliente":cliente,
#             "empresa":empresa
#         }
#         print(linha)
#
#     else:
#         a = ""
#
#
#
#
print("Feito")