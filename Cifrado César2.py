# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
num = int()

for char in text:
    if not char.isalpha() and not char.isdigit():
        continue
    char = char.upper()
                          #ord() es la funcion que obtiene el numero ascii del caracter  y le sumamos el caracter que sigue                      
    if char.isdigit():
        num = int(char) + 1
        
    if ord(code) == 32:
        code =" "
    else:  
        code = ord(char)  + 1

    if code > ord('Z'):
        code = ord('A')
    
    
    cifrado += chr(code)

print(cifrado)