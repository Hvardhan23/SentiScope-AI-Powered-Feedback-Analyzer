import torch

def get_device():
    """
    Returns the appropriate device for PyTorch operations.
    If a GPU is available, it returns 'cuda', otherwise it returns 'cpu'.
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

get_device()
