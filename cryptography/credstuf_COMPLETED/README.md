Description:

We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.


flag encrypted: cvpbPGS{P7e1S_54I35_71Z3}
flag: picoCTF{C7r1F_54V35_71M3}

For this i just opened usernames.txt and find the line where cultiris appears. Then I went to passwords.txt and get what was in that line.
By the type of the encrypted flag I thought that it was encrypted with Caesar cipher, so I just went to a site to decrypt it.
