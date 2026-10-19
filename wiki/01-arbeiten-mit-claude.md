# 1. Arbeiten mit Claude

## Das Wichtigste in fünf Sätzen

1. Claude ist ein sehr fähiger Mitarbeiter, der schreibt, plant, übersetzt, Bilder ansieht und Dateien pflegt, aber er kennt nur, was du ihm sagst und was im Repo steht.
2. Gute Ergebnisse kommen von guten Aufträgen: Sag immer Ziel, Kontext, ein Beispiel und das gewünschte Format.
3. Das erste Ergebnis ist ein Entwurf; korrigiere ruhig direkt und konkret („kürzer“, „frecher“, „ohne Emojis“), das ist normal und gewollt.
4. Claude kann sich irren, besonders bei Zahlen, Namen und aktuellen Ereignissen, deshalb prüfst du Fakten, bevor etwas veröffentlicht wird.
5. Regeln in `CLAUDE.md` gelten für alle, deine persönlichen Vorlieben stehen in `CLAUDE.local.md`, und für ein neues Thema startest du am besten einen neuen Chat.

## Was Claude ist und was nicht

Claude ist ein KI-Assistent. Im Code-Tab der Claude-Desktop-App arbeitet er direkt in unserem Repo: Er liest Dateien, schreibt neue, ändert bestehende und speichert den Stand mit Git (mehr dazu in Dokument 3).

**Claude kann gut:**
- Texte schreiben und umschreiben: Hooks, Skripte, Captions, Kampagnenpläne.
- Ideen entwickeln und kritisch bewerten.
- Übersetzen und an den Ton eines Kontos anpassen (Deutsch, Englisch, Türkisch).
- Bilder und Screenshots ansehen und beschreiben, z. B. Statistiken ablesen oder einen Entwurf bewerten.
- Strukturiert arbeiten: Tabellen pflegen, Listen führen, Pläne aktuell halten.
- Im Internet recherchieren.
- Mit Verbindungen (Connectors) andere Werkzeuge bedienen, z. B. Canva.

**Claude kann nicht oder nur eingeschränkt:**
- **Videos ansehen.** Claude kann keine Videos abspielen. Schick ihm stattdessen Standbilder oder Screenshots und beschreib, was passiert.
- **Sich an alles erinnern.** Jeder Chat beginnt bei null. Was Claude wissen soll, muss im Repo stehen (deshalb gibt es `LAGE.md`, `CLAUDE.md` und das Journal).
- **Immer recht haben.** Claude klingt oft sehr sicher, auch wenn er sich irrt. Bei Spielerzahlen, Transfers, Ergebnissen und Daten immer prüfen.
- **Selbst veröffentlichen.** Das ist bei uns eine feste Regel. Du postest.

## Gute Aufträge geben

Die Faustregel: **Ziel, Kontext, Beispiel, Format.**

| Teil | Frage | Beispiel |
|---|---|---|
| Ziel | Was soll am Ende rauskommen? | „Ein TikTok-Skript, das Leute zum Kommentieren bringt.“ |
| Kontext | Was muss Claude wissen? | „Für das Süper-Lig-Konto. Ein bekannter Stürmer wurde diese Woche stark abgewertet, hier der Screenshot.“ |
| Beispiel | Wie soll es ungefähr aussehen? | „So ähnlich wie unser Post zum Team der Woche letzte Woche.“ |
| Format | In welcher Form? | „Hook, dann fünf Szenen mit Text, unter 30 Sekunden.“ |

**Schwacher Auftrag:**
> Mach mal einen Post über Bundesliga.

**Starker Auftrag:**
> Ich brauche ein Instagram-Karussell für das Bundesliga-Konto. Ziel: Debatte in den Kommentaren. Thema: Der Spieler mit der größten Aufwertung nach dem letzten Spieltag. Ton: frech, auf Deutsch. Format: 5 Folien, erste Folie ist der Hook, letzte Folie fragt nach der Meinung der Fans. Schreib mir drei Hook-Varianten zur Auswahl.

Weitere Tipps:
- **Varianten verlangen.** „Gib mir drei Hooks“ ist besser als „Gib mir einen Hook“. Du wählst aus.
- **Rolle geben.** „Bewerte das wie ein erfahrener TikTok-Stratege“ bringt eine schärfere Meinung.
- **Nach Gegenargumenten fragen.** „Was spricht gegen diese Idee?“
- **Screenshots mitschicken.** Ein Bild sagt Claude oft mehr als drei Sätze.
- **Skills nutzen.** Für viele Aufgaben gibt es fertige Abläufe (Dokument 2).

## Nachfragen und korrigieren

Das erste Ergebnis ist ein Entwurf. Korrigieren ist kein Zeichen, dass etwas schiefgeht, sondern der normale Weg.

- **Konkret sagen, was nicht passt.** Statt „gefällt mir nicht“ lieber „zu lang, und der Hook verrät schon die Auflösung“.
- **Einzelne Teile ändern lassen.** „Lass alles so, nur Szene 3 frecher.“
- **Zurückfragen.** „Warum hast du diesen Hook gewählt?“ Claude erklärt seine Gründe.
- **Claude widerspricht manchmal.** Das ist gewollt. Er sagt einmal, was er denkt, mit Begründung. Wenn du bei deiner Entscheidung bleibst, setzt er sie um.

Wenn du Claude korrigierst, fragt er: „Soll ich mir das nur für dich merken oder als Vorschlag fürs Team aufschreiben?“ So lernt das System mit (siehe unten und Dokument 2, Skill `/regel-vorschlag`).

## Chats, Regeln, Gedächtnis: wie das zusammenhängt

| Begriff | Was es ist | Wer ändert es |
|---|---|---|
| **Chat** | Ein Gespräch mit Claude. Er merkt sich alles innerhalb des Chats, aber nichts zwischen Chats. | Du |
| **`CLAUDE.md` (Wurzel)** | Die festen Regeln für alle Chats. Claude liest sie bei jedem Start automatisch. | Nur Burhan |
| **`content/CLAUDE.md` und `marketing/CLAUDE.md`** | Wie wir in den beiden Bereichen arbeiten: Ton, Abläufe, Gewohnheiten. | Alle Creator, mit Notiz am Dateiende |
| **`vorschlaege.md`** | Sammelstelle für Team-Vorschläge, bevor sie in die `CLAUDE.md` des Bereichs kommen. | Claude schreibt, Creator entscheiden |
| **`CLAUDE.local.md`** | Deine persönlichen Vorlieben. Nur auf deinem Rechner, wird nicht geteilt. | Du |
| **`LAGE.md`** | Das „Gedächtnis“ zwischen Chats: was läuft, was als Nächstes kommt. | Claude am Ende jeder Sitzung |

**Merke:** Was nicht im Repo steht, weiß der nächste Chat nicht. Darum aktualisiert Claude am Ende jeder Sitzung die `LAGE.md`.

## Wann ein neuer Chat sinnvoll ist

Ein Chat hat ein begrenztes Gedächtnis. Wird er sehr lang, fasst Claude ältere Teile zusammen, und Details gehen verloren. Starte einen neuen Chat, wenn:
- du mit einem ganz neuen Thema anfängst;
- der Chat sehr lang geworden ist und Claude Dinge vergisst, die du früher gesagt hast;
- Claude sich verrannt hat und immer wieder dieselben Fehler macht.

Vorher: Lass Claude die `LAGE.md` aktualisieren. Dann weiß der neue Chat, wo ihr steht.

Bei uns gibt es drei feste Chats: **Wiki** (Fragen), **Content** (Produzieren) und **Marketing** (Strategie). Den Start-Prompt für jeden Chat bekommst du im Wiki-Chat.

## Typische Fehler und wie du sie vermeidest

| Fehler | Besser |
|---|---|
| Zu kurzer Auftrag ohne Kontext | Ziel, Kontext, Beispiel, Format |
| Erstes Ergebnis einfach übernehmen | Varianten verlangen, kritisch nachfragen |
| Zahlen von Claude ungeprüft posten | In der App oder auf der Quelle prüfen; Claude nennt immer ein Stand-Datum |
| Alles in einem Riesen-Chat | Pro Thema ein Chat, `LAGE.md` aktuell halten |
| Passwörter oder Login-Codes in den Chat kopieren | Nie. Das ist eine feste Regel. |
| Claude ein Video schicken | Standbilder oder Screenshots schicken und beschreiben |
| Am Ende einfach den Chat schließen | Claude `LAGE.md` aktualisieren und committen lassen |

## Fakten prüfen

Claude kann sich irren und wirkt dabei oft überzeugend. Prüfe deshalb vor dem Veröffentlichen:
- **Spielerdaten** (Ratings, Werte, Auf- und Abwertungen) direkt in der FootPulse-App.
- **Ergebnisse, Transfers, Verletzungen** auf einer verlässlichen Seite (z. B. Transfermarkt, kicker, BBC Sport, Fotomaç).
- **Was die App kann** in `marke/produktfakten.md`. Der Skill `/faktencheck` hilft dabei.
