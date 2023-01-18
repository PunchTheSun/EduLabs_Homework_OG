# Bathroom Class

class Bathroom:
    def __init__(self,size: float, toilet: bool = True, sink: bool = True, shower: bool = True):
        self.__size = size
        self.__toilet = toilet
        self.__sink = sink
        self.__shower = shower

    def get_size(self) -> float:
        return self.__size

    def get_toilet(self) -> bool:
        return self.__toilet

    def get_sink(self) -> bool:
        return self.__sink

    def get_shower(self) -> bool:
        return self.__shower

    def set_size(self, new_size: float) -> bool:
        if isinstance(new_size, float) and new_size > 0:
            self.__size = new_size
            return True
        else:
            print("Invalid input, Please enter a number\nNumber has to be greater than 0")
            return False

    def set_toilet(self, new_toilet: str) -> bool:
        match new_toilet.lower():
            case "yes":
                self.__toilet = True
            case "no":
                self.__toilet = False
            case _:
                print("Invalid input, Please enter 'Yes' or 'No' only")
        return True

    def set_sink(self, new_sink: str) -> bool:
        match new_sink.lower():
            case "yes":
                self.__sink = True
            case "no":
                self.__sink = False
            case _:
                print("Invalid input, Please enter 'Yes' or 'No' only")
        return True

    def set_shower(self, new_shower: str) -> bool:
        match new_shower.lower():
            case "yes":
                self.__shower = True
            case "no":
                self.__shower = False
            case _:
                print("Invalid input, Please enter 'Yes' or 'No' only")
        return True
