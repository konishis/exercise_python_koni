poem = """ mukashi mukashi \
    arutokoroni ojiisan to\
    obaasan ga imasita"""

print(len(poem))
font = open("Douwa.txt", "wt")
font.write(poem)
# print(poem, file=font)
font.close()
