import numpy as np
import matplotlib.pyplot as plt

class StatisticalAnalyzer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def analyze_sequence(self, sequence):
        analysis = {
            'mean': np.mean(sequence),
            'median': np.median(sequence),
            'std_dev': np.std(sequence),
            'max': np.max(sequence),
            'min': np.min(sequence)
        }
        return analysis

    def perform_statistical_analysis(self, collatz_start, arith_start, arith_diff, geom_start, geom_ratio):
        collatz_seq = self.analyzer.generate_collatz(collatz_start)
        arith_seq = self.analyzer.generate_arithmetic(arith_start, arith_diff)
        geom_seq = self.analyzer.generate_geometric(geom_start, geom_ratio)
        fib_seq = self.analyzer.generate_fibonacci()

        # Perform analysis
        collatz_analysis = self.analyze_sequence(collatz_seq)
        arith_analysis = self.analyze_sequence(arith_seq)
        geom_analysis = self.analyze_sequence(geom_seq)
        fib_analysis = self.analyze_sequence(fib_seq)

        # Print analysis results
        print("Collatz Sequence Analysis:", collatz_analysis)
        print("Arithmetic Sequence Analysis:", arith_analysis)
        print("Geometric Sequence Analysis:", geom_analysis)
        print("Fibonacci Sequence Analysis:", fib_analysis)

    def compare_sequences(self, collatz_start, arith_start, arith_diff, geom_start, geom_ratio):
        collatz_seq = self.analyzer.generate_collatz(collatz_start)
        arith_seq = self.analyzer.generate_arithmetic(arith_start, arith_diff)
        geom_seq = self.analyzer.generate_geometric(geom_start, geom_ratio)
        fib_seq = self.analyzer.generate_fibonacci()

        plt.figure(figsize=(12, 6))
        plt.plot(collatz_seq, label='Collatz Sequence')
        plt.plot(arith_seq, label='Arithmetic Sequence')
        plt.plot(geom_seq, label='Geometric Sequence')
        plt.plot(fib_seq, label='Fibonacci Sequence')
        plt.xlabel('Step')
        plt.ylabel('Value')
        plt.title('Sequence Comparison for n=100')
        plt.legend()
        plt.show()
