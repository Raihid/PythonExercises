
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
print(result)
# Kod jest poprawny


# for i in "qwerty": if ord(i) < 100: print i
# Wykomentowane, poniewaz niepoprawne. Musimy zmienic skladnie na taka:


for i in "axby": print ord(i) if ord(i) < 100 else i
# Teraz poprawne
