class Strategie(object):
    """
    definit une strategie de robot de facon abstraite
    """
    def __init__(self, robot):
        """
        robot : Robot
        """
        self.robot = robot