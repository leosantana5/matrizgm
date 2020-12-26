# Meta caracteres: . ^$ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres
# * 0 ou n(ilimitado)
# + 1 ou n(ilimitao)
# ? 0 ou 1
# {n} qualquer quantidade
# {min, max}

import re

texto = '''
00088-2 VISITAS SEMANAIS   0001 00001 SP SAO PAULO                 LIMAO                    AV. INAJAR DE SOUZA/ ORLANDO MARCH,6 00000006226969       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0002 00002 SP SAO PAULO                 CHACARA NOSSA SENHORA DO RUA NOSSA SENHORA DO BOM CONSELHO,25 00000006603689       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0003 00003 SP SAO PAULO                 VILA ALMEIDA             AV. DAS NACOES UNIDAS,22613          00000006839288       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0004 00004 SP SAO PAULO                 VILA LAGEADO             AV. CORIFEU DE AZEVEDO MARQUES,3672  00000006173986       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0005 00005 SP OSASCO                    SAO PEDRO                RUA LUIS HENRIQUE DE OLIVEIRA,46     00000006566373       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0006 00006 SP SAO PAULO                 MOOCA - HIPODROMO        VIADUTO ALCANTARA MACHADO,2078       00000006266039       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0007 00007 SP SANTO ANDRE               CASA BRANCA              AV. SANTOS DUMONT,1001               00000006636180       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0008 00008 SP SAO PAULO                 IPIRANGA                 RUA DO MANIFESTO,1183                00000006693505       249,92          0,00  01/10/2020 31/10/2020
00088-2 VISITAS SEMANAIS   0009 00009 SP SAO PAULO                 ITAIM PAULISTA           AV. MARECHAL TITO,5768 LJ 2          00000006701044       249,92          0,00  01/10/2020 31/10/2020
'''


print(re.findall(r'^([0-9]{5,5})\-([a-zA-Z0-9ÉÁÇ\/:, \s-]{20,20})([ ]{1,1})([0-9]{4,4})([ ]{1,1})([0-9]{5,5})([ ]{1,1})([A-Z]{2,2})([ ]{1,1})([a-zA-ZÉÁÇ\/:, \s-]{25,25})([ ]{1,1})([a-zA-Z0-9ÉÁÃÓÇÓÍ\/:, \s-]{24,24})([ ]{1,1})([a-zA-Z0-9-ÉÁÃÇÓ\/:, \s.]{36,36})([ ]{1,1})([0-9 ]{14,14})([ ]{1,1})([0-9,. ]{12,12})([ ]{1,1})([0-9,. ]{13,13})([ ]{1,1})([0-9/,. ]{11,11})([ ]{1,1})([0-9/,. ]{10,10})',texto))


