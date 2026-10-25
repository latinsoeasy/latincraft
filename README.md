# latincraft
⛏ LatinCraft – Pontes Survival

Minecraft-inspiriertes Vokabeltraining (Latein) zum Klett-Pontes-Gesamtband (Salve! + Lektion 1–34, 1111 Einträge).
Reines HTML/JavaScript, kein Server und keine Datenbank nötig.
Minecraft 风格的拉丁语单词默写游戏，词汇来自 Klett Pontes 词汇表。

## Spielprinzip / 玩法
- **Runde**: Lektionen einzeln oder mehrfach wählen, 10 / 20 / 50 Wörter. Frage auf Deutsch und/oder Englisch, das lateinische Wort wird getippt. Längenstriche (ā, ē …) sind egal, Tippfehler zählen als falsch.
- **Fehlerbank**: Falsche Wörter landen automatisch dort und können gezielt geübt werden. Ein Wort verlässt die Bank, wenn es in **3 verschiedenen Runden hintereinander** richtig ist. Ein Fehler setzt den Zähler auf 0.
- **Minecraft-Elemente**: XP und Level, 10 Herzen (Creeper-Treffer bei Fehlern), Combo-Bonus, Beute pro richtiger Antwort (Erde, Sand, Holz, Stein, Kohle, Eisen, Gold, Diamant).
- **Werkbank**: 50 verschiedene Rezepte, von der Holzspitzhacke bis zum Drachenei.
- **Karte**: Gebaute Items und Rohstoffe können auf einer Karte platziert werden. Die Karte startet bei 5×5 und wächst mit jeweils 50 gemeisterten Wörtern um eine Reihe, maximal 16×16. „Gemeistert“ = richtig beantwortet und nicht in der Fehlerbank.
- **Speicher**: Automatisch im Browser (localStorage). Export/Import als JSON-Datei zum Sichern oder für ein anderes Gerät.

## Dateien
| Datei | Zweck |
|---|---|
| `index.html` | gesamtes Spiel (HTML, CSS, JS, Pixelgrafiken werden im Code erzeugt) |
| `vocab.json` | Vokabeln (Lektion, Latein, Deutsch, Englisch) |
| `build_vocab.py` | erzeugt `vocab.json` aus der Klett-PDF
