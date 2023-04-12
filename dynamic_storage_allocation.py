"""
Author: Tyler J. Burgee
Date: 12 April 2023
Course: CIS 390 - Operating Systems
"""

# IMPORT MODULES
from random import randrange

class DynamicStorageAllocator:
    """
    Class to define a DynamicStorageAllocator object

    Use : to allocate memory to processes.

    Attributes
    ----------
    size : int
        The total size of main memory
    partitions : int
        The number of sections into which main memory is split
    """

    def __init__(self, size: int, partitions: int) -> None:
        """Defines the constructor for a DynamicStorageAllocator object"""
        self.size = size
        self.partitions = partitions

        self.chunks = self._memory_setup_()
        self.holes = self.chunks

    def _memory_setup_(self) -> list:
        """Randomizes the size of each main memory partition"""
        chunks = [0]*self.partitions
        memory_remaining = self.size

        for x in range(len(chunks)-1):
            if memory_remaining > 1:
                chunks[x] = randrange(1, int(memory_remaining/2))
                memory_remaining -= chunks[x]

        chunks[len(chunks)-1] = memory_remaining

        return chunks

    def first_fit(self, processes: list) -> None:
        """Allocates memory to processes according to first-fit algorithm"""
        for process in processes:
            for x, hole in enumerate(self.holes):
                if process <= hole:
                    remainder = hole - process
                    print("Hole {} = {} - {} = {}".format(x, hole, process, remainder))
                    self.holes[x] = remainder
                    break

    def best_fit(self, processes: list) -> None:
        """Allocates memory to processes according to best-fit algorithm"""
        for process in processes:
            differences = [hole - process for hole in self.holes]
            for x, difference in enumerate(differences):
                try:
                    if difference is min([difference for difference in differences if difference >= 0]):
                        print("Hole {} = {} - {} = {}".format(x, self.holes[x], process, difference))
                        self.holes[x] = difference
                        break
                except ValueError:
                    break

    def worst_fit(self, processes: list) -> None:
        """Allocates memory to processes according to worst-fit algorithm"""
        for process in processes:
            differences = [hole - process for hole in self.holes]
            for x, difference in enumerate(differences):
                try:
                    if difference is max([difference for difference in differences if difference >= 0]):
                        print("Hole {} = {} - {} = {}".format(x, self.holes[x], process, difference))
                        self.holes[x] = difference
                        break
                except ValueError:
                    break
        
if __name__ == '__main__':
    # DEFINE THE AMOUNT OF MEMORY TO BE ALLOCATED TO PROCESSES
    processes = [308, 219, 143, 56, 274]

    # INSTANTIATE DynamicStorageAllocator OBJECT
    dsa = DynamicStorageAllocator(1000, 5)

    print("-"*20, "First Fit", "-"*20)
    print("Partition Chunks Before Allocation:", dsa.chunks)

    print("Processes to be Allocated:", processes)

    print("Allocating Memory to Processes...")
    dsa.first_fit(processes)
    print("Partition Chunks After Allocation:", dsa.holes)
    print("-"*50)

    print()

    # INSTANTIATE DynamicStorageAllocator OBJECT
    dsa = DynamicStorageAllocator(1000, 5)

    print("-"*20, "Best Fit", "-"*20)
    print("Partition Chunks Before Allocation:", dsa.chunks)

    print("Processes to be Allocated:", processes)

    print("Allocating Memory to Processes...")
    dsa.best_fit(processes)
    print("Partition Chunks After Allocation:", dsa.holes)
    print("-"*50)

    print()

    # INSTANTIATE DynamicStorageAllocator OBJECT
    dsa = DynamicStorageAllocator(1000, 5)

    print("-"*20, "Worst Fit", "-"*20)
    print("Partition Chunks Before Allocation:", dsa.chunks)

    print("Processes to be Allocated:", processes)

    print("Allocating Memory to Processes...")
    dsa.worst_fit(processes)
    print("Partition Chunks After Allocation:", dsa.holes)
    print("-"*50)
