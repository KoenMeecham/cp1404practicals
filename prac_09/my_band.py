"""Band example with list of musicians."""
from band import Band
from musician import Musician
from guitar import Guitar


def main():
    """Make a band and hav ethem play"""
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add_musician(nuno)
    band.add_musician(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add_musician(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add_musician(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    print(band.play())


main()
