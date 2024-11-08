"""Varaston testipääohjelman moduuli"""

from varasto import Varasto


def tulosta_varastot_alkutila(mehua, olutta):
    """Tulostaa varastojen alkutilan"""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_olutvaraston_getterit(olutta):
    """Tulostaa olutvaraston getter-arvot"""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_mehu_setterit(mehua):
    """Testaa mehuvaraston setterit"""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def testaa_huono_varasto():
    """Testaa virheelliset varastot ja tulostaa ne"""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def testaa_virhetilanteet_lisays(mehua, olutta):
    """Testaa virheelliset lisäykset varastoihin"""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def testaa_virhetilanteet_otto(mehua, olutta):
    """Testaa virheelliset otot varastoista"""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    """Pääohjelma"""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_varastot_alkutila(mehua, olutta)
    tulosta_olutvaraston_getterit(olutta)
    testaa_mehu_setterit(mehua)
    testaa_huono_varasto()
    testaa_virhetilanteet_lisays(mehua, olutta)
    testaa_virhetilanteet_otto(mehua, olutta)


if __name__ == "__main__":
    main()
