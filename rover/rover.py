import json


class RoverBase:
    def __init__(self):
        self.base_position = {
            "x": "0",
            "y": "0"
        }

class Rover(RoverBase):
    def __init__(self, rover_id, position):
        self.rover_id = rover_id
        self.rover_position = {
            "x": str(position["x"]),
            "y": str(position["y"])
        }
        self.direction = "north"
        self.moves = {}
        self.moves[len(self.moves) + 1] = {
            "rover-id": self.rover_id,
            "position": {
                "x": self.rover_position["x"],
                "y": self.rover_position["y"]
            },
            "direction": self.direction
        }
        self.moves_left = 20

    def output_move(self):
        with open("output.json", "w") as f:
            json.dump(self.moves, f)
            f.close()

    def move_foward(self):
        if self.check_moves_left():
            self.update_direction("move_foward")
            self.update_postion()
            self.moves[len(self.moves) + 1] = {
                "rover-id": self.rover_id,
                "position": {
                    "x": self.rover_position["x"],
                    "y": self.rover_position["y"]
                },
                "direction": self.direction
            }

        self.update_moves_left()

    def turn_left(self):
        if self.check_moves_left():
            self.update_direction("turn_left")
            self.moves[len(self.moves) + 1] = {
                "rover-id": self.rover_id,
                "position": {
                    "x": self.rover_position["x"],
                    "y": self.rover_position["y"]
                },
                "direction": self.direction
            }

        self.update_moves_left()

    def turn_right(self):
        if self.check_moves_left():
            self.update_direction("turn_right")
            self.moves[len(self.moves) + 1] = {
                "rover-id": self.rover_id,
                "position": {
                    "x": self.rover_position["x"],
                    "y": self.rover_position["y"]
                },
                "direction": self.direction
            }

        self.update_moves_left()

    def check_moves_left(self):
        if (self.moves_left - 1) <= 0:
            return False
        return True

    def update_moves_left(self):
        self.moves_left = self.moves_left - 1

    def update_direction(self, move):
        if move == "move_foward":
            self.direction = self.direction
        elif move == "turn_right":
            if self.direction == "north":
                self.direction = "east"
            elif self.direction == "east":
                self.direction = "south"
            elif self.direction == "south":
                self.direction = "west"
            elif self.direction == "west":
                self.direction = "north"
        elif move == "turn_left":
            if self.direction == "north":
                self.direction = "west"
            elif self.direction == "west":
                self.direction = "south"
            elif self.direction == "south":
                self.direction = "east"
            elif self.direction == "east":
                self.direction = "north"

    def update_postion(self):
        if self.direction == "east" or self.direction == "west":
            self.rover_position["x"] = str(int(self.rover_position["x"]) + 1)
        elif self.direction == "north" or self.direction == "south":
            self.rover_position["y"] = str(int(self.rover_position["y"]) + 1)


def main():
    data = json.load(open('command.json'))
    for k, v in sorted(data.items()):
        for sk, sv in sorted(v.items()):
            if sv == "new-rover":
                rover = Rover("1AFC", v["postion"])
            elif sk == "command" and not sv == "new-rover":
                if sv == "move-foward":
                    rover.move_foward()
                if sv == "turn-left":
                    rover.turn_left()
                if sv == "turn-right":
                    rover.turn_right()

        if int(k) == len(data):
            rover.output_move()

if __name__ == '__main__':
    main()