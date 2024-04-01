import string

statement = '''“The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.” ''' .lower()

texto = statement

print(f'Statement: {texto}')

for c in string.punctuation:
  texto = texto.replace(c, ' ')

resultante = []
for p in texto.split():
  if p[0] in 'python' or p[-1] in 'python':
    resultante.append(p)
    
print (f'Lista {resultante}')

#video twp280