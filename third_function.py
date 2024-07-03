def chebyshev_distance(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Les vecteurs doivent avoir la même longueur")
    
    max_diff = 0
    for v1, v2 in zip(vec1, vec2):
        diff = abs(v1 - v2)
        if diff > max_diff:
            max_diff = diff
    return max_diff
