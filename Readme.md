# Micromouse Sim
The Micromouse Sim, or short MMs, is a library intended to help develop the pathfinding algorithms of so-called micro mouses. It was born as the final project of my bachelor's degree, where we had to develop an application that heavily used traditional object-oriented programming. To check out the delivered version, you can use the following command: `git checkout bfe77c811ecdf3e20b3bdffe05ad9d782a339f7b`

My goal was not only to fulfill my assignment but to create something that would become the basis of an environment where I could try out what I would learn in the future and experiment with new technologies. (And to have a fun project to work on when I'm bored 😆)

Therefore don't expect perfect code, being, in most cases, the first time I try out something (and it was probably 2 am when I wrote it). Still, please take a look if you are interested because I would be thrilled to have any feedback on how I could have done things better and about best practices. 

## What is a Micromouse?
Micromouse is an event where small robot mice solve a 16×16 maze which began in the late 1970s. Events are held worldwide and are most popular in the U.K., U.S., Japan, Singapore, India, and South Korea.
The maze comprises a 16×16 grid of cells, each 180 mm square with walls 50 mm high. The mice are autonomous robots that must find their way from a predetermined starting position to the central area of the maze unaided. Therefore, the mouse needs to keep memory to map out the labyrinth. In addition, it has to detect when it has reached the goal. After reaching the goal, the mouse can still perform an additional search to find an optimal route. Once the optimal path has been found, the mouse will run that route in the shortest possible time. 

Exp.: [https://www.youtube.com/watch?v=NqdZ9wbXt8k?t=17](https://www.youtube.com/watch?v=NqdZ9wbXt8k?t=17)

## The Simulator
The Micromouse simulator is a tool that allows testing and optimizing the search algorithms for such mice. Furthermore, the simulator is modular, allowing for complete customization from different Mazes to different evaluation functions. The following diagram depicts the other use cases of this library.

![Use case diagram](app/docs/img/Diagrams/UseCase_MMs.png)

Let's now see how to evaluate a mouse and how the library works behind the scenes. The following section explains the procedure; please refer to the `example.ipynb` notebook for a hands-on example.

![Sequence diagram](app/docs/img/Diagrams/Sequence_MMs.png)

When we call `Simulator.run()`, the Simulator starts by triggering the Mouse to solve the maze. First, the Mouse sets up the labyrinth. Once it receives the maze properties, it starts to solve the maze. Once it reaches an end position, it returns the path it found a solution to the Evaluator of the Simulator, which will return the simulation score to the Simulator.
## The Requirements
The following is a list of requirements the tool fulfills or will fulfill:
* [x] The App shall generate a random Maze.
* [x] The App shall simulate the Mice.
* [x] The App shall evaluate the Mice in the Maze.
* [x] The App shall keep track of all relevant simulation metrics and store them in a DataBase:
  * [x] Metadata of environment and mice to allow for the replication of the simulation
  * [x] Experiment data for debugging
  * [x] Results to analyze the performance
* [x] Visualization shall be generated

Nice to have:
* [ ] Multiple Simulator types 
  * [x] SingleRunSimulator
  * [ ] ComparisonSimulator
  * [ ] MultiRunSimulator (Same maze and different mazes)
    * [ ] AverageScoreSimulator
    * [ ] WeightedAverageScoreSimulator
    * [ ] BestScoreSimulator
    * [ ] WorstScoreSimulator
* [ ] Multiple Maze generators with different rules
* [ ] Multiple Mice with a variety of search algorithms
  * [ ] RandomWalkerWithMemory
  * [ ] Mice with post solution procecing (Mice that after having complete the first run calculates a best path with the memory gained.)
    * [ ] GraphMice
* [X] Multiple evaluation function
  * [x] shortest path
  * [x] direction change
  * [ ] min inertia

## Architecture
The library is written in python to allow the developer to run Simulations quickly and easily in notebook tools like JupyterLab from any device and to allow the use of Machine Learning frameworks like Tensorflow and PyTorch.

### Packages
The following diagram describes the package structure of the library.

![Package diagram](app/docs/img/Diagrams/Package_MMs.png)

| Package | Description |
|---------|-------------|
| Simulators | Contains the different types of simulators. |
| Evaluators | Contains the different types of Evaluators to evaluate a mice performance. |
| Mice       | Contains the different types of default mice. |
| Maze       | Contains the different types of maze generators. |
| Cells      | Contains the different types of cells that can be used to build the mazes. |
| Tools      | Contains the different tools that can be used in the development. |
| DataBases  | Contains the different connectors to the different supported DataBases. |
| Test       | Contains the different test of the classes. |

### Classes
The following diagram describes the classes of the library packages and how they relate to each other.

![Class diagram](app/docs/img/Diagrams/Class_MMs.png)

| Class | Description |
|-------|-------------|
| *Simulator* |All the Simulator abstract class children can be used to run the simulations and evaluate the Mice. It receives as an input the instance of the mouse which has to be assessed, the type of maze in which the mouse has to be evaluated, and the type of the evaluator that will be used to determine the mouse. (This class is an implementation of an abstract factory design pattern. Instead of using the original pattern, it was decided to pass directly the constructor of the classes instead of a build function that returns an instance of the class to simplify the implementation of custom variants of the Evaluator and Maze classes. This class is also an implementation of a Strategy design pattern.)|
| SingleRunSimulation | The SingleRunSimulation is a child of the Simulator class and is used to run simulations where the mouse does only one maze run and then is evaluated. |
| *MultiRunSimulation* | All the children of the MultiRunSimulation abstract class can be used to run multiple simulations and evaluate the Mice. |
| *Maze* | All the children of the Maze abstract class can be used to generate a maze in which then a mouse can be evaluated. (This class is an implementation of a Strategy design pattern.)|
| DFS_R | The DFS_R class is a child of the Maze class and generates a maze with the "Depth-first search (Recursive implementation)" method. For more information about this method, please refer to the Wikipedia page [Here](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_implementation) |
| Cell | The Cell class is a class that describes the single cells of a maze. |
| *Mouse* | All the children of the Mouse abstract class can be used to implement the search algorithms to solve the mazes. These are the algorithms to be evaluated. |
| RandomWalker | The RandomWalker class is a child of the Mouse class and is the most naive algorithm to solve a maze. It has no memory and chooses its next step entirely randomly. It's a good baseline to compare against. |
| RandomWalkerWithMemory | The RandomWalkerWithMemory class is a child of the Mouse class. It has a memory of where it was and the not taken paths and chooses its next step randomly from the paths it wasn't. So it's a good baseline to compare against. |
| *Evaluator* | All the children of the Evaluator abstract class implement a way to evaluate the mice in the simulations. (This class is an implementation of a Strategy design pattern.)|
| PathLen | The PathLen class is a child of the Evaluator class and evaluates the mice by calculating the path length of the solution the mice find. |
| ChangeDirection | The ChangeDirection class is a child of the Evaluator class and evaluates the mice by calculating the times the mouse changes its direction in its solution. |
| *DataBase* | All the children of the DataBase abstract class are used to store the simulation data and their results in a DataBase. |
| Mysql | The Mysql class is a child of the DataBase class and stores the simulation data and their results into a Mysql DataBase. |
| ErrorRaiser | The ErrorRaiser class implements multiple methods to check certain things (exp.: type of var) and raises errors accordingly. |
| Visualizer | The Visualizer class is used to visualize different components like a maze. |

For more detailed information about the different implemented classes and their methods, please refer to the [Documentation](#documentation).

## Testing
All code tests can be found in the `/app/src/Test` directory. The tests are grouped by type. All the code that is found in the master branch of the repository was tested and passed 100% of the test in the `/app/src/Test` directory. For a complete description of every test, please refer to the [Documentation](#documentation).

### Static Test
The whole code is tested with pylint, and every finding is analyzed and resolved.
### Unit Test
The unit tests of the code can be found in the `/app/src/Test/UnitTest` directory and are implemented with the native `unittest` python library. All tests have the following naming convention `[ClassName]_test.py` and cover the following classes:

| Class | Package |
|-------|---------|
| Cell  | Cell |
| Maze | Maze |
| Mouse | Mouse |
| ErrorRaiser | Tools |

To execute the Unit Tests cd into `/app/src` and execute `python -m unittest discover -s "./Tests/UnitTest/" -p '*_test.py'` in the terminal.


## Documentation
The complete documentation can be found in the `./app/docs/sphinx_doc/_build/html` and can be viewed in every browser by opening the [index.html](app/docs/sphinx_doc/_build/html/index.html) file. The following command can be used to open the docs from the terminal `open app/docs/sphinx_doc/_build/html/index.html`

### Documentation convention
In this project, we use the Google documentation Style. Here an [Example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

### Autogenerate of Docs
In this project, the documentation is automatically generated with [sphinx](https://www.sphinx-doc.org/en/master/). [Here](https://www.youtube.com/watch?v=b4iFyrLQQh4) a useful tutorial on how to generate the html documentation.

Here some useful commands:
``` Bash
cd app/docs/sphinx_doc # this changes the dir to sphinx_doc
sphinx-apidoc -o . ../../src # generates the rst
make html # generates the html files in app/docs/sphinx_doc/_build
```
The rst files define the layout of the documentation pages. For more information, please refer to the sphinx [documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## Continuous Integration & Continuous Delivery (CI / CD)
It is planed that this repository will have a Jenkins instance attached to it to test, autogenerate documentation and delivery the code.
