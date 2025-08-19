letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
print("****************This is a CAESAR CIPHER machine****************\n")


#caesar cipher

def caesar(word,shift_number,encode_decode):
    cipher_text=""
    if encode_decode=="decode":
                shift_number*=-1
    for char in word:
        if char not in letters:
            cipher_text+=char
        else:
            shifted_position = letters.index(char) + shift_number
            shifted_position%=len(letters)
            cipher_text += letters[shifted_position]  
    
    print(f"Here is the {encode_decode}d result: {cipher_text}")

 
#main Code
flag=False
while not flag:
    choice=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message=input("Type your message:\n").lower()
    shift_number=int(input("Type the shift number: \n"))
    
    caesar(message,shift_number,choice)
    choice2=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if choice2=="no":
        print("****************Thank-you****************")
        flag=True
    
