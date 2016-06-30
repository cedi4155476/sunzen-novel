# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image renpy = "Ren'Py.png"
image gnm = "Gaanmalogo.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define M = Character('Max Lenster', color="#c8ffc8")

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

    M "Du hast ein neues Ren'Py Spiel erstellt."

    M "Sobald du eine Geschichte, Bilder und Musik hinzufügst, kannst du es für alle veröffentlichen!"

    return
