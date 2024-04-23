text_str = \
'''999-222-7777
444-555-6666
'''
'''
text_str

print(text_str)


import re
pattern = re.compile(r'[5-9]\d{2}-\d{3}-\d{4}')
matches = pattern.finditer(text_str)


for match in matches:
    print(match)


pattern = re.compile (r'\d{3} -\d{3}-\d{4}')

matches = pattern.finditer (text_str)


for match in matches:
    print(match)




matches_iter = pattern.finditer (text_str)
matches_all = pattern.findall (text_str)

print(matches_iter)
print(matches_all)
'''
import re

text_str = '''
999-888-7777
567.666.7777
567 888 9999'''

'''pattern = re.compile (r'([5-9]\d{2})[-.\s](\d{3})[-.\s](\d{4})')

output = re.sub(pattern, '\\1 \\2 \\3' , text_str)

print(output)'''


with open ('exercise.txt', 'r') as f:
    data = f.read()


print(data)


pattern = re.compile(r'(\d{1,})\s+\+\s+(\d{1,}\s+=')
output = re.sub(pattern, '\\1 \\2',data)
print(output)

match_iter = pattern.finditer(data)
for match in match_itrt:
    print(match.group(1).match.group(2))

#add

pattern = re.compile(r'(\d+)\s+(\d+)\s+=')
output = re.sub(pattern, '\\1 \\2',data)

print(output)

match_iter = pattern.finditer(data)
for match in match_iter:
    print(match.group(1), '+', match.group(2), '=', int(match.group(1)) + int(match.group(2)))

























