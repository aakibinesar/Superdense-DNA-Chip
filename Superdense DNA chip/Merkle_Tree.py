from libraries import *

def hash_data(data):
    """Hashes the input data using SHA-256"""
    #return hashlib.sha256(data.encode('utf-8')).hexdigest()
    return ColorHash(data).hex	

def merkle_tree(leaves):
    """Generates a Merkle Tree and returns the root hash"""
    # Hash the leaves to create the first level of the tree
    layer = [hash_data(leaf) for leaf in leaves]
    #print('Color hash values of ciphertext strands: ', layer)

    # Build the tree upwards
    while len(layer) > 1:
        # Pair up the nodes and hash them together
        if len(layer) % 2 != 0:  # If there's an odd number, duplicate the last element
            layer.append(layer[-1])
        
        # Hash each pair of nodes
        layer = [hash_data(layer[i] + layer[i + 1]) for i in range(0, len(layer), 2)]
        print(layer)

    return layer[0]  # The root of the Merkle tree
