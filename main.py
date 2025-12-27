from conv2crypt import *

text = "hello" 
kernel = [0 ,  0  , 1]
cipher = conv_encrypt(text, kernel)
print(cipher)
t = conv_decrypt(cipher , kernel)
print(t)