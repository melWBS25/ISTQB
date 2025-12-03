
class TestGrenzwertBMI:
    """Tests für Grenzwerte zwischen Kategorien (TC05 - TC08)"""

    def test_tc05_grenzwert_ug_normal(self):
        """TC05: GW ug/normal - Grenze bei 18.5"""
        kategorie = kategorisiere_bmi(18.5)

    def test_tc06_grenzwert_normal_üg(self):
        """TC06: GW normal/üg - Grenze bei 24.9"""
        kategorie = kategorisiere_bmi(24.8)

    def test_tc07_grenzwert_üg_adipositas(self):
        """TC07: GW üg/adipositas - Grenze bei 29.9"""
        kategorie = kategorisiere_bmi(29.9)

    def test_tc08_grenzwert_adipositas(self):
        """TC08: GW adipositas - Grenze bei 30"""
        kategorie = kategorisiere_bmi(30)
