"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s

    delet = ['f','b','n']
    
    _str = []
    
    for txt in result:
        if txt not in delet:
            _str.append(txt)
            
    result = ''.join(_str)        
    return result
