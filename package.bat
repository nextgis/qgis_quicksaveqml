mkdir quicksaveqml
xcopy *.py quicksaveqml
xcopy *.png quicksaveqml
xcopy README.md quicksaveqml
xcopy LICENSE quicksaveqml
xcopy metadata.txt quicksaveqml
zip -r quicksaveqml.zip quicksaveqml
del /Q quicksaveqml
rd quicksaveqml