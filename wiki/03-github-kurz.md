# 3. GitHub in fünf Minuten

## Das Wichtigste in fünf Sätzen

1. Ein Repo ist ein gemeinsamer Ordner, der sich jede Änderung merkt, sodass man immer sieht, wer wann was geändert hat, und alles zurückholen kann.
2. Ein Branch ist eine eigene Spur in diesem Ordner; wir arbeiten alle auf der Spur `arbeit`, die Spur `main` pflegt nur Burhan.
3. Ein Commit ist ein gespeicherter Zwischenstand mit kurzer Beschreibung, ein Push schickt diese Zwischenstände zu GitHub, damit alle sie bekommen.
4. Claude übernimmt die ganze Technik für dich; du musst keine Befehle lernen, nur verstehen, was passiert.
5. Wenn Claude sagt „du bist nicht auf `arbeit`“, sag einfach „wechsle auf arbeit“.

## Was ist ein Repo?

Ein **Repo** (kurz für Repository, auf Deutsch etwa „Ablage“) ist ein Ordner mit Gedächtnis. Unser Repo heißt `FootPulse-Marketing`. Darin liegen alle Texte, Pläne, Ideen und Tabellen. Es liegt auf deinem Rechner und zusätzlich auf **GitHub**, einer Website, über die wir alle denselben Stand bekommen.

Der Unterschied zu einem normalen Ordner: Jede Änderung wird gespeichert, mit Datum, Name und Beschreibung. Wenn etwas kaputtgeht, kann man den alten Stand zurückholen.

Videos, Bilder und Musik liegen nicht im Repo, sondern in OneDrive. Das Repo ist für Text.

## Was ist ein Branch?

Ein **Branch** (auf Deutsch „Zweig“) ist eine eigene Spur im Repo. Stell dir zwei Fassungen desselben Ordners vor:

- **`main`**: die geprüfte Grundfassung. Nur Burhan ändert sie, z. B. wenn er Regeln anpasst.
- **`arbeit`**: unser gemeinsamer Arbeitsstand. Hier entsteht alles Inhaltliche: Ideen, Skripte, Journal, Kennzahlen.

**Warum arbeiten wir auf `arbeit`?** Damit die Grundfassung sauber bleibt und Burhan in Ruhe entscheiden kann, was davon in `main` übernommen wird. So kann nichts Wichtiges aus Versehen kaputtgehen.

Claude prüft bei jedem Chat-Start, auf welchem Branch du bist. Wenn du nicht auf `arbeit` bist, sagt er es dir und bietet an zu wechseln. Sag dann einfach „ja“.

## Was sind Commit, Push und Pull?

| Begriff | Was passiert | Vergleich |
|---|---|---|
| **Commit** | Claude speichert einen Zwischenstand mit einer kurzen Beschreibung, z. B. „Skript für TOTW Spieltag 8 angelegt“. | Ein Speicherpunkt in einem Spiel |
| **Push** | Claude schickt deine Commits zu GitHub. Erst dann sieht das Team deine Änderungen. | Hochladen |
| **Pull** | Claude holt die Änderungen der anderen von GitHub auf deinen Rechner. | Herunterladen |

Der normale Ablauf in einer Sitzung:
1. Chat starten. Claude prüft den Branch und holt den neuesten Stand (Pull).
2. Ihr arbeitet zusammen.
3. Am Ende aktualisiert Claude die `LAGE.md`, macht einen Commit und fragt dich, ob er pushen soll.

## Was du tun musst

Fast nichts. Diese Sätze reichen:
- „Wechsle auf arbeit.“
- „Hol den neuesten Stand.“
- „Speicher und schick es hoch.“ (Commit und Push)
- „Was hat sich seit gestern geändert?“

## Was, wenn etwas schiefgeht?

- **Claude meldet einen Konflikt.** Das heißt, zwei Leute haben dieselbe Stelle geändert. Lass Claude das erklären und lösen. Im Zweifel frag Burhan.
- **Claude will auf `main` pushen.** Das ist gesperrt und passiert nicht. Sag „wechsle auf arbeit“.
- **Du hast etwas gelöscht, was du brauchst.** Kein Problem, alles ist im Verlauf. Sag Claude: „Hol die alte Fassung von Datei X zurück.“
- **Dateien löschen:** Claude löscht Dateien im Repo über Git (`git rm`), nicht mit normalen Löschbefehlen. Das ist Absicht: So bleibt alles im Verlauf und nichts außerhalb des Repos kann gelöscht werden.
