# True = English; False = German
english = True

# True = LSTM; False = GRU
lstm = True

# Learning Rate
adam = 0.001

# Batch size
batch_size = 32


if english:
    training_file = "english/en_gum-ud-train.conllu"
    dev_file = "english/en_gum-ud-dev.conllu"
    test_file = "english/en_gum-ud-test.conllu"
else:
    training_file = "german/de_hdt-ud-train-a-1.conllu"
    dev_file = "german/de_hdt-ud-dev.conllu"
    test_file = "german/de_hdt-ud-test.conllu"


from conllu import parse_incr

def corpora2sentences_and_tags(files):
    fds = [open(file, "r", encoding="utf-8") for file in files]

    sentences = []
    sentence_tags = []

    for fd in fds:
        for sentence in parse_incr(fd):
            s = []
            s_tag = []
            for word in sentence:
                s.append(word["lemma"])
                s_tag.append(word["upos"])
            sentences.append(s)
            sentence_tags.append(s_tag)

    for fd in fds:
        fd.close()

    return sentences, sentence_tags


train_sentences, train_tags = corpora2sentences_and_tags([training_file, dev_file])
test_sentences, test_tags = corpora2sentences_and_tags([test_file])

words = set()
tags = set()

for s in train_sentences:
    for w in s:
        words.add(w)

for ts in train_tags:
    for t in ts:
        tags.add(t)

word2index = {w: i + 2 for i, w in enumerate(list(words))}
word2index["-PAD-"] = 0  # The special value used for padding
word2index["-OOV-"] = 1  # The special value used for OOVs

tag2index = {t: i + 1 for i, t in enumerate(list(tags))}
tag2index["-PAD-"] = 0  # The special value used to padding

tags_complete_list = ["-PAD-"] + list(tags)

train_sentences_X = []
test_sentences_X = []
train_tags_y = []
test_tags_y = []

for s in train_sentences:
    s_int = []
    for w in s:
        try:
            s_int.append(word2index[w.lower()])
        except KeyError:
            s_int.append(word2index["-OOV-"])

    train_sentences_X.append(s_int)

for s in test_sentences:
    s_int = []
    for w in s:
        try:
            s_int.append(word2index[w.lower()])
        except KeyError:
            s_int.append(word2index["-OOV-"])

    test_sentences_X.append(s_int)

for s in train_tags:
    train_tags_y.append([tag2index[t] for t in s])

for s in test_tags:
    test_tags_y.append([tag2index[t] for t in s])
print(train_sentences[0])
print(train_tags[0])
print(train_sentences_X[0])
print(train_tags_y[0])
print()
print(test_sentences[0])
print(test_tags[0])
print(test_sentences_X[0])
print(test_tags_y[0])

MAX_LENGTH = len(max(train_sentences_X, key=len))
print(MAX_LENGTH)

from keras.preprocessing.sequence import pad_sequences

train_sentences_X = pad_sequences(train_sentences_X, maxlen=MAX_LENGTH, padding="post")
test_sentences_X = pad_sequences(test_sentences_X, maxlen=MAX_LENGTH, padding="post")
train_tags_y = pad_sequences(train_tags_y, maxlen=MAX_LENGTH, padding="post")
test_tags_y = pad_sequences(test_tags_y, maxlen=MAX_LENGTH, padding="post")

print(train_sentences_X[0])
print(test_sentences_X[0])
print(train_tags_y[0])
print(test_tags_y[0])


from keras.models import Sequential
from keras.layers import (
    Dense,
    LSTM,
    InputLayer,
    Bidirectional,
    GRU,
    TimeDistributed,
    Embedding,
    Activation,
)
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
from keras import backend as K


model = Sequential()
model.add(InputLayer(input_shape=(MAX_LENGTH,)))
model.add(Embedding(len(word2index), 128))
if lstm:
    model.add(LSTM(256, return_sequences=True))
else:
    model.add(GRU(256, return_sequences=True))
model.add(TimeDistributed(Dense(len(tag2index))))
model.add(Activation("softmax"))

def ignore_class_accuracy(to_ignore=0):
    def ignore_accuracy(y_true, y_pred):
        y_true_class = K.argmax(y_true, axis=-1)
        y_pred_class = K.argmax(y_pred, axis=-1)

        ignore_mask = K.cast(K.not_equal(y_pred_class, to_ignore), "int32")
        matches = K.cast(K.equal(y_true_class, y_pred_class), "int32") * ignore_mask
        accuracy = K.sum(matches) / K.maximum(K.sum(ignore_mask), 1)
        return accuracy

    return ignore_accuracy

model.compile(
    loss="categorical_crossentropy",
    optimizer=Adam(adam),
    metrics=["accuracy", ignore_class_accuracy(0)],
)

model.summary()

import numpy as np
def to_categorical(sequences, categories):
    cat_sequences = []
    for s in sequences:
        cats = []
        for item in s:
            cats.append(np.zeros(categories))
            cats[-1][item] = 1.0
        cat_sequences.append(cats)
    return np.array(cat_sequences)

es = EarlyStopping(monitor='val_ignore_accuracy', verbose=1, patience=3)
mc = ModelCheckpoint('best_model.h5', monitor='val_ignore_accuracy', mode='max', verbose=1, save_best_only=True)

history = model.fit(
    train_sentences_X,
    to_categorical(train_tags_y, len(tag2index)),
    batch_size=batch_size,
    epochs=50,
    validation_split=0.2,
    callbacks=[es, mc]
)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label="train")
plt.plot(history.history['val_loss'], label="validation")
plt.legend()
plt.show()

scores = model.evaluate(test_sentences_X, to_categorical(test_tags_y, len(tag2index)))
print(f"{model.metrics_names[1]}: {scores[1] * 100}")


test_samples_X = []
for s in test_sentences:
    s_int = []
    for w in s:
        try:
            s_int.append(word2index[w.lower()])
        except KeyError:
            s_int.append(word2index['-OOV-'])
    test_samples_X.append(s_int)
 
test_samples_X = pad_sequences(test_samples_X, maxlen=MAX_LENGTH, padding='post')
predictions = model.predict(test_samples_X)

print(predictions)
print(predictions.shape)

def logits_to_tokens(sequences, index):
    token_sequences = []
    for categorical_sequence in sequences:
        token_sequence = []
        for categorical in categorical_sequence:
            token_sequence.append(index[np.argmax(categorical)])
 
        token_sequences.append(token_sequence)
 
    return token_sequences

index2tag = {i: t for t, i in tag2index.items()}
predicted_tags = logits_to_tokens(predictions, index2tag)

total_tags = 0
correct_tags = 0
total_sentences = 0
correct_sentences = 0
num_tags = len(tag2index)
confusion_matrix = np.zeros(shape=(num_tags, num_tags), dtype=np.double)
corrects = []

for sent, sent_t_p, tags in zip(test_sentences, predicted_tags, test_tags):

    correct_tag_per_sentence = 0
    for w, t_p, t in zip(sent, sent_t_p, tags):
        total_tags += 1
        if t_p == t:
            correct_tag_per_sentence += 1

        confusion_matrix[tag2index[t], tag2index[t_p]] += 1

    if correct_tag_per_sentence == len(sent):
        correct_sentences += 1
        corrects.append(sent)

    correct_tags += correct_tag_per_sentence
    total_sentences += 1


for row in confusion_matrix:
    s = sum(row)
    if s != 0:
        row /= s

print("< Finish evaluation")
print()

print("Total tags:", total_tags)
print("Correct tags:", correct_tags)
print(f"Token-accuracy: {correct_tags*100/total_tags}%")
print()

print("Total sentences:", total_sentences)
print("Correct sentences:", correct_sentences)
print(f"Sentence-accuracy: {correct_sentences*100/total_sentences}%")

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
cm = pd.DataFrame(data=confusion_matrix, index=tags_complete_list, columns=tags_complete_list)
plt.figure(figsize=(10,5))
sn.heatmap(cm, annot=True, fmt=".2f")
plt.show()