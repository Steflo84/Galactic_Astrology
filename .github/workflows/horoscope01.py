#programmer: Stephanie Byrne
#Date: 21/05/2020
#File: starsign03.py - STATUS: TRUE

#NEXT? Start a file called horoscope02.py - copy and past code and date it before adjustments
#QUESTION - can you erase input after writing in terminal? and the astro_sign discrepancy??
# days until there birthday this year (date01.py example of code, transfer into 'input'), add print at end
#format the date entered to be tolerant, for example, dec Dec December 12 (or just make int(12)?)
#format days of month to add '2nd' not '2' for print (research code)
#format the days of the month errors in else statements (Worth It?) Like, Max #31, feb #28#29...

print()
print("ASTROLOGY is traditionally based on 12 signs evenly spread over the year.\nBut in reality star signs are different sizes and also present at different times.\nMaking way for Galactic or Sidereal Astrology.\nLet's find out what sign you are according to these current methods,\nas well as your Chinese Zodiac animal and pull a Tarot card for Participating.\nLet's get started...")
print()
year = int(input("Enter your birth year (eg. 1984): "))
month = input("Enter month of birth (eg. august, november, july etc): ")
day = int(input("Enter Day of your birth (eg. 14, 26, 2): "))

if month == "december":
    if day < 17:
        astro_sign = "WoW! You are the new sign, Ophiuchus!"
    else:
        astro_sign = "Seductive Sagittarius"
elif month == "january":
    if day < 18:
        astro_sign = "Sassy Sagittarius"
    else:
        astro_sign = "Controlling Capricorn"
elif month == "february":
    if day < 15:
        astro_sign = "Care Giver Capricorn"
    else:
        astro_sign = "Alien Aquarius"
elif month == "march":
    if day < 11:
        astro_sign = "Airy Aquarius"
    else:
        astro_sign = "Peaceful Pisces"
elif month == "april":
    if day < 18:
        astro_sign = "Practical Pisces"
    else:
        astro_sign = "All Hail Aries"
elif month == "may":
    if day < 13:
        astro_sign = "At home Aries"
    else:
        astro_sign = "Take home Taurus"
elif month == "june":
    if day < 19:
        astro_sign = "Talented Taurus"
    else:
        astro_sign = "Games of Gemini"
elif month == "july":
    if day < 21:
        astro_sign = "Great mate Gemini"
    else:
        astro_sign = "Compassionate Cancer"
elif month == "august":
    if day < 9:
        astro_sign = "Caretaker Cancer"
    else:
        astro_sign = "Loving Leo"
elif month == "september":
    if day < 15:
        astro_sign = "Leader Leo"
    else:
        astro_sign = "Volatile Virgo"
elif month == "october":
    if day < 30:
        astro_sign = "Virgin Virgo"
    else:
        astro_sign = "Love-able Libra"
elif month == "november":
    if day < 22:
        astro_sign = "Lend a hand Libra"
    else:
        astro_sign = "Seductive Scorpio"
#Followinmg code = Published on w3resources.com - Python Exercises: Display sign of the Chinese Zodiac from the year
#Link: https://www.w3resource.com/python-exercises/python-conditional-exercise-39.php
if 0 == (year - 2000) % 12:
    sign = "Dragon"
elif 1 == (year - 2000) % 12:
    sign = "Snake"
elif 2 == (year - 2000) % 12:
    sign = "Horse"
elif 3 == (year - 2000) % 12:
    sign = "sheep"
elif 4 == (year - 2000) % 12:
    sign = "Monkey"
elif 5 == (year - 2000) % 12:
    sign = "Rooster"
elif 6 == (year - 2000) % 12:
    sign = "Dog"
elif 7 == (year - 2000) % 12:
    sign = "Pig"
elif 8 == (year - 2000) % 12:
    sign = "Rat"
elif 9 == (year - 2000) % 12:
    sign = "Ox"
elif 10 == (year - 2000) % 12:
    sign = "Tiger"
else:
    sign = "Hare"

print()
print("You entered: {0} {1} {2}".format(day, month, year))
print("Your Galactic/Sidereal Astrological sign: ",astro_sign)
print("Your Chinese Zodiac sign: ",sign)
print()
print("A card and Lucky number has been carefully selected for you.\nEnjoy your day!")
import random
tarot_list = ["The Fool(0) - Fresh Start, watch your step!",
              "The Magician(1) - Big Change, careful of those around you",
              "The High Priestess(2) - You are wise, teach others",
              "The Empress(3) - Vitality, you are one with mother nature",
              "The Emperor(4) - You are coming into your power", "The Hierophant(5) - Tradition, routine, old habits - shake it up!",
              "The Lovers(6) - Partnering up", "The Chariot(7) - Charging forward, narrow focus",
              "Strength(8) - Rising above, control", "The Hermit(9) - Secrets are being revealed",
              "Wheel of Fortune(10) - Round and Round, when will this cycle end?!?",
              "Justice(11) - Balance and provide harmony",
              "The Hanged Man(12) - Your stuck in your head, gain a new perspective",
              "Death(13) - Transition and rebirth. It ends so something begins", "Temperance(14) - Purification, past is past",
              "The Devil(15) - Temptations are tempting!", "The Tower(16) - Sudden change, unexpected",
              "The Star(17) - Hope and dreams are your light", "The Moon(18) - Be Cautious, heightened emotions",
              "The Sun(19) - revelation and happiness", "Judgment(20) - Favorable ruling YaY!",
              "The World(21) - Completion, so enjoy your rest"]
print()
print(random.choice(tarot_list))

#SAMPLE RESULT: (excluding intro)
#Enter your birth year (eg. 1984): 1984
#Enter month of birth (eg. august, november, july etc): november
#Enter Day of your birth (eg. 14, 26, 2): 14

#You entered: 14 november 1984
#Your Galactic/Sidereal Astrological sign:  Lend a hand Libra
#Your Chinese Zodiac sign:  Rat

#A card and Lucky number has been carefully selected for you.
#Enjoy your day!

#The Hierophant(5) - Tradition, old habits

#Process finished with exit code 0