#exercise 3

#Input a binary in string and convert it to a number in int
def bin_to_dec(string):
    dec = 0
    for i in range(len(string)-1,-1,-1):
        dec += (2**i)*(int(string[i]))
    return dec

print(bin_to_dec("1010101"))

#Input a number and retrieve the binary notation
def dec_to_bin(num):
    #Initalize a list to put the binary notation in
    bin = []
    #Representing an exponenet
    e = 0
    var = 2**e

    #Find the power of 2 right after the num inputted
    while var < num:
        e += 1
        var = 2**e

    #Find the binary notation
    for i in range(e-1,-1,-1):
        var = 2**i
        if num//var == 1:
            bin.append("1")
            num -= var
        else:
            bin.append("0")

    #Format the binary to look nicer
    bin = ''.join(bin)
    return bin

print(dec_to_bin(85))
    
