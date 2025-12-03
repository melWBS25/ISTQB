import pytest
from bmi_rechner import berechne_bmi, kategorisiere_bmi
class TestKlasse1:
def test_tc01_untergeweicht(self):
    bmi = berechne_bmi(45.00,1.75)
    assert bmi == 14.7
    kategorie = kategorisiere_bmi(bmi)
    assert kategorie == "Untergewicht"

def test_tc02_Normalgewicht(self):
    bmi = berechne_bmi(70.00,1,75)
    assert bmi == 22.9
    kategorie = kategorisiere_bmi(bmi)
    assert kategorie == "Normalgewicht(Mitte)"    

def test_tc01_untergeweicht(self):
    bmi = berechne_bmi(70.00,1,75)
    assert bmi == 22.9
    kategorie = kategorisiere_bmi(bmi)
    assert kategorie == )"

def test_tc01_untergeweicht(self):
    bmi = berechne_bmi(70.00,1,75)
    assert bmi == 22.9
    kategorie = kategorisiere_bmi(bmi)
    assert kategorie == 