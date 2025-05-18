import random

# Alfabet català (sense Ç)
ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALFABET)

def netejar_text(text):
    import unicodedata
    # Elimina accents i converteix a majúscules
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    return text.upper()

def lletra_valida(c):
    return c in ALFABET

def vigenere(text, clau, encripta=True, barreja_majuscules=True):
    text = netejar_text(text)
    clau = netejar_text(clau)
    resultat = []
    idx_clau = 0

    for c in text:
        if lletra_valida(c):
            idx_text = ALFABET.index(c)
            idx_clau_actual = ALFABET.index(clau[idx_clau % len(clau)])
            if encripta:
                nova_idx = (idx_text + idx_clau_actual) % N
            else:
                nova_idx = (idx_text - idx_clau_actual) % N
            lletra = ALFABET[nova_idx]
            # Aleatoriament posa majúscula o minúscula
            if barreja_majuscules and random.choice([True, False]):
                lletra = lletra.lower()
            resultat.append(lletra)
            idx_clau += 1
        else:
            resultat.append(c)  # Manté espais, signes, etc.

    return ''.join(resultat)
