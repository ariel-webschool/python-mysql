from models.Users import Users
print("Api de Gestion des utilisateurs")

# la class Users est notre Model
# il se connecte a la base de donnee
# et fait sa requete:
# - add():	ajout d'un utilisateur
# - delete():	suppression d'un utilisateur
# - update():	met a jour un utilisateur
# - all():	recupere la liste de tous les utilisateurs.

handler = Users()
# Ajout
# handler.add("Jordan","Jesuisengardecesoir")
# handler.all()

# Supprression
# handler.delete("Jordan")
# handler.all()

# Met a jour
# handler.update({"name":"Ariel","password":"Jeveuxmanger"})
# handler.all()

# Recupere un utilisateur specifique
# handler.find("Ariel")
