# Maze Solver





## Setup 
Do the following instructions:
1. Open command prompt, type 'git clone https://github.com/vip30service123/maze_solver.git' to clone the project
2. Type 'python install -r requirements.txt' to install related libraries
3. Type 'python main.py' to run the project

## Usage
### Example

When the app starts, it looks like this
<img src="imgs\Create_maze.png">


Create a maze
![image](imgs\Create_maze.png)

When clicking 'Find the shortest path' button, it will demonstate by a blue line
![image](imgs\Finding_optimal_path.png)

When the maze is unsolvable, it will not draw a blue line
![image](imgs\Unsolvable_maze.png)

When clicking 'Clear' button, it will return to initial state
![alt text](imgs\Initial.png)
### Button type
**Create wall**: Click to a specific block to draw a black block. Click again to erase it. <br/>
**Create starting point**: Click to a specific block to draw a yellow block. It can only be erased by clicking it again. The starting point can only represent once a maze. <br/>
**Create ending point**: Same as 'Creating starting point' button. <br/>
**Finding the shortest path**: Draw a blue line (opimal path) from starting point to ending point. It will not draw anything if the maze is unsolvable. <br/>
**Clear**: Return to the initial state <br/>



## Main problems
Add constants <br/>
Write READ.me <br/>
Write tests <br/>
Write docs <br/>
Change variables name (in proper name) <br/>
Clean code <br/>
Write requirements.txt <br/>