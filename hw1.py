# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:10:05 2021

@author: Mark Borelli II

SimplifiedDES implementation (Python)
This program is intended to implement a simple version of DES
and show accuracy on all test cases.
Key and plainText takes user input,
encrypts, and decrypts messages
Should be able to encrypt a plaintext, and then decrypt with key
"""
output = (0,0,0,0,0,0,0,0)
keyLength = 10 #length of key
#key = int(1100011110) #sample key
#key = bin(key)[2:].zfill(keyLength)
plainText = "00101000".zfill(8) #sample plaintext
plainLength = 8

#blank temporary table
#temp = (0,0,0,0,0,0,0,0,0,0)
#P10 and P8 tables for keys generation
P10 = (2, 4, 1, 6, 3, 9, 0, 8, 7, 5)
P8 = (5, 2, 6, 3, 7, 4, 9, 8)
#Switch tuple
SW = (4, 5, 6, 7, 0, 1, 2, 3)

#tables for initial and inverse permutation
IP = (1, 5, 2, 0, 3, 7, 4, 6)
IIP = (3, 0, 2, 4, 6, 1, 7, 5)

#permutation Expansion table
PE = (3,0,1,2,1,2,3,0)

#P4 Table
P4 = (1,3,2,0)

#Sbox tables
S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]]
S1 =   [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]]

#nifty little permutation function I decided to use instead of using individual
#functions for expansion, etc
def permutation(key,p):
    permutated_key = ''
    for i in p:
        permutated_key += key[i]
    return permutated_key
  
#Bit shift function using circuler left shift
def shift(temp,shift):
    initial_shift = temp[shift:]
    final_shift = initial_shift + temp[:shift]
    return final_shift

#produces keys 1&2
def keyg(k):
    key = bin(k)[2:].zfill(keyLength)
    key = permutation(key, P10) #P10 Permutation
    key = shift(key[:5],1) + shift(key[5:],1)
    k1 = permutation(key, P8) #P8 Permutation
    key = shift(key[:5],2) + shift(key[5:],2) #2nd shift
    k2 = permutation(key, P8)
    return k1,k2

'''#Splits CD0 into C0 and D0
def split(output):
    i = j = 0
    while i < 4:
        C0[i] = output[i]
        #print(C0[i])
        i+=1
    while j < 4:
        D0[j] = output[i]
        #print(D0[j])
        i+=1
        j+=1
    #D0 = ''.join(str(e) for e in D0)
    #C0 = ''.join(str(e) for e in C0)
'''
#Part P4 permutation
def p4(input):
    final = [0,0,0,0,0]
    k = 0
    while k < 4:
        final[k] = input[P4[k]]
        k += 1
    return output + final

#sbox function will yield 
#output for s1 or s2. 
def s_box(inbit, s_mat):
    col = int(inbit[1:3], 2)
    row = int(inbit[0]+inbit[3], 2)
    return bin(s_mat[row][col])[2:].zfill(2)

def F_function(r, skey):
    expansion = permutation(r,PE)
    inbit = bin(int(expansion,2)^int(skey,2))[2:].zfill(8)
    print(inbit)
    D0 = inbit[4:]
    C0 = inbit[:4]
    c_out = s_box(C0, S0)
    d_out = s_box(D0, S1)
    out = c_out + d_out
    return permutation(out, P4)

def f_map(c0,d0,key):
    c0_int = int((c0),2)
    out = (c0_int^int(F_function(d0,key),2))
    return bin(out)[2:].zfill(4),d0
    
#Encrypt function with test key
'''decrypt simply swap k1 and k2'''
def initial_permutations(inp, k1, k2, decrypt = False):
    if decrypt:
        k2,k1 = k1,k2
    inp = permutation(inp, IP)
    C0,D0 = f_map(inp[0:4],inp[4:],k1)
    C0,D0 = f_map(D0,C0,k2)
    x = permutation(C0+D0, IIP)
    return x

def encryption(plaintext,key,decrypt=False):
    k1,k2 = keyg(key) #get k1 and k2 from keyg function
    plaintext = bytes(plaintext, 'utf-8')
    #print(plaintext)
    for i in plaintext:
        inbit = bin(i)[2:].zfill(8)
        ciphertext = initial_permutations(inbit,k1,k2,decrypt)
    if(decrypt == False):
        print("Ciphertext: ", ciphertext, sep='')
    else:
        print("Decryption: ", ciphertext, sep='')

if __name__ == "__main__":
    #print("Plain text: " + plainText)
    #User input
    key = int(input("Enter number 0-1032: "))
    plainText = input("Enter plaintext: ")
    #plainText = plainText.zfill(8)
    encryption(plainText,key,False) #encrypt test
    encryption(plainText,key,True) #decrypt test