# dic = {"n": 42,"f": 7.03,"s": "string cheese"}

# print("{0[n]} {0[f]} {0[s]} {1} {2}".format(dic, "other","test"))


# n= 42
# f=7.03
# s = "string cheese"
# print('{0:d} {1:f} {2:s}'.format(n, f, s))


# print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s="string cheese"))


# n= 42
# f=7.03
# s = "string cheese"
# print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))

n= 42
f=7.03
s = "string cheese"
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

n= 42
f=7.03
s = "string cheese"
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

n= 42
f=7.03
s = "string cheese"
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

n= 42
f=7.03
s = "string cheese"
print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))