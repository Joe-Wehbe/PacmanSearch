# Description
This project was completed as part of the Artificial Intelligence course at the <a href="lau.edu.lb">Lebanese American University</a>. It consists of implementing different search algorithms and heuristics to optimize the Pacman game.</br>

The algorithms and heuristics are written in the `search.py` and `searchAgents.py` files. <br>
Files that can be useful to look at: `pacman.py`, `game.py` and `util.py` (data structures).<br>
Other supporting files can be ignored. <br>

![Pacman](https://github.com/Joe-Wehbe/pacman-search/assets/102875229/7dc2f23b-3358-4bb7-8abf-71f96f2546fd)

# Getting Started
After downloading the code, changing the directory, and unzipping it, you can play a game by typing the following command on your terminal:
```
python pacman.py 
```
Test that the provided Search Agent is working correctly by running:
```
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```
All commands can be found in the `command.txt` file for easy copy-pasting. <br>
Keep in mind that if Pacman gets stuck you can exit the game by clicking `ctrl + c`

# Algorithms and Heuristics
### Q1: Finding Fixed Food Dot using Depth First Search
This algorithm is implemented in `search.py`.
To test it, you can run the following three commands, each one for a different maze: 
```
python pacman.py -l tinyMaze -p SearchAgent
```
```
python pacman.py -l mediumMaze -p SearchAgent
```
```
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### Q2: Breadth First Search
This algorithm is implemented in `search.py`. To test it, you can run the following two commands, each one for a different maze:
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
```
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

### Q3: Varying the Cost Function (Uniform Cost Search)
This algorithm is implemented in `search.py`.
To test it, you can run the following three commands, each one for a different maze: 
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
```
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
```
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

### Q4: A* search
This algorithm is implemented in `search.py`.
To test it, you can run the following command: 
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### Q5: Finding All the Corners
This problem consists of developing a code that uses BFS to find the shortest path through the maze that touches all four corners. The code for this problem is implemented in `searchAgents.py`.
To test the code, you can try the following two commands:
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

### Q6: Corners Problem: Heuristic
This problem consists of implementing a non-trivial, consistent heuristic for the corners problem using A* search. It is implemented in `searchAgents.py`.
To test it, you can run the following command:
```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

### Q7: Eating all the dots
This problem consists of developing a consistent heuristic to let Pacman eat all the dots in as few steps as possible using A* search. It is implemented in `searchAgents.py`.
To test it, you can run the following command:
```
python pacman.py -l testSearch -p AStarFoodSearchAgent
```

### Q8: Suboptimal Search
This problem consists of developing an agent that always greedily eats the closest dot. It is implemented in `searchAgents.py`.
To test it, you can run the following command:
```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```


