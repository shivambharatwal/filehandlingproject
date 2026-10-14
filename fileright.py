with open("practice.txt","a") as file:
    file.write("This is taxt")

with open("practice.txt","r") as file:
    content= file.read()
    print(content)

