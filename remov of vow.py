# remo-vowels
n=int(input())
s=input()[:n]
s=s[::-1]
a=['a','e','i','o','u']
f=['']
for i in s:
    if i not in  a:
        f.append(i)
print(f)
        
        
    
