"""
Exercice 6 : ordre de fabrication (moyen-difficile, 35 min)

Dans un ERP, certains produits doivent être fabriqués avant d’autres.
Écris ordre_fabrication(dependances: dict[str, list[str]]) -> list[str].

dependances["vélo"] = ["cadre", "roue"] signifie que le cadre et la roue doivent
être fabriqués avant le vélo.
Renvoie un ordre de fabrication valide.
S’il y a une dépendance circulaire, lève une exception ValueError avec un
message clair.

ordre_fabrication({
    "vélo": ["cadre", "roue"],
    "roue": ["rayon", "pneu"],
    "cadre": [],
})
# ex. ["cadre", "rayon", "pneu", "roue", "vélo"] (d'autres ordres sont valides)

ordre_fabrication({"a": ["b"], "b": ["a"]})  # ValueError

Indice si tu bloques plus de 15 minutes : cherche « tri topologique ».
"""