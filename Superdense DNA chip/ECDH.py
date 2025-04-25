from libraries import *

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve_names = ['brainpoolP256r1', 'secp256r1']

index = secrets.randbelow(1)

curve_str = ''.join(curve_names[index])

print("Elliptic Curve:", curve_str)

curve = registry.get_curve(curve_str)

alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g
#print("Alice public key:", compress(alicePubKey))

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g
#print("Bob public key:", compress(bobPubKey))

aliceSharedKey = alicePrivKey * bobPubKey
#print("Alice shared key:", compress(aliceSharedKey))

bobSharedKey = bobPrivKey * alicePubKey
#print("Bob shared key:", compress(bobSharedKey))

A_shared_key = "{0:08b}".format(int(compress(aliceSharedKey), 16)) 
B_shared_key = "{0:08b}".format(int(compress(bobSharedKey), 16))

#print(len(A_shared_key))
#print(len(B_shared_key))

assert A_shared_key == B_shared_key

i_str = str(compress(aliceSharedKey)[2:])

for x in i_str:
	if int(x, 16) >= 1 and int(x, 16) <= 8:
		rule = int(x, 16)
		#print(rule)
		break

