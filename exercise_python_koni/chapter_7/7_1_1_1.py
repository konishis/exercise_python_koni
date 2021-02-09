def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s",value2="%s"' % (value, name, value2))

unicode_test('\u9999')

place = 'caf\u00e9'
print(place)