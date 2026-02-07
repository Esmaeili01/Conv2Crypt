from conv2crypt import *



text = "hello" 
kernel = [20 , 42 , 4 , 4 , 223 , 1]
cipher1 = conv_encrypt(text, kernel)
cipher2 = conv_encrypt(text, kernel)
print(cipher1)
print(cipher2)
print()
t1 = conv_decrypt(cipher1 , kernel)
t2 = conv_decrypt(cipher2 , kernel)
print(t1)
print(t2)