from geopy.distance import geodesic
from geopy.distance import great_circle


cds_1 = (-23.421531, -46.527697)
cds_2 = (-23.523583, -46.628641)

destino = "Rua Professor Eldemar Alves de Oliveira, 176"
origem = "Rua Eduardo Chaves, 183"

print(geodesic(cds_1, cds_2))
print(great_circle(cds_1, cds_2))

Anp6aw78wQ0gJrzuzbkUBoGF04IjYJBsL8kWU_15hV0FPAU8Kf916T9SR5I-BOmz