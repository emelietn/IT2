### Oppgave 2.12

> Oppgave 5 fra eksamen V23

Nedenfor finner du flere linjer med pseudokode. Sorter linjene i riktig rekkefølge, slik at det blir pseudokoden til et program som skal finne det største tallet av tre tall. Tips: Linjene med pseudokode har ikke innrykk/indentering.

![v23-5](./bilder/v23-5.png)

svar:

```pseudo
1- F
2- H
3- A
4- B
5- C
6- G
7- E
8 - D
...
```
### Oppgave 2.13

> Oppgave 6 fra eksamen H23

Du får i oppgave å finne det nest største tallet i en liste (array) med tall. Dersom det finnes flere like tall som er størst, skal ingen av disse regnes som nest størst. Under finner du fire alternative løsninger for denne oppgaven skrevet i pseudokode. Hvilke to løsninger er riktige?

```pseudo
1
SET størst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN størst
    SET størst TO tall
  ENDIF
ENDFOR
Fjern størst fra listen
SET nestStørst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN nestStørst 
    SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

2
SET størst TO første tall i listen
SET nestStørst TO andre tall i listen
IF nestStørst GREATER THAN størst
  Bytt størst og nestStørst
ENDIF
FOR hvert tall i listen med start fra tredje tall
  IF tall GREATER THAN størst
    SET nestStørst TO størst
    SET størst TO tall
  ELSEIF tall GREATER THAN nestStørst AND tall NOT EQUAL TO størst
  SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

3
SET størst TO negativt uendelig tall
SET nestStørst TO negativt uendelig tall
FOR hvert tall i listen
  IF tall GREATER THAN størst
    SET nestStørst TO størst
    SET størst TO tall
  ELSEIF tall GREATER THAN nestStørst
    SET nestStørst TO tall
  ENDIF
ENDFOR
DISPLAY nestStørst

4
Sorter listen i synkende rekkefølge
FOR hvert tall i listen
    IF tall NOT EQUAL TO neste tall i listen
        DISPLAY neste tall i listen
        avbryt for-løkken
    ENDIF
ENDFOR
```

Velg de to riktige løsningene.

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

### Oppgave 2.14

> Oppgave 7 fra eksamen H23

Elementene i en indeksert variabel (liste/array) skal sorteres i stigende rekkefølge etter følgende algoritme: Man sammenligner hvert element fra venstre til høyre i listen med neste element, og hvis elementet er større enn neste element, bytter de plass. Deretter går man videre til neste element og sammenligner på nytt frem til hele listen er gjennomgått. Dette gjentas til hele listen gjennomgås uten at det forekommer noen ombyttinger.

Under finner du deler av pseudokoden for denne algoritmen. Her er a en liste med n elementer, og a[ i ] er elementet på plass i i listen.

```pseudo
SET i TO 0
FOR hver i LESSER THAN n - 1
  IF a[i] GREATER THAN a[i+1]    
    CALL byttPlass()
  ENDIF
ENDFOR
```

> Presisering: byttPlass() er en funksjon som bytter plass på to naboelementer i listen.

1. Hva blir innholdet i listen etter at vi har kjørt programmet representert ved pseudokoden over for listen a = [8, 5, 2, 6, 12], som har n = 5 elementer?
Velg riktig svar.

- [ ] `[ 5, 8, 2, 6, 12 ]`
- [ ] `[ 5, 2, 8, 6, 12 ]`
- [ ] `[ 5, 2, 6, 8, 12 ]`
- [ ] `[ 2, 5, 6, 8, 12 ]`

2. Utvid pseudokoden slik at programmet den representerer, sorterer ferdig listen a i stigende rekkefølge etter altgoritmen som er vist øverst. Forklar endringene du gjør. Obs! Du må også lage pseudokode for funksjonen byttPlass().

3. Implementer pseudokoden fra punkt b i ditt programmeringsspråk. Listen skal leses inn automatisk, og den ferdig sorterte listen skal skrives til konsollet eller vises i programmet.