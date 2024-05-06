## Oppgaver

> Oppgavene skal besvares i en fil med navn `oppgaver-pseudokode.md`

### Oppgave 2.1

> Oppgave 1 fra eksamen H23

Hvilket av følgende er ikke et typisk kjennetegn på pseudokode? Velg riktig alternativ.

- [ ] den har uformell syntaks.
- [ ] den ligner på vanlig menneskespråk.
- [X] den kan kjøres direkte på en datamaskin.
- [ ] den brukes ofte i planleggingsfasen av programmering.

### Oppgave 2.2

> Oppgave 2 fra eksamen V23

Ta utgangspunkt i følgende pseudokode:

```pseudo
SET m TO 3
SET i TO 1
WHILE i GREATER THAN m
  DISPLAY "Lykkelig dag!"
  INCREMENT i
ENDWHILE
```
Hvor mange ganger blir teksten "Lykkelig dag!" skrevet ut?

- [ ] tre ganger
- [ ] to ganger
- [ ] én gang
- [X] ingen ganger

### Oppgave 2.3

> Oppgave 4 fra eksamen H23

Hvilke av de følgende sekvensene med pseudokode skriver ut tallene fra og med 1 til og med 5? Flere alternativer kan være riktige. Velg riktige svar.

```pseudo
1.
SET i TO 1
FOR hver i LESSER OR EQUAL 5
  PRINT i
ENDFOR

2.
SET i TO 1
WHILE i < 5
  PRINT i
  INCREMENT i
ENDWHILE
3.
SET i TO 0
FOR hver i LESSER OR EQUAL 4
  PRINT i+1
ENDFOR

4.
SET i TO 1
WHILE i <= 5
  PRINT i
  INCREMENT i BY 2
ENDWHILE
```

- [X] 1
- [ ] 2
- [X] 3
- [ ] 4

### Oppgave 2.4

> Oppgave 3 fra eksamen V23

Tallene 1, 3, 6, 10, 15, 21 og så videre kalles for trekanttall. De tilsvarer antallet prikker som vil vises i en likesidet trekant når man bruker et grunnleggende trekantmønster for å bygge trekanten. Se illustrasjonen nedenfor:

![v23-3](./bilder/v23-3.png)

Den følgende pseudokoden beskriver en funksjon som regner ut og returner trekanttallet nummer n:

```pseudo
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION
```

Bruk funksjonen som er beskrevet ovenfor, og skriv pseudokoden til et program som regner sammen og skriver ut totalsummen av de ti første trekanttallene. Bruk dobbelt mellomrom for innrykk i koden der det er aktuelt. Skriv svaret ditt nedenfor.

> Du kan bruke din egen standard for pseudokode, bare den er hensiktsmessig.

```pseudo
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION


SET n TO 1
SET sum TO 0
FOR hver n LESSER OR EQUAL TO 10
    sum += trekantall(n)
        RETURN sum
ENDFOR


```