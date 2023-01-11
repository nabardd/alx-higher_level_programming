
def roman_to_int(roman_string):
    roman_string = roman_string.lower()
    integer = 0

    numerals = {
      "i": 1,
      "v": 5,
      "x": 10,
      "l": 50,
      "c": 100,
      "d": 500,
      "m": 1000
    }

    for i in range(len(roman_string)):
        if (roman_string[i] not in list(numerals.keys())):
            return 0

        if (
          (i != (len(roman_string) - 1))
          and (numerals[roman_string[i]] < numerals[roman_string[i + 1]])):
            integer += numerals[roman_string[i]] * -1
        else:
            num += numerals[roman_string[i]]

    return integer
