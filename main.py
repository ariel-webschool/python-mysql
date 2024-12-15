from models.Users import Users
print("Gestion des utilisateur")

# CRUD
handler = Users()
# handler.add("Jordan","Jesuisengardecesoir")
# handler.delete("Jordan")
# handler.all()

# handler.update({"name":"Ariel","password":"Jeveuxmanger"})
# handler.all()

handler.find("Ariel")
