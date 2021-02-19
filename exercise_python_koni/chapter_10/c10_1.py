tmpfile = open("oops.txt", "wt")
print("Oops, I created a file.", file=tmpfile)
tmpfile.close()
