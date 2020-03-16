# 3. Deskriptori

# 3.1 problem sa properties

from weakref import WeakKeyDictionary


class PrirodanBrojProperties:
    def __init__(self, broj):
        self._prirodan_broj = 1

    @property
    def prirodan_broj(self):
        return self._prirodan_broj

    @prirodan_broj.setter
    def prirodan_broj(self, broj):
        if not isinstance(broj, int):
            raise ValueError("Broj mora biti ceo")
        if broj <= 0:
            raise ValueError("Broj nije prirodan")
        self._prirodan_broj = broj


class PrirodanBroj():
    def __init__(self):
        self.podrazumevana_vrednost = 1
        self.podaci = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.podaci.get(instance, self.podrazumevana_vrednost)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Broj mora biti ceo")
        if value <= 0:
            raise ValueError("Broj nije prirodan")
        self.podaci[instance] = value


class PrirodanBrojDescriptor:
    # manipulacija objektom (u ovom slucaju dobijanje vrednosit i postavljanje vrednosti atributa)
    # se prosledjuje klasi PrirodanBroj
    prirodan_broj = PrirodanBroj()

    def __init__(self, broj):
        self.prirodan_broj = broj

    # nema boiler plate koda u nasoj klasi
    # mozemo na vise mesta da odradimo ustu proveru


if __name__ == '__main__':
    # Test PrirodanBrojProperties
    pbp = PrirodanBrojProperties(100)
    pbp.prirodan_broj = 1
    pbp.prirodan_broj = 3
    print(pbp.prirodan_broj)
    try:
        pbp.prirodan_broj = -1
    except ValueError:
        print("Broj nije prirodan")

    # Test PrirodanBrojDescriptor
    pbd = PrirodanBrojDescriptor(100)
    pbd.prirodan_broj = 1
    pbd.prirodan_broj = 3
    print(pbd.prirodan_broj)
    try:
        pbd.prirodan_broj = -1
    except ValueError:
        print("Broj nije prirodan")
