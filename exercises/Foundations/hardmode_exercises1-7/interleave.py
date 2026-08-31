def interleave(l, k):
    combined = [x for pairs in zip(l, k) for x in pairs]

    longer = l if len(l) > len(k) else k

    combined += longer[min(len(l), len(k)):]

    return combined

l = [1,2,3,4,5]
k = [6,7,8,9,10,11,12]

print(interleave(l, k))