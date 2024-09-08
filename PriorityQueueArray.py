#########################################
# class Priority Queue Array
# Inserts Item into Priority Queue
#
# Time Complexity Array: O(n) most complex method loops through an array
# Space Complexity Array: O(n) stores all the priorities
#########################################


class PriorityQueueArray:

    #########################################
    # def make queue
    # Init a list of priorities
    #
    # Time Complexity: O(n)  Creates a list with n elements
    # Space Complexity: O(n) The list has to have n elements in it
    #########################################
    def __init__(self, n, srcIndex):
        self.priorities = []

        for i in range(0, n):
            self.priorities.append(float('inf'))

        self.decrease_key(srcIndex, 0)

    #########################################
    # def insert
    # Does Nothing
    #
    # Time Complexity: Not Really Applicable
    # Space Complexity: Not Really Applicable
    #########################################
    @staticmethod
    def insert():
        pass

    #########################################
    # def decrease_key
    # Decreases the Key
    #
    # Time Complexity: 0(1)
    # Space Complexity: Not Really Applicable
    #########################################
    def decrease_key(self, index, priority):
        self.priorities[index] = priority

    #########################################
    # def delete_min
    # Finds Deletes and returns Node with smallest edge
    #
    # Time Complexity: O(n)  Loops through the array
    # Space Complexity: O(1) stores some temporary variables
    #########################################
    def delete_min(self):
        smallest_index = None
        smallest = None

        # loop through priorities and get the index of the smallest priority
        for i in range(0, len(self.priorities)):
            if self.priorities[i] is not None and \
                    (smallest is None or smallest > self.priorities[i]):
                smallest = self.priorities[i]
                smallest_index = i

        # if no smallest priority exists return None
        if smallest_index is None:
            return None

        # return smallest priority and mark it as visited
        self.priorities[smallest_index] = None
        return smallest_index

