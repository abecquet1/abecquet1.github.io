import xml.dom.minidom as dom
doc1 = dom.parse("recette.xml") #pour importer un fichier xml 
doc2 = dom.parseString("<a><b>coucou</b></a>") #pour transformer une chaîne de caractère bien formée
