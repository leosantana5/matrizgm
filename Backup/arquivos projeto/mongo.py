# primeiro instalar as biblotecas ----------------

# pip install pymongo
# pip install pymongo[srv]

# import -------------------------------
import pymongo


# conexão com o banco -------------------
myclient = pymongo.MongoClient("mongodb+srv://admin:eliaslindo@scalper0.qgnlf.mongodb.net/scalpermaster?retryWrites=true&w=majority")
mydb = myclient["scalpermaster"]
mycol = "candlestick"

print(myclient.list_database_names()) #lista os bancos salvos
print(mydb.list_collection_names()) #Lista as collections salvas no banco

# adicionar um unico registro no banco
mydict1 = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

# adicionar mais de um registro no banco
mylist2 = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#procurar e listar valor para um unico campo-------------------------------
for x in mycol.find({},{ "address": 0 }):
  print(x)

#procurar e listar por uma pesquisa já pré determinada com campo selecionados ----------------------------

myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# update de informações----------------------------------------

myquery = {"address": "Valley 345"} #primeiro consulta
newvalues = {"$set": {"address": "Canyon 123"}}# novos valores para subistituição

mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
  print(x)