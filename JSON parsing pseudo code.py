d = {'abc': 'abc', 'def': {'ghi': 'ghi', 'jkl': 'jkl'}}
for element in d.values():
    if isinstance(element, dict):
       for k, v in element.items():
           print(k,v)