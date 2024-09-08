#!/usr/bin/python3


from CS312Graph import *
from PriorityQueueArray import *
from PriorityQueueHeap import *
import time


class Distance:
    def __init__(self):
        self.fromNode = None
        self.distance = float('inf')


class NetworkRoutingSolver:
    def __init__( self, display ):
        self.distances = None

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network


    #########################################
    # def getShortestPath
    # Returns the shortest path from source node to destination
    #
    # Time Complexity: O(n) Path could be across all nodes in the graph
    # Space Complexity: O(n) If the Path could be across all nodes in the graph,
    # I would have to store edges from each node
    #########################################
    def getShortestPath(self, destIndex ):

        # init variables
        path_edges = []

        # finite variable
        total_distance = self.distances[destIndex].distance

        # Temporary variables for loop
        tmp_distance = self.distances[destIndex]
        edge_distance = total_distance
        tmp_location = self.network.nodes[destIndex].loc

        while tmp_distance.fromNode is not None:

            # get the previous node
            edge = self.network.nodes[tmp_distance.fromNode]

            # get distance info for the node
            tmp_distance = self.distances[tmp_distance.fromNode]

            # append new edge to array with info
            path_edges.append((edge.loc, tmp_location, '{:.0f}'.format(edge_distance - tmp_distance.distance)))

            # prepare distance for next distance calculation
            edge_distance = edge_distance - (edge_distance - tmp_distance.distance)

            # retain the location for next calculation
            tmp_location = edge.loc

        return {'cost': total_distance, 'path': path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False):
        self.source = srcIndex

        t1 = time.time()

        self.dijkstras(srcIndex, use_heap)

        t2 = time.time()

        return t2-t1


    #########################################
    # def dijkstras
    # Performs BFS search on the graph
    #
    # DIJKSRAS TOTAL WITH ARRAY
    # Time Complexity: O(n^2) loops through each vertices then, for each
    # vertices loop through all priorities
    # Space Complexity: O(n) stores all the priorities and distance
    #
    # DIJKSRAS TOTAL WITH HEAP
    # Time Complexity: O(n * log(n)) Loops through each vertices then,
    # for each vertices traverse through a binary tree
    # Space Complexity: O(n) stores all the priorities and distances
    #
    # DIJKSRAS BY ITSELF
    # Time Complexity: O(n) loops through entire array of vertices
    # Space Complexity: 0(n) stores all the distances
    #
    # ARRAY BY ITSELF
    # Time Complexity Array: O(n) most complex method loops through an array
    # Space Complexity Array: O(n) stores all the priorities
    #
    # HEAP BY ITSELF
    # Time Complexity Heap: O(log(n)) most complex method traverses through a binary tree
    # Space Complexity Heap: O(n) stores all the priorities
    #########################################
    def dijkstras(self, srcIndex, use_heap):

        # init variables
        nodes = self.network.nodes
        distances = []

        # Set Distance for all nodes to Infinity
        for i in range(0, len(nodes)):
            distances.append(Distance())

        # Set Initial Node Distance to Zero
        distances[srcIndex].distance = 0

        # make queue
        if use_heap:
            priorityQueue = PriorityQueueHeap(srcIndex)
        else:
            priorityQueue = PriorityQueueArray(len(nodes), srcIndex)

        min_index = priorityQueue.delete_min()

        while min_index is not None:

            # get min node and delete
            node = nodes[min_index]

            for i in range(0, len(node.neighbors)):
                if distances[node.neighbors[i].dest.node_id].distance > \
                        distances[node.node_id].distance + node.neighbors[i].length:

                    distances[node.neighbors[i].dest.node_id].distance = \
                        distances[node.node_id].distance + node.neighbors[i].length
                    distances[node.neighbors[i].dest.node_id].fromNode = node.node_id
                    priorityQueue.decrease_key(node.neighbors[i].dest.node_id,
                                               distances[node.node_id].distance + node.neighbors[i].length)

            min_index = priorityQueue.delete_min()

        self.distances = distances
