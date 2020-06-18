# Python-Minesweeper
Detta är ett minesweeper program som du kan välja 3 olika svårighets grader.
Spelet går på tid som stannas om man förlora eller vinner.

Om Du vinner spelet och din tid är mindre än top 3 (Eller om där inte finns top 3) tiden så kommer ett fält där du kan skriva in ditt namn och lägga till det till highscore.
I programmet finns där en higscore lista som visar highscore på alla 3 svårighets nivåer.
Om du slår highscore i en svårighet så korrigerar listan sig själv och puttar ner alla highscore ett steg ner till max rank 3 (Sedan försvinner rank 4).
Highscore sparas i databas vilket gör att det finns kvar när man stänger och öppnar programmet igen.

Programmet använder Tkinter som grafiskt gränssnit och sqlite3 modulen som databas.