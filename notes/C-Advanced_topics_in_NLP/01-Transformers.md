# Transformers

A transformer:
* Sequence to sequence system: [Je suis étudiant] → [I am a student].
* Structure: input [→ Encoder → Decoder] → Output.

An encoder:
* A NN: first layer x1, ..., xn → y1, ..., ym, *with m < n*.
* It is compression.

A decoder:
* Well... the opposite.

Unrolling:
* It is a stack of multiple encoders, and the final encoder is passed to all the decoders.
* Encoders do not share weights.

Encoder parts:
* Self attention →
* Feed forward neural network

Decoder:
* Self attention →
* Encoder-decoder attention → 
* Feed Forward

Self-attention:
* Relationship among words.

Queries, keys, values:
* Obtained by multiplying a matrix per an embedding.
* Learning a function: which words relate to other words.
* A score is computed with q*k.
* Normalization and apply softmax.
* Multiply the softmax score per the value.

Hyperparameters:
* Matrices W^Q, W^K, W^V.
* To avoid overfitting.

Attention heads:
* There are many attention mechanisms.
* Half the heads may not learn anything.
* The z's are concatenated.

Position encoding:
* Special set of weight added depending on the position.

Residuals:
* In order to dampen, average input and output, and then normalize.

Last step:
* Logits → softmax → pick the higher one.