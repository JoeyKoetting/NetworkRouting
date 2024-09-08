#########################################
# class Priority Heap
# Inserts Item into Priority Queue
#
# Time Complexity Heap: O(log(n)) most complex method traverses through a binary tree
# Space Complexity Heap: O(n) stores all the priorities
#########################################


class Element:
    def __init__(self, index, priority):
        self.index = index
        self.priority = priority


class PriorityQueueHeap:

    #########################################
    # def make queue
    # init variables
    #
    # Time Complexity: Not Really Applicable
    # Space Complexity: O(1) stores some variables
    #########################################
    def __init__(self, srcIndex):
        self.priorities = []
        self.size = 0
        self.dictionary = {}
        self.insert(srcIndex, 0)

    #########################################
    # def insert
    # Inserts Item into Priority Queue
    #
    # Time Complexity: O(log(n)) calls bubble_up which is O(log(n))
    # However the insert method does not add on significant complexity
    # Space Complexity: O(1) Creates temp variables and stores things.
    # also appends an item to the heap
    #########################################
    def insert(self, index, priority):

        # if index already exists in tree
        if index in self.dictionary:
            # if visited return
            if self.dictionary[index] is None:
                return
            # not visited bubble_up
            else:
                self.bubble_up(self.dictionary[index])
                return

        # create new node in tree
        self.priorities.append(Element(index, priority))
        self.size = self.size + 1
        self.dictionary[index] = self.size

        # reorder tree
        self.bubble_up(len(self.priorities))

    #########################################
    # def bubble_up
    # Inserts Item into Priority Queue
    #
    # Time Complexity: O(log(n))  recursively traverses a binary tree
    # for a worst case of to a leaf node to a root node
    # Space Complexity: O(1) Creates some temporary variables
    #########################################
    def bubble_up(self, child_loc):

        # if the child_loc is not the root
        if child_loc > 1:

            # get the parent_loc
            if child_loc % 2 == 0:
                parent_loc = child_loc // 2
            else:
                parent_loc = (child_loc - 1) // 2

            # get priorities
            child_priority = self.priorities[child_loc - 1].priority
            parent_priority = self.priorities[parent_loc - 1].priority

            # if child priority is less than parents
            if child_priority < parent_priority:

                # swap everything
                child_index = self.priorities[child_loc - 1].index
                parent_index = self.priorities[parent_loc - 1].index

                self.dictionary[child_index] = parent_loc
                self.dictionary[parent_index] = child_loc

                self.priorities[child_loc - 1], self.priorities[parent_loc - 1] = \
                    self.priorities[parent_loc - 1],  self.priorities[child_loc - 1]

                # keep recursing until we get to the root
                self.bubble_up(parent_loc)
            else:
                # tree is good
                return

    #########################################
    # def decrease_key
    # Decreases the Key
    #
    # Time Complexity:  O(log(n)) calls insert, which calls bubble_up
    # which is O(log(n))
    # Space Complexity: 0(1) All functions this calls has 0(1) space complexity
    #########################################
    def decrease_key(self, index, priority):
        self.insert(index, priority)

    #########################################
    # def delete_min
    # Finds Deletes and returns Node with smallest edge
    #
    # Time Complexity: O(log(n)) calls bubble_down which is O(log(n))
    # Space Complexity: O(1) stores some variables
    #########################################
    def delete_min(self):

        if len(self.priorities) == 0:
            return None

        # get min value
        min = self.priorities[0].index
        self.dictionary[min] = None

        # pop last element of array
        tmp = self.priorities.pop()
        self.size = self.size - 1

        # reset location of last node in tree to first
        if self.size != 0:
            self.dictionary[tmp.index] = 1
            self.priorities[0] = tmp
            self.bubble_down(1)

        return min

    #########################################
    # def bubble_down
    # Inserts Item into Priority Queue
    #
    # Time Complexity: O(log(n)) recursively traverses a binary tree
    # for a worst case of to a root node to a leaf node
    # Space Complexity: O(1) O(n) creates some variables
    #########################################
    def bubble_down(self, parent_loc):

        # if child is left node
        if parent_loc * 2 == self.size:
            child_loc = parent_loc * 2

        # if there are two children
        elif parent_loc * 2 + 1 <= self.size:

            left_child_loc = parent_loc * 2
            right_child_loc = parent_loc * 2 + 1

            left_child_priority = self.priorities[left_child_loc - 1].priority
            right_child_priority = self.priorities[right_child_loc - 1].priority

            # Keep child with smallest priority
            if left_child_priority < right_child_priority:
                child_loc = left_child_loc
            else:
                child_loc = right_child_loc

        # no children
        else:
            return

        # get priorities
        child_priority = self.priorities[child_loc - 1].priority
        parent_priority = self.priorities[parent_loc - 1].priority

        # if child priority is less than parent
        if child_priority < parent_priority:

            # get the indexes
            child_index = self.priorities[child_loc - 1].index
            parent_index = self.priorities[parent_loc - 1].index

            # swap everything
            self.dictionary[child_index] = parent_loc
            self.dictionary[parent_index] = child_loc

            self.priorities[child_loc - 1], self.priorities[parent_loc - 1] = \
                self.priorities[parent_loc - 1], self.priorities[child_loc - 1]

            # recurse down the tree until tree is sorted
            self.bubble_down(child_loc)

        return
