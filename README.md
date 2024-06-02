# Navigating a Maze with Ghosts: An AI Agent Approach

## Overview

This project, "Ghosts in the Maze," is part of the Fall 520 course at Rutgers University. The project aims to implement and analyze various search algorithms within a dynamic environment. Specifically, it involves navigating an agent through a maze populated with moving ghosts.

## Project Structure

### Environment

The environment is a 51x51 maze represented by a 2D numpy array. Cells in the maze can be:
- **Blocked (0)**
- **Unblocked (1)**
- **Goal (2)**
- **Ghost on a normal cell (7)**
- **Multiple ghosts in a cell (8 or 10+)**

The maze is generated randomly with a 28% chance for each cell to be blocked. A valid maze must have a path from the upper left corner to the lower right corner, verified using BFS.

### Ghosts

Ghosts are initially placed in cells reachable from the start node. They move randomly to adjacent cells, including blocked cells. Their movement is simulated at each timestep, adding complexity to the agent's pathfinding.

### Agents

Four different agents are implemented, each employing different strategies to navigate the maze and avoid ghosts:

1. **Agent 1**: Plans the shortest path to the goal, ignoring ghosts.
2. **Agent 2**: Replans at each timestep based on current ghost positions.
3. **Agent 3**: Forecasts future positions of ghosts to choose the best move.
4. **Agent 4**: A custom strategy designed to outperform the previous agents.

## Implementation

### Agent Design

1. **Agent 1**: Uses a static shortest path algorithm and does not adjust for ghost positions after planning.
2. **Agent 2**: Recalculates the path at every step, reacting to the dynamic positions of ghosts.
3. **Agent 3**: Simulates future ghost positions to evaluate and choose the safest path forward.
4. **Agent 4**: Combines elements from previous agents with additional heuristics to optimize survival.

### Performance Analysis

The performance of each agent is evaluated based on their survivability across multiple randomly generated mazes with varying numbers of ghosts. The evaluation includes:
- Success rates of reaching the goal
- Average path lengths
- Computation times

## Results and Discussion

The lab report provides a detailed analysis of each agent's performance, highlighting strengths and weaknesses. Agent 3, which incorporates forecasting, generally performs better than Agent 2, which only reacts to current positions. However, the custom Agent 4 is designed to address specific shortcomings observed in Agents 1-3.

## How to Run

### Prerequisites

- Python 3.x
- numpy

### Installation

Clone the repository:

```bash
git clone https://github.com/Shushang1999/520AI-GhostsandMazes.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Usage
To run the simulation with a specific agent:

```bash
python3 <agent_number>.py
```
Replace <agent_number> with agent1, agent2, agent3, or agent4 to select the corresponding agent.
This give you the results in a .txt file inside results folder.

To convert the logical data into a .csv format:
```bash
cd Results
python3 results_text_to_csv.py
```

For More Information about this project, please look into this blog: https://medium.com/@shushang.nair/navigating-a-maze-with-ghosts-an-ai-agent-approach-7ecafe0b1c2b
