# Micromouse Sim
The Micromouse Sim or short MMs, is a library intended to help in the development of the software of so called micro mouses.

## What is a Micromouse?
Micromouse is an event where small robot mice solve a 16×16 maze which began in the late 1970s. Events are held worldwide and are most popular in the UK, U.S., Japan, Singapore, India, and South Korea.
The maze comprises a 16×16 grid of cells, each 180 mm square with walls 50 mm high. The mice are entirely autonomous robots that must find their way from a predetermined starting position to the central area of the maze unaided. Therefore, the mouse needs to keep memory to map out the labyrinth. In addition, it has to detect when it has reached the goal. After reaching the goal, the mouse can still perform an additional search to find an optimal route. Once the optimal path has been found, the mouse will run that route in the shortest possible time. 

Exp.: https://www.youtube.com/watch?v=NqdZ9wbXt8k

## The Simulator
The Micromouse simulator is a tool that allows testing and optimizing the search algorithms for such mice. The simulator is modular, allowing for complete customization from different Mazes to different valuation functions. The following diagram depicts the different use cases of this library.

![Use case diagram](/app/docs/img/Diagrams/UseCase_MMs.png)

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
* [ ] Multiple Simulator types (Exp. SingleRunSimulator, MultiRunSimulator, ComparisonSimulator)
* [ ] Multiple Maze generators with different rules
* [ ] Multiple Mice with a variety of search algorithms
* [ ] Multiple evaluation function (Exp. shortest path, min inertia, etc.)

## Architecture
The library is written in python to not only allow the developer to run simulation quickly and easily in notebook tools like JupyterLab from any device but also to allow the use of Machine Learning frameworks like Tensorflow and PyTorch.

### Packages
The following diagram describes the package structure of the library.

![Package diagram](/app/docs/img/Diagrams/Package_MMs.png)

| Package | Description |
|---------|-------------|
| Simulators | Contains the different types of simulators. |
| Evaluators | Contains the different types of Evaluators to evaluate a mice performance. |
| Mice       | Contains the different types of default mice. |
| Maze       | Contains the different types of maze generators. |
| Cells      | Contains the different types of cells that can be used to build the mazes. |
| Tools      | Contains the different tools that can be used in the development. |
| Test       | Contains the different test of the classes. |

# TODO describe packages better

### Classes
The following diagram describes the classes of the packages of the library and how they relate to each other.

![Class diagram](app/docs/img/Diagrams/Class_MMs.png)

# TODO describe classes

## Testing
All the tests of the code can be found in the `/app/src/Test` directory. The tests are grouped by type.
### Unit Test
The unit tests of the code can be found in the `/app/src/Test/UnitTest` directory and are implemented with the native `unittest` python library . All tests have the following naming convention `[ClassName]_test.py` and cover following classes:

| Class | Package |
|-------|---------|
| Cell  | Cell |
| Maze | Maze |
| Mouse | Mouse |
| RandomWalker | Mouse |
| ErrorRaiser | Tools |

To execute the Unit Tests cd into `/app/src` and execute `python -m unittest discover -s "./Tests/UnitTest/" -p '*_test.py'` in the terminal.


## Documentation
The full documentation can be found in the `./app/docs/sphinx_doc/_build/html` and can be viewed in every browser by opening the [index.html](app/docs/sphinx_doc/_build/html/index.html) file.

### Documentation convention
In this project we use the Google documentation Style. Here an [Example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

### Autogenerate of Docs
In this project the documentation is automatically generated with [sphinx](https://www.sphinx-doc.org/en/master/).

```

```