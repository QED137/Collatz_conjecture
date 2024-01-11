# Collatz Conjecture Analysis Project

This project is an exploration of the intriguing Collatz Conjecture, a problem in mathematics that, despite its simple formulation, remains unsolved. The project includes a suite of Python tools for generating, visualizing, analyzing, and exporting sequences related to the conjecture.




## What is the Collatz Conjecture?
The Collatz Conjecture asserts that no matter which positive integer you start with, this sequence will always eventually reach 1. Once it reaches 1, the sequence will repeat the cycle 4, 2, 1 indefinitely.
$$
f(n) = 
\begin{cases} 
    \frac{n}{2}, & \text{if } n \text{ is even} \\
    3n + 1, & \text{if } n \text{ is odd}
\end{cases}
$$


The Collatz Conjecture, also known as the "3x+1 problem", is a hypothesis in mathematics that concerns sequences formed by the following process:

1. Start with any positive integer `n`.
2. If `n` is even, divide it by 2.
3. If `n` is odd, multiply it by 3 and add 1.
4. Continue this process with each new value of `n`.

The conjecture asserts that no matter which positive integer you start with, this process will always reach 1.

# Why It's Interesting:
What makes the Collatz Conjecture particularly intriguing is its simplicity and accessibility. The rules are straightforward enough for anyone to understand and try, yet the underlying behavior of the sequence it produces is complex and unpredictable. It exhibits chaotic and seemingly random behavior, yet mathematicians suspect that there's an underlying pattern or proof that could explain why all paths lead to 1.
## Historical Background:
The conjecture was first posed by Lothar Collatz, a German mathematician, in 1937. Since then, it has been tested on a wide range of numbers, and no counterexamples have been found - all tested sequences indeed eventually arrive at 1.

## Mathematical Significance:
The allure of the Collatz Conjecture lies in its resistance to a wide range of mathematical techniques. It's a problem that sits at the crossroads of number theory and dynamical systems and challenges our understanding of both.

## Current State:
As of now, the conjecture has neither been proved nor disproved. It remains an active area of research, attracting both professional mathematicians and amateur enthusiasts alike. The problem is a testament to the fact that some of the most straightforward questions in mathematics can also be the most profound and challenging.

The Collatz Conjecture is a perfect example of how a simple algorithm can lead to a complex and beautiful mathematical journey, making it a favorite topic among many in the field of mathematics and beyond.
## Features

- **Sequence Generation**: Generate various sequences including Collatz, Fibonacci, arithmetic, and geometric sequences.
- **Data Visualization**: Visualize these sequences using different plot types, including standard plots and 3D visualizations.
- **Statistical Analysis**: Perform and output statistical analysis on the generated sequences.
- **Data Exporting**: Export the sequences and analyses to CSV and Excel formats.

## Getting Started

To run the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/QED137/Collatz_conjecture.git