# Les variables sont nommées en snake case
# Tous les mots sont en minuscules séparées par un underscore
# Le caractère '=' permet d'affecter une valeur à une variable
ma_variable = 12

# variable = valeur à stocker
ma_variable = "Toto"

ma_variable = True

# Pour afficher des éléments dans le terminal, on utilise la fonction print pré-implémenté dans Python
print(ma_variable)  # Affiche True

# Les numériques

## Les entiers
mon_entier = 12
print(type(mon_entier))  # int

## Les nombres à virgule
mon_nombre_a_virgule = 14.124
print(type(mon_nombre_a_virgule))  # float

# /!\ Toujours utiliser un '.' et pas une virgule pour les nombres à virgule
mon_nombre_a_virgule_bis = 14, 124, "toto"  
print(mon_nombre_a_virgule_bis) # liste d'éléments!
print(type(mon_nombre_a_virgule_bis)) # tuple

# Les chaînes de caractères
## Les deux syntaxes suivantes sont les mêmes!
ma_chaine = "Arthur"
ma_chaine_2 = 'Emmie'

# Permet de créer une chaîne multilignes sans utiliser le caractère spécial `\n`
ma_chaine_3 = """Margot
est
souriante
aujourd'hui
et demain
on verra"""
ma_chaine_4 = 'Aujourd\'hui'
# Cette chaîne de caractère revient à la même chose que ma_chaine_3
ma_chaine_5 = "Margot\nest\nsouriante\naujourd'hui\net demain\non verra"

# Dupliquer une ligne de code: ALT (OPTION) + SHIFT + Flèche du bas
print(ma_chaine)
print(ma_chaine_2)
print(ma_chaine_3)
print(ma_chaine_4)
print(ma_chaine_5)

print("Bonjour Toto,\nComment vas-tu ?")

# Les booléens
## Un booléen peut prendre deux valeurs: Vrai ou Faux
mon_booleen = False 
mon_booleen = True

# None
## None représente l'absence de valeur
mon_chaine = None

# On peut transformer des variables d'un type à un autre
nombre_chaine = "12.3"
print(type(nombre_chaine))

# Cette opération s'appelle le casting
# On utilise le type dans lequel on souhaite transformer la variable avec les parenthèses
nombre = float(nombre_chaine)
print(type(nombre))

# Garder la partie entière du nombre
entier = int(nombre)
print(entier)

# Transformer une chaîne qui contient des caractères provoque une erreur dans le script
# float(ma_chaine)