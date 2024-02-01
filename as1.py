def echo(text:str, repetitions: int =3)->str:
    textstr=text[-3:]
    print(textstr)
    for element in range (0,repetitions-1):
        textstr=textstr[1::]
        print(textstr)
    return "."
if __name__=="__main__":
    text=input("yell something at mountain:")
    print(echo(text))