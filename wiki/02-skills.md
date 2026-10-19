# 2. Skills: deine Abkürzungen

## Das Wichtigste in fünf Sätzen

1. Ein Skill ist ein fertiger Ablauf, den Claude Schritt für Schritt abarbeitet, damit du nicht jedes Mal alles neu erklären musst.
2. Du startest einen Skill, indem du `/` und seinen Namen tippst, z. B. `/post-entwerfen`; danach fragt Claude dich nach allem, was fehlt.
3. Wir haben zwölf Skills, vom Post-Entwurf über das Spieltag-Paket bis zum Wochenrückblick.
4. Claude kann Skills auch von selbst vorschlagen, wenn sie zu deinem Wunsch passen, und du kannst jederzeit neue Skills vorschlagen.
5. Über Verbindungen (Connectors) kann Claude andere Werkzeuge bedienen; für uns ist Canva die wichtigste.

## Was ist ein Skill?

Ein Skill ist eine Anleitung für Claude, die im Repo liegt (`.claude/skills/<name>/SKILL.md`). Sie sagt Claude, welche Fragen er stellen soll, welche Dateien er lesen muss, worauf er achten soll und was am Ende rauskommen soll.

Vorteil: Jeder bekommt dieselbe Qualität, und du musst nicht jedes Mal einen langen Auftrag schreiben.

## So startest du einen Skill

1. Tipp im Chat `/`. Es erscheint eine Liste.
2. Wähl den Skill aus oder tipp den Namen weiter, z. B. `/post-entwerfen`.
3. Du kannst gleich etwas dazuschreiben: `/post-entwerfen TOTW Süper Lig für TikTok`.
4. Claude fragt nach allem, was noch fehlt.

Du musst Skills nicht starten. Wenn du schreibst „Mach mir einen Post für das Bundesliga-Konto“, erkennt Claude oft selbst, dass `/post-entwerfen` passt.

## Unsere Skills

| Skill | Was er tut | Beispiel |
|---|---|---|
| `/post-entwerfen` | Fragt Konto, Plattform, Sprache, Format und Ziel ab. Liefert Hook, Skript oder Bildtext, Caption, Hashtags und Call-to-Action. Weist auf Produktfakten und Bildrechte hin. Legt die Datei in `content/ideen/` oder `content/produktion/` an. | `/post-entwerfen Reel fürs Premier-League-Konto über den größten Absteiger der Woche` |
| `/faktencheck` | Prüft einen Entwurf gegen `produktfakten.md` und das Glossar. Gibt Hinweise, keine Sperre. | `/faktencheck content/produktion/2026-10-24_bundesliga_totw-spieltag8.md` |
| `/spieltag-paket` | Nach einem Spieltag, je Liga: Team der Woche, größte Auf- und Abwertungen mit Begründung (aus Screenshots oder von der öffentlichen Seite), drei Story-Ideen, je ein Hook-Vorschlag. Zahlen immer mit Stand-Datum. | `/spieltag-paket Süper Lig` und dann Screenshots aus der App schicken |
| `/uebersetzen` | Deutsch ↔ Englisch ↔ Türkisch mit Glossar, an den Ton des Kontos angepasst, nicht wörtlich. | `/uebersetzen dieses Skript fürs Süper-Lig-Konto` |
| `/wiederverwerten` | Macht aus einem Video oder Post die Varianten für andere Plattformen und Konten (Format, Länge, Sprache, Caption). | `/wiederverwerten das TikTok von gestern für Instagram und X` |
| `/content-kalender` | Pflegt den Plan: was, wann, wo, Status. Zeigt Lücken je Konto. | `/content-kalender Was fehlt nächste Woche?` |
| `/test-eintragen` | Legt einen Test im Journal an (Hypothese, was variiert wird, Erfolgskriterium) und trägt später das Ergebnis ein. | `/test-eintragen Frage-Hook gegen Aussage-Hook auf TikTok` |
| `/wochenrueckblick` | Der wöchentliche Termin: fragt Kennzahlen, Fan-Feedback, Testergebnisse, Hooks und Inspiration ab, schreibt alles ins Journal und zieht drei Erkenntnisse. | `/wochenrueckblick` und Screenshots der Statistiken schicken |
| `/hook-sammeln` | Nimmt einen Link oder Screenshot und trägt Hook oder Vorbild mit Begründung ein. | `/hook-sammeln` plus Screenshot eines Reels, das dir gefallen hat |
| `/video-planen` | Storyboard, Shotlist, Sprechertext, Untertiteldatei (SRT), freier Musikvorschlag, Schnitt-Anleitung für CapCut. | `/video-planen 25 Sekunden: Warum ist dieser Verteidiger +5?` |
| `/regel-vorschlag` | Der Lernmechanismus: Eine Korrektur persönlich merken oder als Team-Vorschlag in `vorschlaege.md` eintragen. | `/regel-vorschlag Auf TikTok keine Hashtags im Bildtext` |
| `/hilfe` | „Wie mache ich …?“ in einfacher Sprache, mit Verweis ins Wiki. | `/hilfe Wie verbinde ich Canva?` |

## Eigene Skills vorschlagen

Wenn du merkst, dass du Claude immer wieder dasselbe erklärst, ist das ein Kandidat für einen neuen Skill. Beispiele: „Derby-Vorschau“, „Transfer-Check“, „Story-Umfrage“.

So geht es: Sag Claude „Ich möchte einen neuen Skill vorschlagen“ und beschreibe, was er tun soll. Claude schreibt einen Entwurf in `content/vorschlaege.md` oder `marketing/vorschlaege.md`. Ihr besprecht ihn beim Wochentermin. Wenn ihr ihn wollt, legt Claude ihn an.

Bestehende Skills dürft ihr auch verbessern, mit einer kurzen Notiz, was und warum.

## Verbindungen (Connectors)

Ein **Connector** verbindet Claude mit einem anderen Werkzeug. Danach kann Claude dort direkt arbeiten.

| Werkzeug | Connector? | Was Claude damit kann |
|---|---|---|
| **Canva** | Ja, offiziell | Designs suchen, neue erstellen, Vorlagen befüllen, exportieren |
| **CapCut** | Nein (Stand 19.10.2026) | Claude liefert Dateien (z. B. SRT-Untertitel) und Anleitungen, du schneidest |
| **Instagram, TikTok, X** | Wir nutzen bewusst keinen | Claude postet nie selbst (feste Regel). Automatisierung schaltet nur Burhan frei. |

**Canva verbinden:** In der Claude-App die Einstellungen öffnen, zu **Connectors** gehen, Canva suchen, **Verbinden** klicken und dich bei Canva anmelden. Du meldest dich selbst an; Claude bekommt kein Passwort. Genauer erklärt in Dokument 7. Wenn etwas anders aussieht, frag den Wiki-Chat.
