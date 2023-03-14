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
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    root = problem.getStartState() # starting state of the search (first node)
    path = [] # path that Pacman traverses (to return)
    visited = [] # list that stores explored nodes
    stack = util.Stack() # stack that stores the nodes currently being visited and to visit

    stack.push((root, path)) # pushing the first node and the path list onto the stack

    while not stack.isEmpty(): # Running DFS until the stack is empty, or the goal state is reached
        current, path = stack.pop() # remove the node being visited from the stack, store it in current, and store the path in the "path" list

        if current not in visited: # if the current node is not yet visited
            visited.append(current) # mark it as visited and add it to the list of visited nodes

            if problem.isGoalState(current): # if the current node is the goal state
                return path # return the path to the goal

            for adjacent, added_path, cost in problem.getSuccessors(current): # check for all adjacent nodes of the current node
                if adjacent not in visited: # if adjacent nodes are not yet visited
                    new_path = path + [added_path] # update the path
                    stack.push((adjacent, new_path)) # push the nodes and the new path onto the stack
    return path

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    root = problem.getStartState() # starting state of the search (first node)
    path = [] # path that Pacman traverses (to return)
    visited = [] # list that stores explored nodes
    queue = util.Queue() # queue that stores the nodes currently being visited and to visit

    queue.push((root, path)) # pushing the first node and the path list into the queue

    while not queue.isEmpty(): # Running BFS until the queue is empty, or the goal state is reached
        current, path = queue.pop() # remove the node being visited from the queue, store it in current, and store the path in the "path" list

        if current not in visited: # if the current node is not yet visited
            visited.append(current) # mark it as visited and add it to the list of visited nodes

            if problem.isGoalState(current): # if the current node is the goal state
                return path # return the path to the goal

            for adjacent, added_path, cost in problem.getSuccessors(current): # check for all adjacent nodes of the current node
                if adjacent not in visited: # if adjacent nodes are not yet visited
                    new_path = path + [added_path] # update the path
                    queue.push((adjacent, new_path)) # push the nodes and the new path into the queue
    return path

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    root = problem.getStartState() # starting state of the search (first node)
    path = [] # path that Pacman traverses (to return)
    visited = [] # list that stores explored nodes
    pqueue = util.PriorityQueue() # priority queue that stores the nodes currently being visited and to visit

    pqueue.push((root, path), 0) # pushing the first node, the path list, and the priority into the priority queue

    while not pqueue.isEmpty(): # Running UCS until the priority queue is empty, or the goal state is reached
        current, path = pqueue.pop() # remove the node being visited from the priority queue, store it in current, and store the path in the "path" list

        if current not in visited: # if the current node is not yet visited
            visited.append(current) # mark it as visited and add it to the list of visited nodes

            if problem.isGoalState(current): # if the current node is the goal state
                return path # return the path to the goal

            for adjacent, added_path, cost in problem.getSuccessors(current): # check for all adjacent nodes of the current node
                if adjacent not in visited: # if adjacent nodes are not yet visited
                    new_path = path + [added_path] # update the path
                    new_cost = problem.getCostOfActions(new_path) # update the cost
                    pqueue.push((adjacent, new_path), new_cost) # push the nodes and the new path into the priority queue
    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    root = problem.getStartState() # starting state of the search (first node)
    path = [] # path that Pacman traverses (to return)
    visited = [] # list that stores explored nodes
    pqueue = util.PriorityQueue() # priority queue that stores the nodes currently being visited and to visit

    pqueue.push((root, path), heuristic(root, problem)) # pushing the first node, the path list, and the heuristic into the priority queue

    while not pqueue.isEmpty(): # Running A* until the priority queue is empty, or the goal state is reached
        current, path = pqueue.pop() # remove the node being visited from the priority queue, store it in current, and store the path in the "path" list

        if current not in visited: # if the current node is not yet visited
            visited.append(current) # mark it as visited and add it to the list of visited nodes

            if problem.isGoalState(current): # if the current node is the goal state
                return path # return the path to the goal

            for adjacent, added_path, cost in problem.getSuccessors(current): # check for all adjacent nodes of the current node
                if adjacent not in visited: # if adjacent nodes are not yet visited
                    new_path = path + [added_path] # update the path
                    new_cost = problem.getCostOfActions(new_path) # update the cost
                    new_heuristic = new_cost + heuristic(adjacent, problem) # update heuristic
                    pqueue.push((adjacent, new_path), new_heuristic) # push the adjacent nodes, the new path and the heuristic into the priority queue
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
