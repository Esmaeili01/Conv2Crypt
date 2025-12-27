from random import randint 
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def conv_encrypt (text : str , kernel : list) -> str : 
    text = text.upper()
    n = len(text)
    m = len(kernel)
    en_list = []
    for i in range(m-1): 
        en_list.append(randint(0,25))
    
    for i in range(n) :
        index = alphabet.find(text[i])
        sum = 0
        for j in range(m-1) : 
            sum += en_list[i+j]*kernel[j]

        x = (index - sum) // kernel[m-1] % 26
        en_list.append(x)
    
    cipher = ""
    for i in en_list:
        cipher += alphabet[i]

        
    return cipher

def conv_decrypt(cipher : str , kernel : list) -> str : 

    cipher = cipher.upper()
    n = len(cipher)
    m = len(kernel)
    text = ""
    for i in range(n - m + 1) : 
        sum = 0 
        for j in range(m) : 
            sum += alphabet.find(cipher[i+j]) * kernel[j]
        sum = sum % 26

        text += alphabet[sum]


    return text


