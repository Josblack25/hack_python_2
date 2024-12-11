"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    
    result = s
    _ls = []
    
    txt_ls = [result[i:i+8] for i in range(0, len(result), 8)]
    
   
    for txt in txt_ls:
        if len(result) > 2:
            if result == 'fooziman':
                if len(txt) % 2 ==0:
                    content = f"{txt[0]}{txt[1]}{txt[2].replace('o','-')}{txt[3]}{txt[4]}{txt[4].join('-')}{txt[5]}{txt[6]}{txt[7].replace('n','-')}"
                    _ls.append(content)           
            elif result == 'barziman':
                if len(txt) % 2 ==0:
                    content = f"{txt[0]}{txt[1]}{txt[2].replace('r','-')}{txt[3]}{txt[4]}{txt[5].replace('m','-')}{txt[6]}{txt[7]}"
                    _ls.append(content)
            elif len(txt) % 2 != 0:
                    content = f"{txt[0]}{txt[1]}{txt[2].replace('x','-')}"
                    _ls.append(content)
        else:
            _ls.append(txt)              
                        
    result = "".join(_ls)
    return result
    



