import numpy as np

def calculate(list):
    calculations: dict = {}
    # input check:
    # - raise ValueError if len(list) < 9
    #print(len(list))
    if (len(list) < 9):
        raise ValueError('List must contain nine numbers.')
    np_matrix = np.reshape(list, (3,3))

    # Calculate Mean
    calculations['mean'] = [ 
        np_matrix.mean(axis=0).tolist(),
        np_matrix.mean(axis=1).tolist(),
        np_matrix.mean()
    ]

    # Variance
    calculations['variance'] = [
        np_matrix.var(axis=0).tolist(),
        np_matrix.var(axis=1).tolist(),
        np_matrix.var()
    ]

    # StdDev
    calculations['standard deviation'] = [
        np_matrix.std(axis=0).tolist(),
        np_matrix.std(axis=1).tolist(),
        np_matrix.std()
    ]

    # Max
    calculations['max'] = [
        np_matrix.max(axis=0).tolist(),
        np_matrix.max(axis=1).tolist(),
        np_matrix.max()
    ]

    # Min
    calculations['min'] = [
        np_matrix.min(axis=0).tolist(),
        np_matrix.min(axis=1).tolist(),
        np_matrix.min()
    ]

    # Sum
    calculations['sum'] = [
        np_matrix.sum(axis=0).tolist(),
        np_matrix.sum(axis=1).tolist(),
        np_matrix.sum()
    ]

    return calculations

if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))
