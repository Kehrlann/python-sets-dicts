__SET_CAPACITY = 1000


def create():
    """
    La fonction create renvoie un nouveau "set" custom,
    pas un "vrai" set python.
    """
    return [None] * __SET_CAPACITY


def hash_string(entry):
    """
    Fonction de hash à utiliser pour le set.
    """
    return int.from_bytes(entry.encode(), byteorder='big') % __SET_CAPACITY


def add(set, entry):
    """
    La fonction add permet d'ajouter l'entrée "entry" au set "set",
    si elle n'est pas déjà présente.
    """
    pass


def contains(set: list, entry: str):
    """
    La fonction contains renvoie True si "entry" est dans le "set",
    et "False" sinon.

    Exemple:

    >>> my_set = create()
    >>> add(my_set, "foo")
    >>> contains(my_set, "foo")
    True
    >>> contains(my_set, "bar")
    False
    """
    pass


def size(set: list):
    """
    La fonction size renvoie le nombre d'éléments dans le set.

    Exemple:

    >>> my_set = create()
    >>> add(my_set, "foo")
    >>> add(my_set, "bar")
    >>> add(my_set, "foo")
    >>> size(my_set)
    2
    """
    pass
