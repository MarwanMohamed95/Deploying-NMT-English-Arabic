# **Neural Machine Translation (English to Arabic) Through API**

This tutorial demonstrates how to train a sequence-to-sequence (seq2seq) model for English to Arabic and Arabic to English translation using [Transformer](https://arxiv.org/abs/1706.03762).

We first trained classification model to detect the language of the input sentence then used the appropiate translation model to translate that sentence from English to Arabic or from Arabic to English.

Then we implemented Flask and streamlit API translate the input sentences using the trained model. 

![](https://github.com/MarwanMohamed95/English-Arabic-NMT/blob/master/test1.PNG?raw=true)

![](https://github.com/MarwanMohamed95/English-Arabic-NMT/blob/master/test2.PNG?raw=true)

### Transformer Overview:

The Transformer is a neural network architecture proposed in the paper "Attention is All You Need" by Vaswani et al. (2017). It has revolutionized the field of natural language processing (NLP) by replacing traditional recurrent neural network (RNN) based models, such as LSTMs, with a self-attention mechanism that can capture long-term dependencies in sequences more efficiently.

The architecture of the Transformer consists of two major components: the encoder and the decoder. The encoder takes an input sequence and produces a hidden representation, while the decoder takes the hidden representation and generates an output sequence. Both the encoder and decoder consist of multiple layers of self-attention and feedforward neural networks.

The self-attention mechanism is the key component of the Transformer. It allows the model to weigh the importance of different parts of the input sequence when generating the output sequence. The self-attention mechanism works by computing a set of attention scores between each pair of positions in the input sequence. These attention scores are used to weight the contributions of each position to the output at each position.

In addition to the self-attention mechanism, the Transformer also uses positional encodings to provide the model with information about the order of the input sequence. The positional encodings are added to the input embeddings before being fed into the model.

Overall, the Transformer has become the standard architecture for a wide range of NLP tasks, such as machine translation, text classification, and language generation, and has achieved state-of-the-art performance on many benchmarks.

![](https://github.com/MarwanMohamed95/Neural-Machine-Translation-with-Transformer/blob/main/transformer.png?raw=true)