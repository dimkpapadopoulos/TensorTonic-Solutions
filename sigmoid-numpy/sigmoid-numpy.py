import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if type(x)==float:
        s = 1 + np.exp(-x)
        return 1/s
    
    X = np.asarray(x, dtype=float)
    s = 1 + np.exp(-X)
    return 1/s
    