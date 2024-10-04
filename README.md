# Huffman Encoding Algorithm
## Overview
This project implements the Huffman Encoding Algorithm, a widely used data compression technique that assigns variable-length codes to input characters based on their frequencies. The algorithm is used for lossless data compression, reducing the amount of space required to store or transmit data.

## How Huffman Encoding Works
Frequency Count: Each character is associated with its frequency of occurrence.
Min-Heap (Priority Queue): A binary tree is built using a min-heap where each node represents a symbol and its frequency.
Tree Construction: The two nodes with the lowest frequencies are merged to create a new internal node with their combined frequency. This process repeats until a single root node remains, representing the complete Huffman tree.
Code Assignment: A binary code is assigned to each character based on its position in the tree. Left branches correspond to 0 and right branches to 1, leading to shorter codes for more frequent characters.

## Time Complexity
The overall time complexity of the Huffman Algorithm is O(n log n), where n is the number of unique symbols. This complexity arises due to the heap operations involved in building the Huffman tree.

![Time Complexity Plot](./Figure_5.png)

