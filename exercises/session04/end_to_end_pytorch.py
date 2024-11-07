# Implement the end-to-end training pipeline using PyTorch

# 1. Load the data
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

x = torch.tensor(data:[1,2,3,4,5], device=device)

y = torch.tensor([1,2,3,4,5])
print(y.type())
y = y.to(device)
print(y.type())

torch.LongTensor


# 2. Define the model

import torch
from torch import nn

class ManualLinearRegressor(nn.Module):
    def __init__(self)
        super().__init__()
        self.w = nn.Parameter(torch.randn(()))
        self.b = nn.Parameter(torch.randn(()))

    def forward(self, x):
        return self.w * x + self.b
# 3. Define the loss function


# 4. Define the optimizer
# 5. Train the model
# 6. Make predictions

