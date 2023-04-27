def decode_XKCD_tuple(xkcd_values, k):
    decoded = list(map(decode_value, xkcd_values))
    decoded.sort(reverse=True)
    return decoded[:k]
    pass

def decode_value(xkcd):
    return list_of_weights_to_number(xkcd_to_list_of_weights(xkcd))
    pass

def xkcd_to_list_of_weights(xkcd):
    weights = []
    for a in xkcd:
        if a == '0':
            weights[-1] += '0'            
        else:
            weights.append(a)
    weights = list(map(int, weights))
    return weights
    pass

def list_of_weights_to_number(weights):
    num = 0
    for i in range(len(weights)):
        cur = weights[i]
        if i < len(weights) - 1:
            nex = weights[i+1]
            if cur < nex:
                num -= int(cur)
            else:   
                num += int(cur)
        else:
            num += int(cur)
    return num

###################################################################################
if __name__ == '__main__':
    # add here your personal tests
    print(decode_XKCD_tuple(['100100100101005','1001001001010051','10010010010100511'], 2))
    # expected outcome is [395, 396, 397] → [397, 396]
    
