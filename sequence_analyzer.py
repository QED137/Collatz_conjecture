import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
import pandas as pd
class SequenceComparison:
    def __init__(self, max_length):
        self.max_length = max_length

    def generate_collatz(self, start):
        sequence = [start]
        while start != 1 and len(sequence) < self.max_length:
            start = start // 2 if start % 2 == 0 else 3 * start + 1
            sequence.append(start)
        return sequence[:self.max_length]

    def generate_arithmetic(self, start, difference):
        return [start + i * difference for i in range(self.max_length)]

    def generate_geometric(self, start, ratio):
        return [start * (ratio ** i) for i in range(self.max_length)]

    def generate_fibonacci(self):
        sequence = [0, 1]
        while len(sequence) < self.max_length:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:self.max_length]

