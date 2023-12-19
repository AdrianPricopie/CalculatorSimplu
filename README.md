# Calculator Simplu

## Descriere
Acest proiect reprezintă o simplă aplicație de calculator implementată în limbajul de programare Python. Calculatorul permite efectuarea operațiilor de adunare, scădere, înmulțire, împărțire și setare a valorii curente.

## Utilizare
1. Rulează scriptul `calculator_simplu.py` într-un mediu Python.
2. Introdu valoarea inițială când este solicitat (apasă Enter pentru a utiliza valoarea implicită 0).
3. Introdu comenzi pentru a efectua operații pe valoarea curentă a calculatorului.
4. Pentru a ieși din program, introdu comanda "x".

## Comenzi acceptate
- **Adunare (+):** `+ valoare`
- **Scădere (-):** `- valoare`
- **Înmulțire (*):** `* valoare`
- **Împărțire (/):** `/ valoare` (afisează o eroare dacă se încearcă împărțirea la 0)
- **Setare valoare (=):** `= valoare`
- **Ieșire (x):** `x`

## Exemplu de utilizare
``plaintext

    Introdu valoarea initiala (initial este 0): 10
    > + 5
    15.0
    > * 2
    30.0
    > / 3
    10.0
    > = 50
    50.0
    > x
    Program terminated.


## Structura proiect => principii OOP (clase și obiecte).
Am creat un Python Package, calculators care contine 3 fisiere python:

- _ init _.py
- calculator_simplu.py => in acest fisier am creat clasa CalculatorSimplu() și metodele necesare pentru operațiile aritmetice (+, -, *, /) precum si metoda de afișare a rezultatului
- main.py(fisierul unde se ruleaza aplicatia) => aici am importat clasa CalculatorSimplu() prin comanda: from calculators.calculator_simplu import CalculatorSimplu, precum si functia afisare_rezultat() prin -=-- -- comanda: from calculators.calculator_simplu import afisare_rezultat si am creat obiectul calculator

