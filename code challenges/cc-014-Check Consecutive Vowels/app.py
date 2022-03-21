sentence=input("Please enter a string: ").strip().lower()
vowel= "aeiou"
count=0
for i in range(len(sentence)-1):
    if sentence[i] in vowel and sentence[i+1] in vowel:
        count+=1

if count != 0:
    print("Positive")
else:
    print("Negative")