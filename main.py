# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        print("True")
    else:
        print("False")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_anagram("kevo", "voke")
