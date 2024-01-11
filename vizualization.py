#visualisation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
import pandas as pd
class SequenceVisualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer
    def compare_with_fibonacci(self, n):
        fib_seq = self.analyzer.generate_fibonacci()
        collatz_seq = self.analyzer.generate_collatz(n)

        plt.figure(figsize=(10, 6))
        plt.plot(collatz_seq, label='Collatz Sequence')
        plt.plot(fib_seq, label='Fibonacci Sequence')
        plt.title(f'Comparison of Collatz and Fibonacci Sequences for n={n}')
        plt.xlabel('Step')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    def create_standard_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for counter in range(1, self.max_value + 1):
            sequence = self.calculate_sequence(counter)
            xs, zs = zip(*sequence)
            ys = [counter] * len(xs)

            ax.plot(xs, ys, zs)  # Add color coding or other customizations here

        ax.set_xlabel('Step')
        ax.set_ylabel('Starting Number')
        ax.set_zlabel('Value')
        ax.set_title('3D Collatz Sequences for Numbers 1 to ' + str(self.max_value))

        plt.show()

    def plot_surface(self, max_value, max_steps):
        self.max_value = max_value
        self.max_steps = max_steps
        data = self.analyzer.generate_data()  # Assuming generate_data is a method in analyzer
        X, Y = np.meshgrid(range(self.max_steps), range(1, self.max_value + 1))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, data, cmap='viridis')
        ax.set_xlabel('Step')
        ax.set_ylabel('Starting Number')
        ax.set_zlabel('Value')
        ax.set_title('3D Surface Plot of Collatz Sequences')
        plt.show()

    def save_animation(self, max_value, filename, fps=10, dpi=300):
        # Prepare figure for saving the animation
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('Step')
        self.ax.set_ylabel('Starting Number')
        self.ax.set_zlabel('Value')

        # Update function for animation
        def update(frame):
            self.ax.clear()
            self.ax.set_title('3D Collatz Sequences for Numbers 1 to ' + str(max_value))
            self.ax.set_xlabel('Step')
            self.ax.set_ylabel('Starting Number')
            self.ax.set_zlabel('Value')
            counter = frame + 1
            sequence = self.calculate_sequence(counter)
            xs, zs = zip(*sequence)
            ys = [counter] * len(xs)
            self.ax.plot(xs, ys, zs, color=plt.cm.viridis(len(sequence) / 100))

        # Create animation
        anim = FuncAnimation(self.fig, update, frames=range(max_value), repeat=False)

        # Save animation
        anim.save(filename, fps=fps, dpi=dpi)
    def plot_surface(self):
        self.generate_data()
        X, Y = np.meshgrid(range(self.max_steps), range(1, self.max_value + 1))
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, self.data, cmap='viridis')
        ax.set_xlabel('Step')
        ax.set_ylabel('Starting Number')
        ax.set_zlabel('Value')
        ax.set_title('3D Surface Plot of Collatz Sequences')
        plt.show()
