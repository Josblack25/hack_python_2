"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    _ls = []
    
    if len(result) <= 1:
        return [0]
    
    for i in range(len(result)):
        if (i+1) % 2 !=0:
            _ls.append(str(i+1))
        elif (i+1) % 2 ==0:
            _ls.append(int(i+1))
    
    result = _ls
    print(result)
    return result
