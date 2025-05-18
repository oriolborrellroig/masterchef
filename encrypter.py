import random
import unicodedata

class VigenereCatala:
    def __init__(self, clau):
        self.ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.N = len(self.ALFABET)

    def _netejar_text(self, text):
        # Elimina accents i converteix a majúscules
        text = ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
        return text.upper()

    def _lletra_valida(self, c):
        return c in self.ALFABET

    def vigenere(self, text, clau, encripta=True, barreja_majuscules=True):
        text = self._netejar_text(text)
        resultat = []
        idx_clau = 0

        for c in text:
            if self._lletra_valida(c):
                idx_text = self.ALFABET.index(c)
                idx_clau_actual = self.ALFABET.index(clau[idx_clau % len(clau)])
                if encripta:
                    nova_idx = (idx_text + idx_clau_actual) % self.N
                else:
                    nova_idx = (idx_text - idx_clau_actual) % self.N
                lletra = self.ALFABET[nova_idx]
                if barreja_majuscules and random.choice([True, False]):
                    lletra = lletra.lower()
                resultat.append(lletra)
                idx_clau += 1
            else:
                resultat.append(c)  # Manté espais, signes, etc.

        return ''.join(resultat)
