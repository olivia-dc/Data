import random
dataset_file = """my friend makes the best raspberry pies in town
i think apple pies are the best pies
steve thinks apple makes the best computers in the world
I own two computers and they’re not apple because I am not steve or rich """
model = {}
for line in dataset_file.split('\n'):
    line = line.lower().split()
    for i, word in enumerate(line):
        if i == len(line)-1:   
            model['END'] = model.get('END', []) + [word]
        else:    
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i+1]] 
generated = []
while True:
    if not generated:
        words = model['START']
    elif generated[-1] in model['END']:
        break
    else:
        words = model[generated[-1]]
    generated.append(random.choice(words))
print(generated)