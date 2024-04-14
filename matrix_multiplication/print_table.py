from pretty_html_table import build_table
import matplotlib.pyplot as plt
import pandas as pd


def print_table(result_table):
    result_table = pd.DataFrame(result_table, columns=['Time taken (s)'])
    result_table.index = [f"Threads = {i+1}" for i in range(len(result_table))]
    html_table = build_table(result_table, 'blue_light', index=True)
    with open('result_table.html', 'w') as f:
        f.write(html_table)
    print('Table saved in result_table.html')
    return html_table


def print_graph(result_table, range_threads=8):
    df = pd.DataFrame(result_table[:range_threads])
    
    df.index = [f"{i+1} threads" for i in range(1, len(result_table)+1)]
    df.plot(kind='line', marker='o', figsize=(12, 6))
    
    plt.xlabel('Number of threads')
    plt.ylabel('Time taken (s)')
    plt.title('Time taken for matrix multiplication with different number of threads')
    
    plt.savefig('result_graph.png')
    print('Graph saved in result_graph.png')
    plt.show()
    
    return df