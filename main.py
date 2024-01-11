import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import ipywidgets as widgets
import pandas as pd
import sequence_analyzer
import statical_analyse
import vizualization
import dataExporter
from sequence_analyzer import SequenceComparison
from vizualization import SequenceVisualizer
from statical_analyse import StatisticalAnalyzer
from dataExporter import DataExporter

def main():
    # Define maximum length for sequences
    max_length = 100

    # Create an instance of SequenceAnalyzer
    analyzer = SequenceComparison(max_length)

    # Create instances of other modules, passing the analyzer instance
    visualizer = SequenceVisualizer(analyzer)
    statistical_analyzer = StatisticalAnalyzer(analyzer)
    data_exporter = DataExporter(analyzer)

    # Example usage of the classes

    # Generate and visualize sequences
    visualizer.compare_with_fibonacci(50)
    visualizer.plot_sequences(50) # if you have this method
    # ... other visualization methods

    # Perform statistical analysis
    statistical_analyzer.perform_statistical_analysis(15, 1, 2, 1, 1.5)

    # Export data
    data_exporter.export_to_csv('sequence_data.csv', 'collatz', 15)
    # ... other data exporting methods

if __name__ == "__main__":
    main()
