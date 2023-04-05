#3
#Using Format Str
#And multi line string


srt_eva = '5 + 3 * (2+1) ** 2'
result_eva = eval(srt_eva) #Using  eval()
print(f'{srt_eva} = {result_eva}') #Using string format

print('''
Explination
(5 + 3 * (2+1) ** 2)
           |     
  (5 + 3 * 3 ** 2)
             |
    (5 + 3 * 9)
           |
     (5 + 27)
        |
       32
''')  #Using multiline string