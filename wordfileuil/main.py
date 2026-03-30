from wordcount import wordcount
from nospace import nospace
from toupperandlower import changetolower, changetoupper

def main():
    while True:
        print("CHOOSE YOUR OPTION: \n1. Word Count\n2. No Space \n3. To Upper \n4. To Lower \n5. Exit")
        opt = int(input("\nEnter your option : "))
        if opt==5:
            print("BYE BYE")
            break
        text = input("Enter the text : ")
        match(opt):
            case 1:
                print(wordcount(text))
                break
            case 2:
                print(nospace(text))
                break
            case 3:
                print(changetoupper(text))
                break
            case 4:
                print(changetolower(text))
                break

if __name__=="__main__":
    main()