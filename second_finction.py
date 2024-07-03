import numpy as np

def chebyshev_distance(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    if vec1.shape != vec2.shape:
        raise ValueError("Les vecteurs doivent avoir la même longueur")
    
    return np.max(np.abs(vec1 - vec2))
