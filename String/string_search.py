#find, index,rfind

message=' the quick brown fox jumped over the lazy dog'
idx=message.find('own')
if idx != -1:
    print(f'find own at index {idx}')
else:
    print('Not found')

idx= message.find('owl')
if idx != -1:
    print(f'find own at index {idx}')
else:
    print('Not found')

idx=message.find('azy')
print(idx)