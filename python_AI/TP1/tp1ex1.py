S = int(input("Enter a number of seconds  : "))

rest = S % 3600
H = S // 3600

S = rest

rest = S % 60
M = S // 60

S = rest

print(H, "h ", M, "min ", S, "sec.")


