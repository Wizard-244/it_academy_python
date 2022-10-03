d = "Count the number of lowercase"
s = " and uppercase letters"
let_l = 0 # Upper letter
let_p = 0 # lower letter
print(d.lower())
print(s.upper())
print("Input letter")
f = input()
print(f)
for i in f:
    if "a" <= i <= "z":
        let_l += 1
    else:
        if "A" <= i <= "Z":
            let_p += 1
print ("lower letter")
print (let_l)
print ("upper letter")
print (let_p)