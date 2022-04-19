# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1   #ord() es la funcion que obtiene el numero ascii del caracter  y le sumamos el caracter que sigue
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)