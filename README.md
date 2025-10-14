**Teisendaja: baas 8 -> baas 2**\
**Johanna Okas KTA-25**

Siin on Pythonis kirjutatud programm, mis teisendab arve oktaalarvust (baas 8) binaararvuks (baas 2) käsureal värvilise tekstiväljundiga.

Tabelist "lookup_table.py" võtab "main_converter.py" info sisendi kontrollimiseks ning teisendamise teostamiseks.\
"Main_converter.py" sisu läks veidikene pikemaks, sest mul tekkis vajadus seda enda meelest ilusamaks teha.\
\
• Kõigepealt küsib programm kasutajalt oktaalarvu (_ENTER OCTAL NUMBER_)\
• Programm kontrollib, et sisend sisaldaks ainult numbreid 0-7 valideerimisfunktsiooniga `is_valid_octal()`\
• Funktsiooniga `convert_octal_to_binary()` teostatakse teisendamine, tulemused liidetakse stringiks, millest moodustub lõplik binaararv.\
• Kasutajal on seejärel valik, kas teisendada uut arvu või sulgeda programm.

