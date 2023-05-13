import serial
from array import array 
 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)

print("Início da leitura de dados...") 

print(ser.inWaiting())
while True:
    try:
      linha = ser.readline()
    except IndexError:
      print("Deu erro de leitura")
      continue
    print(f"Saída do readline: {linha}")
    try:
      linha = linha.decode()
    except UnicodeDecodeError: 
     print("deu erro de decodificação")
     continue
    print(f"Saída do decode: {linha} do typo {type(linha)}")
    splitedArray = [s for s in linha.split(',')]
    print(f"Saída do array: {splitedArray}")
    print(splitedArray[0])
    print(splitedArray[1])
    print(f"Primeiro valor: {splitedArray[0]}, segundo valor {splitedArray[1]}")
    

ser.close()

