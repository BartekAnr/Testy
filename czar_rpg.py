# obrazenia maja uwzgledniac kazde 10 punktow niewykorzystanej many (Obliczyæ rzeczywiste obra¿enia czaru – dla uproszczenia przyjmijmy, ¿e obra¿enia wzrastaj¹ o 10% za ka¿de 10 punktów many powy¿ej kosztu many.)

def czar_ataku(nazwa_postaci, moc_czaru, mana, koszt_many):
    if koszt_many > mana:
        print(f"Postac {nazwa_postaci} nie ma wystarczajacej many, by rzucic czar!")
    elif koszt_many <= mana:
        mana = mana - koszt_many
        bonus = (mana - koszt_many) / 10
        plus = moc_czaru * 0.1 * bonus
        obrazenia = moc_czaru + plus
        print(f"Postac {nazwa_postaci} rzucila czar zadajac {obrazenia} punktow obrazen. Pozostalo jej {mana} punktow many!")
    
czar_ataku("Mag", 100, 120, 50)     
czar_ataku("Czarodziej", 80, 40, 50)     


"""

LEPIEJ NAPISANE LICZENIE OBRAZEN ZA KAZDE 10 PUNKTOW NADWYZKI ZA KOSZT MANY W STOSUNKU DO CALEJ POSIADANEJ MANY
def czar_ataku(nazwa_postaci, moc_czaru, mana, koszt_many):
    if koszt_many > mana:
        print(f"Postac {nazwa_postaci} nie ma wystarczajacej many, by rzucic czar!")
    else:
        mana -= koszt_many
        nadwyzka = mana - koszt_many
        bonus = (nadwyzka // 10) * 0.1  # Wzrost obrazen o 10% za kazde 10 punktow nadwyzki
        obrazenia = moc_czaru * (1 + bonus)
        
        print(f"Postac {nazwa_postaci} rzucila czar, zadajac {obrazenia:.1f} punktow obrazen. Pozostalo jej {mana} punktow many!")

# Przyklady wywolania
czar_ataku("Mag", 100, 120, 50)  # Powinno zwrocic 170 obrazen
czar_ataku("Czarodziej", 80, 40, 50)  # Powinno zwrocic komunikat o braku many
"""