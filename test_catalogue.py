from unittest import TestCase, main
from livre_s17 import Livre
import catalogue

class TestCatalogue(TestCase):
    def setUp(self):
       
        self.CATALOGUE = [
            Livre("1984", "Orwell", "9780451524935", 328, 1949),
            Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
            Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
            Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
        ]
        DOUBLON = Livre("1984 (réédition)", "Orwell", "9780451524935", 328, 1949)
        self.AVEC_DOUBLON = self.CATALOGUE + [DOUBLON]


    def test_trier_par_titre(self):
        self.assertEqual(
            catalogue.trier_par_titre(self.CATALOGUE),
            [
                Livre("1984", "Orwell", "9780451524935", 328, 1949),
                Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
                Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
                Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
            ],
        )


    def test_trier_par_annee(self):
        self.assertEqual(
            catalogue.trier_par_annee(self.CATALOGUE, True),
            [
                Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
                Livre("1984", "Orwell", "9780451524935", 328, 1949),
                Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
                Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
            ],
        )


    def test_trier_par_auteur_puis_annee_recente(self):
        self.assertEqual(
            catalogue.trier_par_auteur_puis_annee_recente(self.CATALOGUE),
            [
                Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
                Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
                Livre("1984", "Orwell", "9780451524935", 328, 1949),
                Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
            ],
        )


    def test_catalogue_non_change_apres_tri(self):
        catalogue.trier_par_annee(self.CATALOGUE)
        self.assertEqual(
            self.CATALOGUE,
            [
                Livre("1984", "Orwell", "9780451524935", 328, 1949),
                Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
                Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
                Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
            ]
        )


    def test_dedoublement_taille(self):
        self.assertEqual(len(catalogue.dedoublonner(self.AVEC_DOUBLON)), 4)


    def test_dedoublement_ordre(self):
        self.assertEqual(
            catalogue.dedoublonner(self.AVEC_DOUBLON)[0],
            Livre("1984", "Orwell", "9780451524935", 328, 1949),
        )

    def test_len_groupe(self):
        g = catalogue.regrouper_par_auteur(self.CATALOGUE)
        self.assertEqual(len(g["Orwell"]), 2)

if __name__ == "__main__":
    main()
