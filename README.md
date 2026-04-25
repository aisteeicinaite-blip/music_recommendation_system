Muzikos rekomendavimo sistema
1. Įvadas

Šio kursinio darbo tikslas buvo sukurti muzikos rekomendavimo sistemą naudojant Python ir objektinį programavimą (OOP). Programa leidžia vartotojui gauti dainų rekomendacijas pagal pasirinktą žanrą arba nuotaiką.

Sistema nuskaito dainų duomenis iš CSV failo ir pateikia rekomendacijas per konsolę. Vartotojas gali pasirinkti rekomendavimo būdą, įvesti kriterijų, gauti kelias dainas, generuoti daugiau rekomendacijų bei išsaugoti jas į tekstinį failą.

Kaip paleisti programą

python -m src.main

Kaip paleisti testus

python -m unittest discover -s tests

Kaip naudotis programa
Paleisti programą.
Pasirinkti rekomendavimą pagal žanrą arba nuotaiką.
Įvesti vieną iš galimų reikšmių.
Sistema pateiks rekomenduojamas dainas.
Galima generuoti daugiau rekomendacijų.
Galima išsaugoti rekomendacijas į failą.

2. Analizė
Programos struktūra

Projektas suskirstytas į kelias dalis:

models – klasės, aprašančios duomenis (pvz., Song)
services – logika, susijusi su failais ir rekomendacijomis
patterns – rekomendavimo strategijos
data – CSV failas su dainomis
tests – testai


Funkcionalumas

Programa turi šias funkcijas:

nuskaito dainas iš CSV failo
rekomenduoja dainas pagal žanrą
rekomenduoja dainas pagal nuotaiką
leidžia generuoti daugiau rekomendacijų
leidžia išsaugoti rekomendacijas į TXT failą
turi testus pagrindinei logikai patikrinti


OOP principai
Paveldėjimas (Inheritance)
Klasė Song paveldi iš MusicItem. Tai leidžia pakartotinai naudoti bendrą informaciją, pavyzdžiui dainos pavadinimą.

Inkapsuliacija (Encapsulation)
Duomenys saugomi klasėse, o prie jų prieinama per metodus, tokius kaip get_genre ar get_mood.

Polimorfizmas (Polymorphism)
Skirtingos klasės (GenreRecommendation ir MoodRecommendation) turi tą patį metodą recommend(), tačiau veikia skirtingai.

Abstrakcija (Abstraction)
Programa suskirstyta į logines dalis:
FileManager atsakingas už failus
RecommendationEngine už rekomendacijas
Song už duomenų saugojimą
Dizaino šablonas

Projekte naudojamas Strategy pattern.
Skirtingos rekomendavimo strategijos (pagal žanrą arba nuotaiką) įgyvendinamos atskirose klasėse. RecommendationEngine naudoja pasirinktą strategiją priklausomai nuo vartotojo pasirinkimo.

Kompozicija (Composition)
RecommendationEngine klasė savo viduje turi strategijos objektą, todėl gali keisti rekomendavimo logiką nekeisdama pačios klasės struktūros.

Darbas su failais (File I/O)

Programa:
nuskaito duomenis iš songs.csv failo
išsaugo rekomendacijas į recommendations.txt failą


Testavimas

Naudotas unittest framework.

Testai tikrina:
ar rekomendacijos pagal žanrą veikia
ar rekomendacijos pagal nuotaiką veikia
ar grąžinamas teisingas rezultatų kiekis
ar sistema veikia su skirtingais įvedimais


3. Rezultatai

Sukurta veikianti muzikos rekomendavimo sistema. Programa leidžia vartotojui gauti rekomendacijas pagal pasirinktus kriterijus. Taip pat realizuotas failų nuskaitymas ir išsaugojimas bei sukurti testai pagrindinei logikai patikrinti.

4. Išvados

Šio darbo metu buvo pritaikyti objektinio programavimo principai, realizuotas dizaino šablonas ir sukurta veikianti sistema. Ateityje programą būtų galima išplėsti pridedant daugiau dainų, sudėtingesnes rekomendacijas arba grafinę vartotojo sąsają.