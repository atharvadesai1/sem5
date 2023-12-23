vowel = ['a','e','i','o','u']

def countvowel(s):
    count=0
    for i in range(len(s)):
        for v in vowel:
            if(s[i]==v):
                count+=1
    return str(count)

string = str(input("Enter the string:\n"))
print(f"\nTotal number of vowels in the string are {countvowel(string)}")