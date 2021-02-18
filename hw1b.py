# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:44:21 2021

@author: Mark
"""
key = bin(728).zfill(10)[2:] # 1100011110
#Sbox tables
S0 = [
        ["01", "00", "11", "10"],
        ["11", "10", "01", "00"],
        ["00", "10", "01", "11"],
        ["11", "01", "11", "10"]]
S1 =   [
        ["00", "01", "10", "11"],
        ["10", "00", "01", "11"],
        ["11", "00", "01", "00"],
        ["10", "01", "00", "11"]]

matrix = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

matrix2 = [ 
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]


def bin2dec(inp):
    if(inp == "00"):
        return 0
    if(inp == "01"):
        return 1
    if(inp == "10"):
        return 2
    if(inp == "11"):
        return 3

def s_box(inbit, s_mat):
    col = bin2dec(inbit[1] + inbit[2])
    row = bin2dec(inbit[0] + inbit[3])
    return s_mat[row][col]

#This will loop through 16^2 possible combinations and use the XOR function stored in z
    #We will use populate to build the tables for both S0 and S1
def populate():
    for z1 in range(16):
        for z2 in range(16):
            z = z1 ^ z2
            zb = str(bin(z))[2:]
            z10b = str(bin(z1))[2:]
            i = 0
            j = 0
            while i < 4-len(z10b):
                z10b = "0" + z10b
            z20b = str(bin(z2))[2:]
            while j < 4-len(z20b):
                z20b = "0" + z20b
            xor_z = str(bin(z))[2:]
            intz = int(xor_z,2)
            
    #S0 Differential Table creation

            S0x = s_box(z10b,S0)
            S0y = s_box(z20b,S0)
            xBin = bin2dec(S0x)
            yBin = bin2dec(S0y)
            y_xor = xBin ^ yBin #XOR
            xBin = str(bin(xBin))[2:]
            b = 0
            k = 0
            while b < 4-len(xBin):
                xBin = "0" + xBin
                
            yBin = str(bin(yBin))[2:]
            while k < 4-len(yBin):
                yBin += "0" + yBin
                
            yFin = str(bin(y_xor))[2:]
            y_xorint = int(yFin,2)
            matrix[intz][y_xorint] += 1 #Increment table


#S1 Differential Table creation
            a1 = s_box(z10b,S1)
            a2 = s_box(z20b,S1)
            a1Bin = bin2dec(a1)
            a2Bin = bin2dec(a2)
            a_xor = a1Bin ^ a2Bin
            a1Bin = str(bin(a1Bin))[2:]
            for i in range(4-len(a1Bin)):
                a1Bin = "0" + a1Bin
                
            a2Bin = str(bin(a2Bin))[2:]
            for j in range(4-len(a2Bin)):
                a2Bin = "0" + a2Bin
                
            binarya_xor = str(bin(a_xor))[2:]
            aint = int(binarya_xor,2)
            matrix2[intz][aint] += 1 #Increment S1 table
        
if __name__ == "__main__":      
    populate()
    print("Table S0: ")
    print("")
    print(matrix)
    print("")
    print("Table S1: ")

    print("")
    print(matrix2)