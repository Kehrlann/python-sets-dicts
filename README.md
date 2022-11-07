# Sets and dictionnaries

## Consignes générales

Pour le rendu, remplissez **uniquement les fonctions** dans les fichiers désignés, veillez bien à n'ajouter aucun autre code dans ces fichiers. Évaluez votre note en local de temps en temps (cf ci-dessous).

## Rendre votre travail

Quand le résultat pour un des exercices est satisfaisant, git add, git commit, git push:

```shell
$ git add dict-struct.py
$ # ajoutez aussi tout autre fichier que vous voulez committer
$ git commit --message "Dict as struct, finished"
$ git push
```

Rendus **obligatoires**:

⛔️⛔️⛔️⛔️⛔️⛔️⛔️
⛔️ TODO
⛔️⛔️⛔️⛔️⛔️⛔️⛔️

Rendus facultatifs:

⛔️⛔️⛔️⛔️⛔️⛔️⛔️
⛔️ TODO
⛔️⛔️⛔️⛔️⛔️⛔️⛔️

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.

## Exercice 1 - Les départements

Dans le fichier `communes-departement-region.csv`, vous trouverez une base de données des communes de France. Complétez le fichier
`departements.py` pour en extraire l'ensemble des départements en France. Il y a 101 départements. Chaque ligne représente une commune,
au format CSV (comma-separated-values), c'est à dire des "colonnes" de tableau délimitées par des virgules. Par exemple:

```
75105,PARIS 05,75005,PARIS,,48.8445086596,2.34985938556,105,,Paris 05,Paris 05,75,Paris,11,Île-de-France
```

Attention:
- Les données ne sont pas 100% "propres", il peut y avoir des lignes avec des données manquantes
- Le fichier commence par une ligne d'en-tête, qui n'est pas une entrée à proprement parler, mais la description de chacune des colonnes.


## Exercice 2 - Génération aléatoire de personnes

Dans le fichier `personnes.py`, écrivez une fonction `read` qui permet de lire des fichiers tels que `sample_people.txt`

```
Marie Durand 2022-25-12
Jean Dupont 2001-11-12
Camille Saint-Nazaire 2000-04-15
```

Écrivez une fonction qui lit ce genre de fichiers et qui retourne les données sous la forme d’une liste de dictionnaires. 
Quelles seraient les clés à utiliser pour ces dictionnaires ? (Le grader pourra vous aider).


A partir des deux fichiers joints, remplissez la fonction `create`:

* `last_names.txt`  
  (dérivé de [cette liste](https://fr.wikipedia.org/wiki/Liste_des_noms_de_famille_les_plus_courants_en_France))
* `first_names.txt`  
  (dérivé de [cette liste](https://fr.wikipedia.org/wiki/Liste_des_pr%C3%A9noms_les_plus_donn%C3%A9s_en_France))

* fabriquez un jeu de données aléatoires contenant 10000 personnes  
  avec la contrainte qu'il y ait en sortie **unicité du nom x prénom**  
* pour les dates de naissance tirez au sort une date entre le 01/01/2000 et le 31/12/2004
* rangez cela dans le fichier `data-big.txt` (pas la peine de committer!)
* vous devez produire ce fichier dans un temps de l'ordre de 50-100ms


**indice** Pour choisir un élément au hasard dans un itérable, voir le module `random`.
**indice** Pour la date, voir les modules `datetime.date`, et `datetime.timedelta`.

## Exercice 3 - Implémentation d'un Set pour les chaînes de caractère

Dans le fichier `custom_set.py`, implémentez un ensemble simple pour les chaînes de caractères. Les fonctions
`create` et `hash_string` sont fournies. Vous devez implémenter:
- `add`
- `contains`
- `size`

L'ensemble ne doit pas contenir de doublons, et `contains` doit être beaucoup plus rapide que la recherche dans
une simple liste.

Exemple d'utilisation:

```python
>>> my_set = create()
>>> add(my_set, "foo")
>>> add(my_set, "foo")
>>> add(my_set, "bar")
>>> contains(my_set, "foo")
True
>>> contains(my_set, "bar")
True
>>> contains(my_set, "quux")
False
>> size(my_set)
2
```

**indice** En regardant le fichier

## License

La base de données des communes est en ODbL, fournie sur data.gouv.fr par Mohamed Badaoui, utilisée sans modifications, export du 2022-11-07 - [source](https://www.data.gouv.fr/fr/datasets/communes-de-france-base-des-codes-postaux/#resources)



All exercises above are licensed _CC BY-NC-ND, Thierry Parmentelat_

- [Palindrome](https://github.com/ue12-p22/python/blob/70e65198dbe5efa84608842c327286b7218f5807/notebooks/2-09-exos.py) (added examples)
- [Comptage dans un fichier](https://github.com/flotpython/course/blob/71e4a51e4832cc5e070b9a26bd3deedf576138a0/w3/w3-s2-x1-comptage.md) (trimmed examples)
- [Calculatruce](https://github.com/flotpython/course/blob/71e4a51e4832cc5e070b9a26bd3deedf576138a0/w6/w6-s9-x1b-postfix.md) (added examples)

