import unittest
from departements import find_departements
from tempfile import TemporaryDirectory
from shutil import copyfile
from pathlib import Path


class TestDepartements(unittest.TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)
        self.input = self.test_path / "communes-departement-region.csv"
        copyfile(Path(".github") / "communes-departement-region.csv", self.input)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_uses_set(self):
        self.assertIsInstance(find_departements(
            self.input), set, "find_departments doit renvoyer un ensemble")

    def test_size(self):
        self.assertEqual(len(find_departements(self.input)),
                         101, "il y a 101 départments dans la liste")


if __name__ == '__main__':
    unittest.main(verbosity=2)
