import pandas as pd

class DataExporter:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def export_to_csv(self, filename, sequence_type, *args):
        """
        Export the specified sequence data to a CSV file.
        sequence_type: Type of sequence to export ('collatz', 'arithmetic', 'geometric', 'fibonacci')
        args: Additional arguments needed for sequence generation (like start, difference, ratio)
        """
        data = []
        for i in range(1, self.analyzer.max_length + 1):
            if sequence_type == 'collatz':
                sequence = self.analyzer.generate_collatz(i)
            elif sequence_type == 'arithmetic':
                sequence = self.analyzer.generate_arithmetic(*args)
            elif sequence_type == 'geometric':
                sequence = self.analyzer.generate_geometric(*args)
            elif sequence_type == 'fibonacci':
                sequence = self.analyzer.generate_fibonacci()
            else:
                raise ValueError("Invalid sequence type")

            data.append(sequence)

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)

    def export_to_excel(self, filename, sequence_type, *args):
        """
        Export the specified sequence data to an Excel file.
        sequence_type: Type of sequence to export ('collatz', 'arithmetic', 'geometric', 'fibonacci')
        args: Additional arguments needed for sequence generation (like start, difference, ratio)
        """
        data = []
        for i in range(1, self.analyzer.max_length + 1):
            if sequence_type == 'collatz':
                sequence = self.analyzer.generate_collatz(i)
            elif sequence_type == 'arithmetic':
                sequence = self.analyzer.generate_arithmetic(*args)
            elif sequence_type == 'geometric':
                sequence = self.analyzer.generate_geometric(*args)
            elif sequence_type == 'fibonacci':
                sequence = self.analyzer.generate_fibonacci()
            else:
                raise ValueError("Invalid sequence type")

            data.append(sequence)

        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
