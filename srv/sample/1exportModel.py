from torch import nn
import ezkl

# simple model example by jseam senpai: https://t.co/ThNaMwrude

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.relu = nn.ReLU()
        self.d2 = nn.Linear(10,10)

    def forward(self, x):
        x = self.d2(x)
        return self.relu(x)


def main():
    circuit = MyModel()
    ezkl.export(circuit, input_shape = [10])    


if __name__ == "__main__":
    main()