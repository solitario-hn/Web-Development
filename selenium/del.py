am="Time machine - 123,456,789"
amt=am.split(' - ')[1].strip().replace(',',"")
key=am.split('-')[1].replace(',',"")
print(int(amt))
print(int(key))

int(key)
#element_text.split("-")[1].strip().replace(",", "")