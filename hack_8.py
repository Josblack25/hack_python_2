"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    _ls = []
    
    conten = len(result)
    
    if conten % 2 !=0:
        for i in range(len(result)):
            _ls.append(f'{result[i]}-{i+1}')        
    else:
        for i in range(len(result)):
            _ls.append(str(i+1))
        
    result = _ls
    result.reverse()
    print(result)
   
    return result
