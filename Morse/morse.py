


DIT = 0
DAH = 1

morse_code = {
  "a" : [DIT, DAH],
  "b" : [DAH, DIT, DIT, DIT],
  "c" : [DAH, DIT, DAH, DIT],
  "d" : [DAH, DIT, DIT],
  "e" : [DIT],
  "f" : [DIT, DIT, DAH, DIT],
  "g" : [DAH, DAH, DIT],
  "h" : [DIT, DIT, DIT, DIT],
  "i" : [DIT, DIT],
  "j" : [DIT, DAH, DAH, DAH],
  "k" : [DAH, DIT, DAH],
  "l" : [DIT, DAH, DIT, DIT],
  "m" : [DAH, DAH],
  "n" : [DAH, DIT],
  "o" : [DAH, DAH, DAH],
  "p" : [DIT, DAH, DAH, DIT],
  "q" : [DAH, DAH, DIT, DAH],
  "r" : [DIT, DAH, DIT],
  "s" : [DIT, DIT, DIT],
  "t" : [DAH],
  "u" : [DIT, DIT, DAH],
  "v" : [DIT, DIT, DIT, DAH],
  "w" : [DIT, DAH, DAH],
  "x" : [DAH, DIT, DIT, DAH],
  "y" : [DAH, DIT, DAH, DAH],
  "z" : [DAH, DAH, DIT, DIT],
  "0" : [DAH, DAH, DAH, DAH, DAH],
  "1" : [DIT, DAH, DAH, DAH, DAH],
  "2" : [DIT, DIT, DAH, DAH, DAH],
  "3" : [DIT, DIT, DIT, DAH, DAH],
  "4" : [DIT, DIT, DIT, DIT, DAH],
  "5" : [DIT, DIT, DIT, DIT, DIT],
  "6" : [DAH, DIT, DIT, DIT, DIT],
  "7" : [DAH, DAH, DIT, DIT, DIT],
  "8" : [DAH, DAH, DAH, DIT, DIT],
  "9" : [DAH, DAH, DAH, DAH, DIT],
  "0" : [DAH, DAH, DAH, DAH, DAH],
  "." : [DIT, DAH, DIT, DAH, DIT, DAH],
  "," : [DAH, DAH, DIT, DIT, DAH, DAH],
  "?" : [DIT, DIT, DAH, DAH, DIT, DIT],
  "'" : [DIT, DAH, DAH, DAH, DAH, DIT],
  "!" : [DAH, DIT, DAH, DIT, DAH, DAH],
  "/" : [DAH, DIT, DIT, DAH, DIT],
  "(" : [DAH, DIT, DAH, DAH, DIT],
  ")" : [DAH, DIT, DAH, DAH, DIT, DAH],
  "&" : [DIT, DAH, DIT, DIT, DIT],
  ":" : [DAH, DAH, DAH, DIT, DIT, DIT],
  ";" : [DAH, DIT, DAH, DIT, DAH, DIT],
  "=" : [DAH, DIT, DIT, DIT, DAH],
  "+" : [DIT, DAH, DIT, DAH, DIT],
  "-" : [DAH, DIT, DIT, DIT, DIT, DAH],
  "_" : [DIT, DIT, DAH, DAH, DIT, DAH],
  "\"" : [DIT, DAH, DIT, DIT, DAH, DIT],
  "$" : [DIT, DIT, DIT, DAH, DIT, DIT, DAH],
  "@" : [DIT, DAH, DAH, DIT, DAH, DIT],
  "EOW": [DIT, DIT, DIT, DAH, DIT, DAH],
  "ERROR": [DIT, DIT, DIT, DIT, DIT, DIT, DIT, DIT],
  "OVER": [DAH, DIT, DAH],
}

def get_code(char):
    code = morse_code[char.lower()]
    sound=""
    for bit in code:
        if bit == 0:
            sound += "DIT "
        else:
            sound += "DAH "
    return sound

print(f"C: {get_code('C')}")
