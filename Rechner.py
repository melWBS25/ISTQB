
from Calculator import Calculator

def test_addiere_zwei_zahlen():
    # Arrange
    rechner = Calculator()

    # Act
    ergebnis = rechner.addiere(5, 3)
    # Assert
    assert ergebnis == 8, f"Erwartet: 8, Erhalten: {ergebnis}"

def test_subtrahiere_zwei_zahlen():
    # Arrange
    rechner = Calculator()

    # Act
    ergebnis = rechner.subtrahiere(10, 4)

    # Assert
    assert ergebnis == 6, f"Erwartet: 6, Erhalten: {ergebnis}"

def test_dividiere_zwei_zahlen():
    # Arrange
    rechner = Calculator()
    # Act
    ergebnis = rechner.dividiere(100, 4)
    # Assert
    assert ergebnis == 25, f"Erwartet: 25, Erhalten: {ergebnis}"

def test_dividiere_zwei_zahlen_durch_0():
    rechner = Calculator()
    try:
        rechner.dividiere(10,0)
        assert False, "Es wurde kein Fehler geworfen"
    except ValueError:
        pass





# Alle Tests durchführen
try:
    test_addiere_zwei_zahlen()
    test_subtrahiere_zwei_zahlen()
    test_dividiere_zwei_zahlen()
    test_dividiere_zwei_zahlen_durch_0()
    print("Tests bestanden Rechner")


except NameError as e:
    print(f"Test fehlgeschlagen: {e}")
except AttributeError as t:
    print(f"Test fehlgeschlagen: {t}")
except AssertionError as a:
    print(f"Test fehlgeschlagen: {a}")
    print("Assertion Error: Bedingung nicht erfüllt")
