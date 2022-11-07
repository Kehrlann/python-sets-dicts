import unittest
from personnes import read, create
from tempfile import TemporaryDirectory
from shutil import copyfile
from os import remove, path
from pathlib import Path
from datetime import date


class TestPersonnes(unittest.TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        self.input = self.test_path / "sample_people.txt"
        copyfile(Path(".github") / "sample_people.txt", self.input)
        if path.isfile("data-big.txt"):
            remove("data-big.txt")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_reads(self):
        personnes = read(self.input)
        self.assertIsInstance(
            personnes, list, "La fonction 'personnes' doit retourner une liste")
        self.assertEqual(len(personnes), 3,
                         "Le fichier sample_people.txt contient 3 personnes")

        first = personnes[0]
        self.assertIsInstance(
            first, dict, "Chaque élément de la liste doit être un dictionnaire")
        self.assertTrue(
            "nom" in first, "Le dictionnaire représentant une personne doit contenir la clef 'nom'")
        self.assertTrue(
            "prenom" in first, "Le dictionnaire représentant une personne doit contenir la clef 'prenom'")
        self.assertTrue("date_naissance" in first,
                        "Le dictionnaire représentant une personne doit contenir la clef 'date_naissance'")

    def test_creates_file(self):
        create()
        self.assertTrue(path.isfile("data-big.txt"),
                        "La fonction create doit générer un fichier data-big.txt")
        with open("data-big.txt", 'r') as f:
            prenom_nom_set = set()
            prenom_nom_list = []
            for line in f:
                prenom, nom, date_naissance = line.strip().split(' ')
                prenom_nom_set.add(prenom + nom)
                prenom_nom_list.append(prenom + nom)

                try:
                    parsed_date = date.fromisoformat(date_naissance)
                except:
                    self.fail(
                        f"La date [{date_naissance}] doit être au format AAAA-MM-JJ (ISO-8601)")
                self.assertGreaterEqual(parsed_date, date(
                    2000, 1, 1), "La date de naissance doit être >= 2000-01-01")
                self.assertLessEqual(parsed_date, date(
                    2004, 12, 31), "La date de naissance doit être <= 2004-12-31")

            self.assertEqual(len(prenom_nom_list), 1000,
                             "La fonction doit générer 1000 personnes")
            self.assertEqual(len(prenom_nom_set), 1000,
                             "Les (prenom x nom) doivent être uniques")

    def test_is_random(self):
        create()
        contents = None
        with open("data-big.txt", 'r') as f:
            contents = f.read()
        create()
        with open("data-big.txt", 'r') as f:
            self.assertNotEqual(contents, f.read(
            ), "create() doit produire des contenus aléatoires, pas deux fois la même chose")


if __name__ == '__main__':
    unittest.main(verbosity=2)
