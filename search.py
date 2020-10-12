# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        state, stepCost), where 'successor' is a successor to the current
        state, 'state' is the state required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfstates(self, states):
        """
         states: A list of states to take

        This method returns the total cost of a particular sequence of states.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of states that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # Checks if the starting point is the target point
    if problem.isGoalState(problem.getStartState()):
        return []

    nodeStack = util.Stack()
    origin = problem.getStartState()
    visited = []

    originInfo = (origin, [])
    nodeStack.push(originInfo)

    while not nodeStack.isEmpty():
        currentNode, states = nodeStack.pop()  # Receiving each node's info to be checked
        if currentNode not in visited:  # Appends the already visited nodes so they can be skipped in the
            visited.append(currentNode)  # next iteration

            # Returns the final directions list when it reaches the target point
            if problem.isGoalState(currentNode):
                return states

            for nextNode, state, cost in problem.getSuccessors(currentNode):
                nextState = states + [state]  # Creating the decisions list by appending the current state
                nextDecisionInfo = (nextNode, nextState)  # The new step tuple
                # print(" Next state could be ", nextNode, " with action ", state, " and cost ", cost)
                nodeStack.push(nextDecisionInfo)  # Pushing the adjacent nodes to the stack

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    node = problem.getStartState()
    if problem.isGoalState(node):
        return []
    frontier = util.Queue()
    node_tuple = (node, [])  # tuple with current state and its path from initial node to it
    frontier.push(node_tuple)
    explored = {node}

    while not frontier.isEmpty():
        node, parent_path = frontier.pop()  # the shallowest node in frontier and its path from starting node to it

        for child in problem.getSuccessors(node):
            if child[0] not in explored:
                explored.add(child[0])  # mark child node as visited if it's not visited
                if problem.isGoalState(child[0]):  # checking if child node is the goal node
                    return parent_path + [child[1]]
                child_tuple = (child[0], parent_path + [child[1]])  # update the child's path from initial node to it
                frontier.push(child_tuple)
    # error

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    if problem.isGoalState(problem.getStartState()):
        return []

    nodesPriorityQueue = util.PriorityQueue()
    origin = problem.getStartState()
    visited = []

    originInfo = (origin, [], 0)                # Setting the initial cost to 0
    nodesPriorityQueue.push(originInfo, 0)      # The start point has priority 0

    while not nodesPriorityQueue.isEmpty():
        currentNode, states, currentCost = nodesPriorityQueue.pop()  # Receiving each node's info to be checked
        if currentNode not in visited:  # Appends the already visited nodes so they can be skipped in the
            visited.append(currentNode)  # next iteration

            # Returns the final directions list when it reaches the target point
            if problem.isGoalState(currentNode):
                return states

            for nextNode, state, cost in problem.getSuccessors(currentNode):
                priority = currentCost + cost   # Updating each node's priority based on its cost
                nextState = states + [state]  # Creating the decisions list by appending the current state
                nextDecisionInfo = (nextNode, nextState, priority)  # The new step tuple
                # print(" Next state could be ", nextNode, " with action ", state, " and cost ", cost)
                nodesPriorityQueue.push(nextDecisionInfo, priority)  # Pushing the adjacent nodes to the stack

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
