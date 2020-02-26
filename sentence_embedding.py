import numpy as np

def gen_mean(vals, p = 3):
    p = float(p)
    return np.power(
        np.mean(
            np.power(
                np.array(vals, dtype=np.complex),
                p),
            axis=0),
        1 / p
    )

def get_pmeans(wordembeddings):
    """give wordembeddings"""
    pmean_embedding = []

    # ('max', (lambda word_embeddings: [np.max(word_embeddings, axis=0)], lambda embeddings_size: embeddings_size)),
    # ('min', (lambda word_embeddings: [np.min(word_embeddings, axis=0)], lambda embeddings_size: embeddings_size)),

    pmean_embedding.append(gen_mean(wordembeddings,1))
    pmean_embedding.append(np.max(wordembeddings,axis= 0))
    pmean_embedding.append(np.min(wordembeddings, axis= 0))
    # pmean_embedding.append(gen_mean(wordembeddings,0.5))
    pmean_embedding.append(gen_mean(wordembeddings,2))
    pmean_embedding.append(gen_mean(wordembeddings,3))

    # pmean_embedding.append(gen_mean(wordembeddings,4))
    # pmean_embedding.append(gen_mean(wordembeddings,5))

    return np.concatenate(pmean_embedding, axis=0)
