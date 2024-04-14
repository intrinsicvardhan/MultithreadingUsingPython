import time 
import threading 
from mat_mul import matrix_multiply
from print_table import print_table, print_graph
import random

k = 10
range_threads = 20
M = [[round(random.uniform(0, 1), 2) for _ in range(k)] for _ in range(k)]

result_table = [0.0 for _ in range(range_threads)]

def perform_mul(M, num_matrices=100):
    k = len(M)
    for num_threads in range(range_threads):
        threads = []
        start_time = time.time()
        for _ in range(num_matrices):
            random_matrices = [[[round(random.uniform(0, 1), 2) for _ in range(k)] for _ in range(k)] for _ in range(num_matrices)]

            for matrix in random_matrices:
                thread = threading.Thread(target=matrix_multiply, args=(M, matrix))
                threads.append(thread)
                thread.start()

            for thread in threads: 
                thread.join()

        end_time = time.time()
        result_table[num_threads-1] = end_time - start_time
    return result_table

def main():
    result_table = perform_mul(M, 100)
    print_table(result_table)
    print_graph(result_table, range_threads=range_threads)
    
main()
