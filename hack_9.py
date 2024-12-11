"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    result = s
        
    ls = {}
    
    result.pop('bar')
    
    result['foo'] = 'fooziman'
        
    
    for key, value in result.items(): 
        new = key.capitalize() 
        if new not in result:
            ls[new] = value.capitalize()
             
             
    result = ls  
    print(result)
    return result
