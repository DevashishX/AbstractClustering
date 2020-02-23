import numpy as np




def gen_mean(vals, p = 3):
    p = float(p)
    return np.power(
        np.mean(
            np.power(
                np.array(vals, dtype=complex),
                p),
            axis=0),
        1 / p
    )

def get_pmeans(wordembeddings):
    pmean_embedding = []
    pmean_embedding.append(gen_mean(wordembeddings,1))
    pmean_embedding.append(gen_mean(wordembeddings,2))
    pmean_embedding.append(gen_mean(wordembeddings,3))
    pmean_embedding.append(gen_mean(wordembeddings,4))
    pmean_embedding.append(gen_mean(wordembeddings,5))

    return np.concatenate(pmean_embedding, axis=0)
