from conv2crypt import *

text = "helloworld" 
kernel = [1 , 1 , 1]
cipher = conv_encrypt(text, kernel)
print(cipher)
t = conv_decrypt(cipher , kernel)
print(t)