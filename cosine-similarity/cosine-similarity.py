import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    n1 = np.linalg.norm(a)
    n2 = np.linalg.norm(b)
    
    return float(np.dot(a,b)/(n1*n2)) if n1 and n2 else 0.0
    