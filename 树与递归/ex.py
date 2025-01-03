import torch
import torch.nn as nn
import numpy as np
class RMSNorm(torch.nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        #eps防止取倒数之后分母为0
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

list_a = np.array([[1.0,2.0,np.sqrt(7.0)],
                   [4.0,5.0,6.0]])
a = torch.tensor(np.array(list_a))
rms = RMSNorm(3)
print(rms.norm(a))