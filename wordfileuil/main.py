from wordcount import wordcount
from nospace import nospace

def main():
    text = input()
    print(wordcount(text))
    print(nospace(text))

def __name__=="__main__":
    main()