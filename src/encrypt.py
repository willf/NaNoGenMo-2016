import random


# Modified from http://stackoverflow.com/a/25238398
# to work with Python 3, and return a list
def random_derangement(n):
    while True:
        v = list(range(n))
        for j in range(n - 1, -1, -1):
            p = random.randint(0, j)
            if v[p] == j:
                break
            else:
                v[j], v[p] = v[p], v[j]
        else:
            if v[0] != 0:
                return v


def random_key(alphabet):
    return "".join([alphabet[i] for i in random_derangement(len(alphabet))])


class SubstitutionCipher(object):
    def __init__(self, alphabet, key):
        assert (len(key) == len(alphabet))
        self.alphabet = alphabet
        self.key = key
        self.e = dict(zip(alphabet, key))
        self.d = dict(zip(key, alphabet))

    # the huge assumptions are are:
    # 1. that latex commands are of the form \xxx{yyy}
    # 2. that none of the parameters are anything but encipherable text
    # 3. That \,{,} are not part of the alphabet
    # This will work for things like \textbf{some text}
    # or \emph{some text} just fine.
    def convert(self, d, text):
        buffer = list(text)
        in_latex_cmd = False
        in_latex_group = False
        for i, ch in enumerate(buffer):
            if in_latex_cmd:
                buffer[i] = ch
                if ch == '{' or ch == '}':
                    in_latex_cmd = False
            else:
                if buffer[i].isupper():
                    buffer[i] = d.get(ch.lower(), ch).upper()
                else:
                    buffer[i] = d.get(ch, ch)
                if ch == '\\':
                    in_latex_cmd = True
        return "".join(buffer)

    def encrypt(self, plaintext):
        return self.convert(self.e, plaintext)

    def decrypt(self, ciphertext):
        return self.convert(self.d, ciphertext)

    def encrypt_file(self, i, o):
        with open(o, "w") as outf:
            for line in open(i):
                outf.write(self.encrypt(line))
                outf.write("\n")
