class Locker:
    def __init__(self, filename: str):
        self.filename= filename

    def _create_locker(self):
        print("create locker")

    def _unlock_locker(self):
        print("unlock locker")

    def _return_locker(self):
        print("return locker")

    def menu(self):
        """
        Executes functions based on user input.
        Functions are creating, unlocking and returning lockers.
        Runs forever unless exit command is given through user input.

        :param self: self object
        :return None:
        """

        # Dict containing functions to user requests
        response_factory = {
            1: self._create_locker,
            2: self._unlock_locker,
            3: self._return_locker
        }

        while True:
            print("Choose one of the following actions")
            print("1:   Create a locker")
            print("2:   Unlock your locker")
            print("3:   Return your locker")
            print("3:   Exit \n")
            
            while True:
                try:
                    # Receive action from user
                    # If input is not an int it throws a ValueError
                    action = int(input("Type the number corresponding to an action:"))

                    # Exits if given exit action
                    if action == 4:
                        return

                    # Executes action
                    # If action not in dict it throws an KeyError
                    response_factory[action]()
                    break

                except KeyError:
                    print("Action not found")
                except ValueError:
                    print("Action not an int")

                # Unreachable
                else:
                    print("Something else went wrong.")
