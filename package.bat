mkdir quicksaveqml
mkdir quicksaveqml\i18n
xcopy *.py quicksaveqml
xcopy *.ui quicksaveqml
xcopy *.png quicksaveqml
xcopy README.md quicksaveqml
xcopy LICENSE quicksaveqml
xcopy metadata.txt quicksaveqml
xcopy i18n\quicksaveqml_ru.ts quicksaveqml\i18n\quicksaveqml_ru.ts
lrelease quicksaveqml\i18n\quicksaveqml_ru.ts
del quicksaveqml\i18n\*.ts
zip -r quicksaveqml.zip quicksaveqml
del quicksaveqml\i18n\*.qm
del /Q quicksaveqml
rd quicksaveqml\i18n
rd quicksaveqml