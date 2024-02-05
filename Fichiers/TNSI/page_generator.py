import random

TAGS = ["Musique",
        "Cuisine",
        "Jeux",
        "Informatique",
        "Sport",
        "Science",
        "Cinema",
        "Actualités"]

def page(i, tags, liens):
    res = f"""
    <!DOCTYPE html>
    <html>
    	<head>
    		<meta charset = "utf-8">
    		<title>Page {i}</title>
    	</head>



    	<body>

            <h1>Tags</h1>
                <ul>
    """
    for tag in tags:
        res += f"\t\t\t\t<li>{tag}</li>\n"

    res += f"""
                </ul>
            <h1>Liens</h1>
                <ul>
    """

    for j in liens:
        res += f'\t\t\t\t<li><a href = "page_{j:02}.html"> Lien vers la page {j}</a></li>\n'
    res += """
                </ul>
    	</body>

    </html>
    """
    return res


for i in range(100):

    nb_tag = random.randint(1,3)
    tags = set()
    while len(tags) < nb_tag:
        tags.add(random.choice(TAGS))

    nb_link = random.randint(1, 10)
    liens = set()
    while len(liens) < nb_link:
        liens.add(random.randint(0,99))

    name = f"page_{i:02}.html"
    with open(name, 'w', encoding="utf-8") as f:
        f.write(page(i, tags, liens))
