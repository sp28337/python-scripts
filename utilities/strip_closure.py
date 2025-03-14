def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(' ?!,.;')

print(strip1(' hello python!..'))
print(strip2(' hello python!..'))
