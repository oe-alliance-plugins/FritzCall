

# <p align="center">FritzCall Plugin for Enigma2 (E²) ![GitHub repo size](https://img.shields.io/github/repo-size/oe-alliance-plugins/FritzCall.svg)</p>

**Show Incoming and Outgoing Calls on your TV Screen with a Fritz!Box**


## Github status
[![Build](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/buildbot.yml/badge.svg)](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/buildbot.yml)
[![Lint Status](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/pylint.yml/badge.svg)](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/pylint.yml)
[![Ruff Status](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/ruff.yml/badge.svg)](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/ruff.yml)
[![Build Status](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/compile.yml/badge.svg)](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/compile.yml)
[![AUTOTAG](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/autotag.yml/badge.svg)](https://github.com/oe-alliance-plugins/FritzCall/actions/workflows/autotag.yml)


[![Plugin Version](https://img.shields.io/github/v/tag/oe-alliance-plugins/FritzCall?label=Latest%20Version&color=darkviolet)](https://github.com/oe-alliance-plugins/FritzCall/tags)
[![Latest Release](https://img.shields.io/github/release-date/oe-alliance-plugins/FritzCall?label=From&color=darkviolet)](https://github.com/oe-alliance-plugins/FritzCall/releases/latest)
[![Github last commit](https://img.shields.io/github/last-commit/oe-alliance-plugins/FritzCall)](https://github.com/oe-alliance-plugins/FritzCall)
[![GitHub Activity](https://img.shields.io/github/commit-activity/y/oe-alliance-plugins/FritzCall.svg?label=commits)](https://github.com/oe-alliance-plugins/FritzCall/commits)
[![GitHub Activity](https://img.shields.io/github/commit-activity/m/oe-alliance-plugins/FritzCall.svg?label=commits)](https://github.com/oe-alliance-plugins/FritzCall/commits)

## SonarCloud status
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=bugs)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=oe-alliance-plugins_FritzCall&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)

[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-light.svg)](https://sonarcloud.io/summary/new_code?id=oe-alliance-plugins_FritzCall)

---

### 📦 FritzCall Overview

Das FritzCall-Plugin zeigt Anrufe, die auf einer FRITZ!Box Fon ankommen oder über diese rausgehen, auf dem Fernseher an.(*) Darüberhinaus bietet es noch Folgendes an:

- War die Dreambox im Standby wird optional eine Zusammenfassung der Anrufe bei Wiedereinschalten angezeigt.
- Unbekannte Nummern werden versucht über diverse Websites aufzulösen.
- Es hat ein internes Telefonbuch, in dem gefundene Nummern gespeichert werden können.
- Das Telefonbuch der FRITZ!Box Fon kann eingelesen und benutzt werden.
- Dieses interne Telefonbuch kann bearbeitet werden.
- Die Anzeige kann auf bestimmte eigene Nummern eingeschränkt werden
- Es wird ein Anruferbild angezeigt, wenn ein entsprechendes Bild (PNG mit 256 Farben) mit dem Namen oder der Nummer des Anrufers im Verzeichnis <Lokation des Telefonbuchs>/FritzCallFaces existiert

(*) Dazu muss an einem Telefon, dass direkt an der FRITZ!Box Fon angeschlossen ist, die Folge `#96*5*` eingeben und gewählt werden. Des weiteren muss "Zugriff für Anwendungen zulassen" in der FRITZ!Box aktiviert werden (Heimnetzübersicht/Netzwerkeinstellungen). Dokumentation und Screenshots finden sich hier.

Die ipk-Datei installiert man auf der Box mit ```opkg install <Dateiname>```.
Unter Umständen muss man vorher noch die existierende Installation entfernen mit ```opkg remove enigma2-plugin-extensions-fritzcall```.

Wenn ihr nicht wollt, dass der nächste FW-Update das Plugin überschreibt ```opkg flag hold enigma2-plugin-extensions-fritzcall```.

Ansonsten Installation eines tar-Ball. Installation (am besten über eine bestehende Installation):

- Datei auf die Dreambox nach /tmp spielen.
- Auf der Dreambox dann: "cd /; tar xvzf /tmp/FritzCall.tar.gz"
- Falls noch nicht installiert, twisted-web, python-json und python-html installieren
- Dann Enigma neu starten.
- In der Konfiguration unbedingt die Firmware-Version richtig einstellen!
- Die Rückwärtssuche wird gesteuert von der Datei reverselookup.xml im Plugin-Verzeichnis. Da sich diese meist öfter ändert als das Plugin, stelle ich sie, wenn nötig, separat zur Verfügung. Eine neue Version braucht nur in das Plugin-Verzeichnis /usr/lib/enigma2/python/Plugins/Extensions/FritzCall kopiert zu werden. Das Plugin sollte eine neue Version automatisch erkennen und diese neu einlesen. Die aktuellste Version stelle ich zukünftig hier zur Verfügung.

DrMichael

PS:
- Die aktuelle Version speichert das interne Telefonbuch nun in Phonebook.json
- Wenn Logging auf DEBUG steht, werden u.U. Dateien mit sensiblen Informationen unter "/tmp/Fritz..." angelegt.
- Die neueren Versionen speichern das Passwort verschlüsselt. Daher kann es zu Fehlermeldung bzgl. Benutzer/Passwort kommen. Dann Passwort neu eingeben in der Konfiguration.
- Um alle weiteren Fragen danach zuvorzukommen: Nein, es wird kein Timeshift/Anhalten des Bildes bei Anruf geben analog Mute.

---

### 🙏 Credits

**👨‍💻 Author:**

- original Idea and Created by <a href="https://github.com/DrMichael">**DrMichael**</a>

** Special Thanks **
- All contributors and testers
- Open source community
- Enigma2 developers

---

### 📜 License Information [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation

This plugin is released under GPLv3. See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html#license-text) for full details.

<img width="120" height="58" alt="GPLv3_Logo svg" src="https://github.com/user-attachments/assets/67d32b0a-2a44-4fa9-a972-202daf28808e" />

---

### 🤝 Contributing & Contact

FritzCall is created by users for users and we welcome every contribution. There are no highly paid developers. There are only users who have seen a problem and done their best to fix it. This means FritzCall will always need the contributions of users like you. How can you get involved?

For questions or feedback, feel free and please open an issue or contribute with a Pull Request!

Pull requests are very welcome for:
- **Coding:** Developers can help by fixing a bug, adding new features, Integration improvements, Feature enhancements
- **Localization:** Translate into your native language.
- **Helping users:** Our support process relies on enthusiastic contributors like you to help others.

Your contribution is very welcome! Follow these steps:

1. 🍴 Fork this repository
2. 🔄 Create a branch for your feature
3. 💻 Make your changes
4. ✅ Commit using conventional messages
5. 📤 Push to your branch
6. 🔍 Open a Pull Request

Enjoy and help us improve it today. :)

### 🚨 Disclaimer

The project author is not responsible for how this software is used by others. It is not intended to be used for accessing or distributing copyrighted materials without authorization.
Users are solely responsible for determining the legality of their actions.

This repository has no control over the streams, links, or the legality of the content provided by the different hosts (including all mirror sites). It is the end user's responsibility to ensure the legal use of these streams, and we strongly recommend verifying that the content complies with all applicable laws, including copyright laws and regulations of your countrys jurisdiction before use.

---

⭐️ If you find this plugin useful, please give it a star on GitHub!
Thanks! ❤️ 💞 💖 ❤️‍🔥 💗
