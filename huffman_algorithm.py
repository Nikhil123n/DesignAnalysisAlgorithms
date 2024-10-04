import math
import time
import numpy
import random
import heapq
import matplotlib.pyplot as plt

# Defining structure of Huffman Tree
class huffman_node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    
    # For priority queue to compare two frequencies of node
    def __lt__(self, next):
        return self.freq < next.freq
    
    def __repr__(self):
        return f"HuffmanTree(freq={self.freq}, symbol={self.symbol})"

# Huffman algorithm code
def huffman_algorithm(symbols_and_freq):
    # Step 1: Creating a priority queue using(min-heap)
    heapQueue = [huffman_node(freq, symbol) for symbol, freq in symbols_and_freq.items()]
    heapq.heapify(heapQueue)    

    # Step 2: Building the Huffman Tree
    while len(heapQueue) > 1:
        left = heapq.heappop(heapQueue)
        right = heapq.heappop(heapQueue)
        merged = huffman_node(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heapQueue, merged)

    # The remaining node is the root of the Huffman Tree
    root = heapq.heappop(heapQueue)
    
    # Step 3: Generate the Huffman Code in 0 & 1    
    def generate_codes(node, prefix=""):
        if node.symbol is not None:  
            return {node.symbol: prefix}
        codes = {}
        if node.left:
            codes.update(generate_codes(node.left, prefix + "0"))
        if node.right:
            codes.update(generate_codes(node.right, prefix + "1"))
        return codes
    
    return generate_codes(root)

# _____________________________________________________________________________________________________________________
# Theoretical time complexity O(n * log n)
def theoretical_time(n): 
    return (n * math.log2(n))

def generate_random_symbols_and_frequencies(n):
    symbols = [chr(i + 65) for i in range(n)]
    symbols_and_freq = {symbol: random.randint(1, 1000) for symbol in symbols}    
    return symbols_and_freq

# _____________________________________________________________________________________________________________________
theor_time = []
expt_time = []
n_Range = [10, 50, 100, 200, 500, 1000]

for n in n_Range:
    symbols_and_freq = generate_random_symbols_and_frequencies(n)    

    # Execute the Huffman coding algorithm
    startTime = time.perf_counter_ns()
    huffman_dict = huffman_algorithm(symbols_and_freq)
    endTime = time.perf_counter_ns()

    theor_time.append(theoretical_time(n))
    expt_time.append(endTime - startTime)


print(theor_time, expt_time)

# Scaling the theoretical values
theoretical_avg, experimental_avg = numpy.average(theor_time), numpy.average(expt_time)
scale_factor = experimental_avg / theoretical_avg  # Scale theoretical to match experimental times
for i in range(len(theor_time)):
    theor_time[i] *= scale_factor

print(theor_time)
print(expt_time)

# _____________________________________________________________________________________________________________________
# Plotting
plt.figure(figsize=(12, 6))

# Plotting theoretical times
plt.plot(n_Range, theor_time, label="Theoretical Time (O(n * log n))", marker='o')

# Plotting experimental times
plt.plot(n_Range, expt_time, label="Experimental Time", marker='x')

plt.ticklabel_format(style='plain')

plt.xlabel("Number of Symbols (n)")
plt.ylabel("Time Complexity (in ns)")
plt.legend()

# Show the plot
plt.show()
