import random
dataset_file = """my friend makes the best raspberry pies in town
i think apple pies are the best pies
steve thinks apple makes the best computers in the world
I own two computers and they’re not apple because I am not steve or rich """

def model_grammar(str):
    model = {}
    for line in str.split('\n'):
        line = line.lower().split()
        for i, word in enumerate(line):
            if i == len(line)-1:
                model['END'] = model.get('END', []) + [word]
            else:
                if i == 0:
                    model['START'] = model.get('START', []) + [word]
                model[word] = model.get(word, []) + [line[i+1]]
    return model
modeled_gram = model_grammar(dataset_file)
# words = model_grammar.model['START']
# print(modeled_gram[1])
def generated_n(gram):
    generated = []
    while True:
        if not generated:
            words = gram['START']
        elif generated[-1] in gram['END']:
            break
        else:
            words = gram[generated[-1]]
        generated.append(random.choice(words))
    return generated
new_gram = generated_n(modeled_gram)
print(new_gram)
