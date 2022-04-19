# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1 #ord() es la funcion que obtiene el numero ascii del caracter  y le restamos el caracter que sigue
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
