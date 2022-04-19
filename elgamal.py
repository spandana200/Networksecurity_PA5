import random
from math import gcd


# Encrypt the message
def encrypt(msg, q, h, g):
    # selecting a random integer k
    k = random.randint(1,q-1) 
    K = pow(h, k, q)
    C1 = pow(g, k, q)
    # (axb)mod n = ((a mod n) x (b mod n)) mod n
    C2 = ((K%q)*(msg%q))%q    
    return C1, C2

# Decrypt the message
def decrypt(en_msg, p, key, q):
    K = pow(en_msg, key, q)
    # by using fermats's little theorem inverse of K mod q is pow(K,q-2,q) 
    dr_msg = ((p%q)*(pow(K,q-2,q)))%q  
    return dr_msg

def main():
    q = int(input("Enter a prime number q: "))

    # calculating primitive roots of q and storing them in an array
    required_set = {n for n in range(1, q) if gcd(n, q)==1 }
    primitive_roots=[g1 for g1 in range(1, q) if required_set == {pow(g1, powers, q)
            for powers in range(1, q)}]
    
    #choosing one primitive root from the array 
    alpha = random.choice(primitive_roots)
    print("Alpha: ",alpha)


    M=int(input("Enter the message less than q: "))
    print()

    #key generation
    XA = random.randint(1,q-2) # Private key 
    print("Private key: ",XA)
    YA = pow(alpha, XA, q)
    print("Public key: {" + str(q) + ","+ str(alpha) + "," + str(YA) + "}")
    C1, C2 = encrypt(M, q, YA, alpha)
    dmsg = decrypt(C1, C2, XA, q) 
   
    print()
    print("Original Message :", M)
    
    print ()
    print ("The encrypted message : (" + str(C1) + "," + str(C2) + ")")
    print ()
    print("Decrypted Message :", dmsg);
    print ()

if __name__ == '__main__':
 main() 