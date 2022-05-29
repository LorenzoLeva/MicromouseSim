import mysql.connector
from Tools.ErrorRaiser import ErrorRaiser
from Mice.Mouse import Mouse
from DataBases.DataBase import DataBase
from Evaluators.Evaluator import Evaluator
from Mazes.Maze import Maze
from Simulations.Simulation import Simulation

class Mysql(DataBase):
    '''The Mysql class is an extension of the mysql.connector and allows to store the simulation runs in a mysql database.'''

    def __init__(self, host: str, user: str, password: str) -> None:
        self.host = ErrorRaiser.raiseIsNotType(str, host)
        self.user = ErrorRaiser.raiseIsNotType(str, user)
        self.password = ErrorRaiser.raiseIsNotType(str, password)

        self.db = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.db.cursor()

        self.createDB()

    def insertMouse(self, mouse: Mouse, simID: int) -> int:
        mouse = ErrorRaiser.raiseNotSubclass(Mouse, mouse)
        simID = ErrorRaiser.raiseIsNotType(int, simID)

        sql = f'INSERT INTO `MMs`.`Mouse` (`type`, `seed`, `simulator`) VALUES (\'{type(mouse).__name__}\', \'{mouse.seed}\', \'{simID}\');'

        return self.insertAndGetID(sql)
    
    def insertMaze(self, maze: Maze, simID: int) -> int:
        maze = ErrorRaiser.raiseNotSubclass(Maze, maze)
        simID = ErrorRaiser.raiseIsNotType(int, simID)

        sql = f'INSERT INTO `MMs`.`Maze` (`type`, `xSize`, `ySize`, `startCellX`, `startCellY`, `endCell1X`, `endCell1Y`, `endCell2X`, `endCell2Y`, `simulator`) VALUES (\'{type(maze).__name__}\', \'{maze.x}\', \'{maze.y}\', \'{maze.startCell[0]}\', \'{maze.startCell[1]}\', \'{maze.endCell1[0]}\', \'{maze.endCell1[1]}\', \'{maze.endCell2[0]}\', \'{maze.endCell2[1]}\', \'{simID}\');'

        return self.insertAndGetID(sql)

    def insertSimulation(self, sim: Simulation) -> int:
        sim = ErrorRaiser.raiseNotSubclass(Simulation, sim)

        if sim.results != None:
            sql = f'INSERT INTO `MMs`.`Simulation` (`type`) VALUES (\'{type(sim).__name__}\');'

            simID = self.insertAndGetID(sql)

            self.insertMouse(sim.mouse, simID)
            self.insertMaze(sim.maze, simID)
            self.insertEvaluator(sim.evaluator, simID)
        else:
            raise Exception('To be able to store the simulation in the DB it has to be run first.')


    def insertEvaluator(self, evaluator: Evaluator, simID: int) -> int:
        evaluator = ErrorRaiser.raiseNotSubclass(Evaluator, evaluator)
        simID = ErrorRaiser.raiseIsNotType(int, simID)

        sql = f'INSERT INTO `MMs`.`Evaluator` (`type`, `scoreResult`, `timeToSolve`, `simulator`) VALUES (\'{type(evaluator).__name__}\', \'{evaluator.scoreResults}\', \'{evaluator.timeToSolve}\', \'{simID}\');'

        return self.insertAndGetID(sql)

    def insertAndGetID(self, sql: str) -> int:
        sql = ErrorRaiser.raiseIsNotType(str, sql)

        self.cursor.execute(sql)
        self.db.commit()

        return self.cursor.lastrowid
    
    def execute(self, sql):
        sql = ErrorRaiser.raiseIsNotType(str, sql)

        self.cursor.execute(sql)
        self.db.commit()

    def createDB(self):
        '''Creates the DataBase with all the needed tables if it doesn't exists.'''

        f = open("./DataBases/sql_files/createDB.sql", "r")

        for q in f.read().replace("\n", "").split(";"):
            self.execute(q)

