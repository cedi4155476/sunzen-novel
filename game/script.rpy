# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image renpy = "Ren'Py.png"
image gnm = "Gaanmalogo.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.

##Haupt-Charaktere
define M = Character('Max Lenster', color="#c8ffc8")
define Haupt = Character(' ', color="#cccccc")
define R = Character('Riolf Nartrod', color="#cccccc")

##Andere
define U = Character('???', color="cccccc")


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
    
    ##Einkaufszentrum Flencia
    M"Sieht doch schon besser aus!"
    Haupt"Aber meine alten Sachen reichen doch aus."
    M"Nein tun sie nicht. Du schaffst es nur knapp durch die Woche mit deiner Kleidung. Schonmal was von Ersatzwäsche gehört?"
    Haupt"Wie oft wollen wir dieses Thema eigentlich noch ansprechen?"
    M"Du hast doch damit angefangen!"
    Haupt"Aber du hast weitergemacht!"
    M"Denkst du ans gleiche wie ich?"
    Haupt"Natürlich"
    "Ohne noch genaueres zu bereden gingen wir zum Cafe 'Fliegender Drache'."
    ##Szenenwechsel Cafe Fliegender Drache
    Haupt"Ein Kleins-di-Vanilla gerne."
    M"Ugh... Für mich gerne ein normales Vanille Eis."
    "Der Kellner nahm die Bestellung entgegen und verliess uns wieder."
    M"Wie kannst du das nur essen. Da kannst du gleich ne Eisenstange essen."
    Haupt"Ach was, das sind doch bestimmt viele verschiedene Früchte drinnen, aber sicher kein Eisen."
    "Es gab ein grosses Rätsel in diesem Cafe. Nämlich was für Zutaten sich im Kleins-di-Vanilla befinden. Nur der Koch selber weiss darüber bescheid."
    "90 der Leute behaupten, es schmecke so, als würde man eine Eisenstange essen. Die anderen 10 finden es fruchtig und erfrischend."
    M"Meine Eltern haben es mal wieder geschafft."
    Haupt"Haben sie schon wieder die Einrichtung geändert?"
    M"JA! Diesmal ist sogar aus dem oberen Stockwerk ein Garten entstanden, dafür ist nun im ehemaligen Garten die Küche. Wie schaffen die das immer?"
    Haupt"Na dann wünsch ich viel spass, wenn es regnet."
    M"Na danke Mister 'ich werde von den Leuten ausgelacht, weil ich keine Ahnung hab, was man sich anziehen soll'"
    Haupt"Das nimmst du zurück!"
    M"Als ob!"
    "Wir blickten uns gegenseitig an, als würden Blitze zwischen uns existieren und gingen dann Richtung Spielhalle."
    ##Szenenwechsel Spielhalle Flencia
    M"Diesesmal gewinne ich!"
    Haupt"Als ob!"
    "Leider verlor ich trotz des Angebens..."
    "Es wurde langsam spät."
    Haupt"Ich brauch noch Geld fürs Abendessen."
    M"Na dann ab zur Kito Bank."
    ##Szenenwechsel Grosstadt
    "Wie jedesmal, wenn wir zur Kito Bank gingen, machten wir ein Wettrennen."
    "Es war Hochsommer, weswegen uns nach einer kurzen Zeit bereits beiden die Puste ausging."
    "Wir entschieden uns für ein Unentschieden und gingen gemütlich weiter."
    M"Hey dort vorne ist ein Eiswagen!"
    Haupt"Ich habe aber kein Geld mehr."
    M"Schon gut ich lade dich ein."
    "Wir holten uns beide ein Vanille Eis und gingen dann weiter zur Bank."
    M"Da scheint es ein Unfall gegeben zu haben."
    "Ich blickte von meinem Eis weg auf die Strasse und sah zur Unfallstelle."
    "Ein Lastwagen schien von der Seite in ein Polizeiauto gefahren zu sein."
    "Die Polizisten wurden gerade von der Ambulanz weggefahren."
    "Da jedoch das Polizeiauto nicht sehr stark beschädigt war, konnte man ein Todesfall ausschliessen."
    M"Oh müssen jetzt die armen Polizisten ins Krankenhaus um ihr boböchen zu heilen."
    "Ich erinnerte mich wieder an früher."
    "Sehr oft wurde bei Max eine 'Untersuchung' durchgeführt von der Polizei."
    "Jedesmal stellen diese dann das ganze Haus auf den Kopf und nehmen 'schädliche Ware' in gewahrsam."
    "Mit 'schädlicher Ware' waren bisher immer Schmucksachen gemeint."
    "Es schmerzte mich, dass mein Heimatsland so grausam sein kann."
    ##Szenenwechsel Kito Bank
    "Bei der Bank gab es eine überaus lange Schlange. Ich stellte mich hinten an und Max wartete bei den Bänken."
    "Auf einmal kamen einige merkwürdig gekleidete Männer in das Gebäude und teilten sich auf."
    return
