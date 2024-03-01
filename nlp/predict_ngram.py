import numpy as np
import tiktoken

from n_gram import train_trigram

enc = tiktoken.encoding_for_model("davinci")
tokenizer = enc.encode
trigram = train_trigram()

prompt = "The most beautiful proof in math is"
tokens = tokenizer(prompt)
next_word = ""

for i in range(5):
    values, probabilities = [], []
    for word in range(enc.n_vocab):
        prob = trigram.n_gram_probability([tokens[-2], tokens[-1], word])
        values.append(word)
        probabilities.append(prob)

    top = sorted(zip(values, probabilities), key=lambda x: x[1], reverse=True)[:50]
    values, probabilities = zip(*top)

    print([enc.decode([i]) for i in values[:10]], probabilities[:10])

    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    next_word = np.random.choice(values, p=probabilities)
    tokens.append(next_word)

print(tokens)
for t in tokens:
    print(f"'{enc.decode([t])}'")
print(enc.decode(tokens))
