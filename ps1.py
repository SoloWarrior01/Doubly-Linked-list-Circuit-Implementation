f = open('ps1.bin', 'w+b')
array = [20,4,255,8,10,9,0,6,2,5,12,4,15,17,9,1,2,30,22,12,19,18,35,255,17]
binary_format = bytearray(array)
f.write(binary_format)
f.close()
