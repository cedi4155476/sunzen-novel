# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image renpy = "Ren'Py.png"
image gnm = "Gaanmalogo.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define M = Character('Max Lenster', color="#c8ffc8")
define n = Character('Notiz', color="#FF0000")

# Hier beginnt das Spiel.

label splashscreen:
    
    scene black
    with Pause(1)

    show text "Made with"
    with dissolve
    with Pause(1)
    hide text
    with dissolve
    with Pause(1)
    
    show renpy at truecenter
    with dissolve
    with Pause(2)
    hide renpy
    with dissolve
    with Pause(1)
    
    show text "presentet by"
    with dissolve
    with Pause(1)
    hide text
    with dissolve
    with Pause(1)
    
    show gnm
    with dissolve
    with Pause(2)
    hide gnm
    with dissolve
    with Pause(1)

    return
    
# Kapitel 1

label start:
    
    "Ich ging mit Max wieder einmal nach Flencia um Kleider zu kaufen."
    "Es war die Hauptstadt von Loeda und konnte so ziemlich alles bieten, was man braucht."
    "Es war wie jedes andere Mal. "
    n"Hier bitte Dialogue denken!"
    "Danach gingen wir in das Café „Fliegender Drache“ und gönnten uns ein erfrischendes Eis."
    "Ich nahm wie immer mein Lieblingseis. Das Kleins-di-Vanilla."
    "Es war ein Vanille-Eis mit Schoko Splitter und einer speziellen Glasur oben drauf. Die meisten, die ich kannte, mochten diese Glasur überhaupt nicht. Ich jedoch war beinahe ein exzentrischer Fan davon."
    n"Hier bitte wieder Dialogue denken!"
    "Ich persönlich fand es immer höchst amüsant, wenn er über seine Eltern sprach. Man konnte ihm richtig ansehen, dass sie ihm peinlich waren. Ich hab ihn auch damit immer wieder aufgezogen."
    "Im Gegenzug nervte er mich immer wieder mit meinem Essgeschmack und auch Kleidungstil. Obwohl er beim zweiten schon vergeblich versuchte, etwas daran zu ändern."
    "Wir gingen nach dem verspeisen der  Eisbecher zur Spielautomaten-Abteilung."
    n"Also, die Paar Zeilen hier sind nur zum füllen gedacht. Wir müssen hier eindeutig ein script verfassen an dem wir uns entlang hangeln können. Direkt aus dem Text heraus ginge auch, ist nur recht unausgereift ^^"
    return
