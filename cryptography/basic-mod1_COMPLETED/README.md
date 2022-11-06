Description:

We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format


flag: picoCTF{R0UND_N_R0UND_B6B25531}


Made a python script to make the necessary conversions
