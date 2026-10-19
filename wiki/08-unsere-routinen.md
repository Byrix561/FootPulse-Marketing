# 8. Unsere Routinen

## Das Wichtigste in fünf Sätzen

1. Einmal pro Woche, an einem festen Tag, gehen wir in etwa 20 Minuten Kennzahlen, Testergebnisse, Fan-Feedback und neue Inspiration durch (Skill `/wochenrueckblick`).
2. Jeder Test kommt ins Testjournal, mit Hypothese vorher und Zahlen nach 48 Stunden und 7 Tagen.
3. Diese Aufzeichnungen sind die Grundlage für den späteren 90-Tage-Plan, also für die Frage, wofür wir Geld ausgeben.
4. Am Ende jeder Arbeitssitzung aktualisiert Claude die `LAGE.md`, damit der nächste Chat weiß, wo wir stehen.
5. Medien liegen in OneDrive, Texte im Repo, und nicht-freie Bilder oder Musik tragen wir in die Bildrechte-Liste ein.

## Übersicht

| Routine | Was | Wann | Dauer | Wo | Skill |
|---|---|---|---|---|---|
| **Wochentermin** | Alles unten gemeinsam durchgehen, drei Erkenntnisse ziehen | Fester Wochentag | ca. 20 Min. | `journal/wochenrueckblick/` | `/wochenrueckblick` |
| **Kennzahlen** | Zahlen je Konto und Plattform | Wöchentlich, im Wochentermin | 5–10 Min. | `journal/kennzahlen/` | `/wochenrueckblick` |
| **Testjournal** | Jeder Test mit Hypothese und Ergebnis | Bei jedem Test, Zahlen nach 48 h und 7 Tagen | 2 Min. je Eintrag | `journal/tests.md` | `/test-eintragen` |
| **Fan-Feedback** | Wünsche, Kritik, Debatten, ohne Namen | Wöchentlich | 5 Min. | `feedback/fans.md` | `/wochenrueckblick` |
| **Hook-Bibliothek** | Hooks, die funktionieren | Sobald dir einer auffällt | 1 Min. | `inspiration/hooks.md` | `/hook-sammeln` |
| **Inspiration** | Vorbilder mit Begründung | Sobald dir etwas auffällt | 1 Min. | `inspiration/vorbilder.md` | `/hook-sammeln` |
| **Warteliste** | Gesamtzahl der Anmeldungen | Wöchentlich | 1 Min. | `marketing/warteliste.md` | `/wochenrueckblick` |
| **LAGE** | Was läuft, was kommt, was wartet | Ende jeder Sitzung | automatisch | `LAGE.md` je Bereich | Claude macht es |
| **Bildrechte-Liste** | Nicht-freie Medien | Wenn etwas Unfreies verwendet wird | 1 Min. | `rechte/nicht-freie-medien.md` | Claude fragt nach |

## Der Wochentermin

**Was:** Ein fester Termin pro Woche, ca. 20 Minuten. Der Marketing-Chat vereinbart den Tag beim ersten Start mit dir und kann eine geplante Aufgabe in der Claude-Desktop-App einrichten, die dich an diesem Tag mit `/wochenrueckblick` startet (nur mit deinem Ja).

**Ablauf:**
1. Kennzahlen: Screenshots der Statistiken aus Instagram, TikTok und X schicken. Claude liest sie ab und trägt sie ein.
2. Warteliste: Gesamtzahl der Anmeldungen.
3. Testergebnisse: Welche Tests haben jetzt Zahlen?
4. Fan-Feedback: Was fiel in den Kommentaren auf?
5. Neue Hooks und Inspiration.
6. Drei Erkenntnisse und was wir nächste Woche anders machen.
7. Offene Team-Vorschläge aus `vorschlaege.md` besprechen.

**Warum:** Weil wir sonst in drei Monaten nicht mehr wissen, was funktioniert hat. Diese 20 Minuten sind die wertvollste Zeit der Woche.

**Erinnerung:** Jeder Content- und Marketing-Chat prüft beim Start das Datum des letzten Wochenrückblicks. Ist er älter als 7 Tage, erinnert er dich einmal freundlich.

## Testjournal

**Was:** Für jeden Post, mit dem wir etwas ausprobieren: Hypothese, Konto, Plattform, Sprache, Format, Hook, Zahlen nach 48 Stunden und 7 Tagen, Erkenntnis in einem Satz.

**Warum:** Grundlage für den 90-Tage-Plan. Nur was wir aufgeschrieben haben, können wir später gezielt wiederholen und mit Budget skalieren.

**Wie:** `/test-eintragen`. Wenn du Claude von einem veröffentlichten Post erzählst, fragt er nach 48 Stunden und nach 7 Tagen nach den Zahlen.

## Kennzahlen

**Was:** Je Konto und Plattform pro Woche: Follower (und Veränderung), Reichweite bzw. Aufrufe, durchschnittliche Wiedergabedauer bzw. Retention bei Videos, Likes, Kommentare, Shares, Saves, Profilaufrufe, Link-Klicks. Dazu die Wartelisten-Anmeldungen gesamt.

**Wo findest du die Zahlen?**
- **Instagram**: Profil → Professionelles Dashboard → Insights.
- **TikTok**: Profil → Menü → Creator-Tools bzw. Business Suite → Analytics.
- **X**: Profil → Analytics (bzw. bei jedem Post das Statistik-Symbol).

(Die Menüs ändern sich manchmal. Schick Claude einen Screenshot, wenn du etwas nicht findest.)

**Tipp:** Einfach Screenshots machen und Claude schicken. Er trägt alles in `journal/kennzahlen/JJJJ-KWnn.md` ein.

## Fan-Feedback

**Was:** Was Fans kommentieren, kritisieren und sich wünschen. Zusammengefasst, **ohne Namen oder Kontonamen**.

**Warum:** Fans sagen uns, welche Spieler sie interessieren, welche Debatten zünden und was sie von der App erwarten. Das ist Stoff für neuen Content und wertvoll für Burhan.

## Hook-Bibliothek und Inspiration

**Was:** Hooks und Posts (eigene und fremde), die funktionieren, mit Begründung, warum.

**Warum:** Gute Hooks sind Muster, die man wiederverwenden kann. Wer eine volle Bibliothek hat, startet nie bei null.

**Wie:** Link oder Screenshot an Claude schicken und `/hook-sammeln` sagen.

## LAGE

**Was:** Jede `LAGE.md` ist eine Seite: oben das Datum, dann was läuft, was als Nächstes kommt, was wartet.

**Warum:** Claude vergisst zwischen Chats alles. Die `LAGE.md` ist sein Gedächtnis.

**Wie:** Claude aktualisiert sie am Ende jeder Sitzung selbst. Sag zum Schluss einfach: „Wir sind fertig für heute.“

## Bildrechte-Liste

**Was:** Alles, was wir ohne freie Lizenz verwenden, steht in `rechte/nicht-freie-medien.md` (was, wo verwendet, Quelle, Datum).

**Warum:** Wenn sich jemand beschwert, wissen wir sofort, welcher Post betroffen ist, und können reagieren.

**Wie:** Claude sagt dir, wenn etwas nicht frei ist, und fragt, ob er es eintragen soll. Freie Quellen stehen in `rechte/freie-quellen.md`.

## OneDrive: wo die Medien liegen

Videos, Bilder und Musik gehören nicht ins Repo, sondern in den OneDrive-Ordner **„FootPulse Marketing“**:

```
FootPulse Marketing/
  00 Marke/             Logo, Schriften, Canva-Exporte der Vorlagen
  01 Rohmaterial/       eigene Aufnahmen, Bildschirmaufnahmen der App, KI-Rohclips
     Bundesliga/  Premier League/  Süper Lig/  FootPulse/
  02 In Arbeit/         je Projekt ein Ordner: JJJJ-MM-TT_konto_kurztitel
  03 Fertig/            exportierte, freigegebene Dateien, gleiche Benennung
  04 Veröffentlicht/    Archiv nach Monat: 2026-10/
  05 Musik und Sounds/  nur freie Quellen, mit Lizenzhinweis als Textdatei
  06 Vorlagen/          CapCut- und Canva-Vorlagen, Untertitel-Stile
```

**Benennung:** `2026-10-24_bundesliga_totw-spieltag8_v2.mp4` (Datum, Konto, Kurztitel, Version).

Im Repo steht zu jedem Projekt der Link zum OneDrive-Ordner. So findet jeder alles: Text im Repo, Medien in OneDrive.

**Wie bekommst du einen OneDrive-Link?** Rechtsklick auf den Ordner → „Freigeben“ bzw. „Link kopieren“. Den Link gibst du Claude, er trägt ihn in die Datei ein.
