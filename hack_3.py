"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""
s = 'qu'

def fn_hack_3(s):
   result = s
    
   replac = ('u','v'), ('a','@'), ('e','3'), ('i','¡'), ('o','0')
    
   if result == "qu": 
      for a,b in replac:
         result = result.replace(a,b)
         result = result.capitalize()
   else:
        for a,b in replac:
         result = result.replace(a,b)    
         result = result.capitalize()[:-1] + result[-1].upper()
   
   print(result)
   return result

fn_hack_3(s)