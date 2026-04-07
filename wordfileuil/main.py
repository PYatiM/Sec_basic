from wordcount import wordcount
from nospace import nospace
from toupperandlower import changetolower, changetoupper
from wordlistgenerator import generate
from wordlistcleaner import clean_wordlist
from file_word_extractor import extractor
from merger import merge_files
from statanalyse import analyze
from passpattgener import mutate, generate
from hashgenerator import generate_hashes


def main():
    while True:
        print("CHOOSE YOUR OPTION: \n1. Word Count \n2. No Space \n3. To Upper \n4. To Lower \n5. Wordlist generate \n6. Wordlist clean \n7. File word extractor \n8. File Merger  \n9. Statistic Analyzer \n10. Password pattern Generator \n11. Hash Generator \n12. Exit")
        opt = int(input("\nEnter your option : "))
        if opt==12:
            print("BYE BYE")
            break
        if opt!=6 or opt!=7 or opt!=8:
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
            case 8:
                print("Give absolute address of Input file : ")
                inter = input()
                merge_files(output,inter)
                break
            case 9:
                print("Give absolute address of Input file : ")
                inter = input()
                analyse(inter)
                break
            case 10:
                print("Give absolute address of Input file : ")
                inter = input()
                generate(inter, output)
                break
            case 11:
                print("Give absolute address of Input file : ")
                inter = input()
                generate_hashes(inter,output)
                break


if __name__=="__main__":
    main()