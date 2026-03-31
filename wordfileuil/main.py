from wordcount import wordcount
from nospace import nospace
from toupperandlower import changetolower, changetoupper
from wordlistgenerator import generate
from wordlistcleaner import clean_wordlist
from file_word_extractor import e

def main():
    while True:
        print("CHOOSE YOUR OPTION: \n1. Word Count\n2. No Space \n3. To Upper \n4. To Lower \n5. Wordlist generate \n6. Wordlist clean \n7. File word extractor \n8. Exit")
        opt = int(input("\nEnter your option : "))
        if opt==8:
            print("BYE BYE")
            break
        if opt!=6 or opt!=7:
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
            case 5:
                print(generate(text))
                break
            case 6:
                print("Give absolute address of Input file : ")
                inter = input()
                print(clean_wordlist(inter,output))
                break
            case 7:
                print("Give absolute address of Input file : ")
                inter = input()
                print(extractor(inter))
                break


if __name__=="__main__":
    main()