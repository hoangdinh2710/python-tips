# Run a function with different parameters (1 argument)
from multiprocessing import Pool, freeze_support 

def print_range(range): 
	# print range 
	print('From {} to {}:'.format(range[0], range[1]))
 
def run_parallel(): 
	# list of ranges 
	list_ranges = [[0, 10], [10, 20], [20, 30]] 
	# pool object with number of elements in the list 
	pool = Pool(processes=len(list_ranges)) 
	# map the function to the list and pass 
	# function and list_ranges as arguments 
	pool.map(print_range, list_ranges)

# Driver code 
if __name__ == '__main__': 
	run_parallel()

# Run a function with different parameters with more than 1 args
def print_range_args(arg1,arg2): 
	# print range 
	print(f'From {arg1} to {arg2}:') 

for x, y in [[1, 1], [2, 2]]:
    # Define a pool of workers with 2 processes
    pool = Pool(processes=2) 
	# For each worker use the argument x and y
    pool.apply_async(print_range_args, (x, y))

# Driver code 
if __name__ == '__main__': 
	run_parallel()

# Difference between map, apply,starmap
'''

Async methods submit all the processes at once and retrieve the results once they are finished. Use get method to obtain the results.

Pool.map(or Pool.apply) methods are very much similar to Python built-in map(or apply). They block the main process until all the processes complete and return the result.

                  | Multi-args   Concurrence    Blocking     Ordered-results
---------------------------------------------------------------------
Pool.map          | no           yes            yes          yes
Pool.map_async    | no           yes            no           yes
Pool.apply        | yes          no             yes          no
Pool.apply_async  | yes          yes            no           no
Pool.starmap      | yes          yes            yes          yes
Pool.starmap_async| yes          yes            no           no
'''

# When function query data from database, add free support to avoid error
# Driver code 
if __name__ == '__main__': 
    freeze_support() 
    run_parallel()