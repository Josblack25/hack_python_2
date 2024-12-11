"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    
    _ls = []
    
    sl = []
    
    salida = []
    
    for i in result:
        for j in i.keys():
            _ls.append(str(j))
            for h in i.values():
                _ls.append(str(h))

        
    for f in range(len(_ls)):
       sl.append(str(f+1))
    

    dic = [{sl[i]: sl[i+1]} for i in range( 0, len(sl), 2)]
    
    result = dic

    print(result)
    return result