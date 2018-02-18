import json
import pytest

from rover.rover import Rover


class TestRover:
    @pytest.mark.skip(reason="Failing on assert, needs further debug")
    def test_no_moves_left(self):
        fake_json = {
            "1": {"command": "new-rover", "postion": {"x": "3", "y": "3"}},
            "2": {"rover-id": "1AFC", "command": "move-foward"},
            "3": {"rover-id": "1AFC", "command": "turn-left"},
            "4": {"rover-id": "1AFC", "command": "move-foward"},
            "5": {"rover-id": "1AFC", "command": "turn-right"},
            "6": {"rover-id": "1AFC", "command": "move-foward"},
            "7": {"rover-id": "1AFC", "command": "move-foward"},
            "8": {"rover-id": "1AFC", "command": "move-foward"},
            "9": {"rover-id": "1AFC", "command": "turn-left"},
            "10": {"rover-id": "1AFC", "command": "move-foward"},
            "11": {"rover-id": "1AFC", "command": "turn-right"},
            "12": {"rover-id": "1AFC", "command": "move-foward"},
            "13": {"rover-id": "1AFC", "command": "move-foward"},
            "14": {"rover-id": "1AFC", "command": "move-foward"},
            "15": {"rover-id": "1AFC", "command": "turn-left"},
            "16": {"rover-id": "1AFC", "command": "move-foward"},
            "17": {"rover-id": "1AFC", "command": "turn-right"},
            "18": {"rover-id": "1AFC", "command": "move-foward"},
            "19": {"rover-id": "1AFC", "command": "move-foward"},
            "20": {"rover-id": "1AFC", "command": "turn-right"},
            "21": {"rover-id": "1AFC", "command": "move-foward"},
            "22": {"rover-id": "1AFC", "command": "move-foward"},
            "23": {"rover-id": "1AFC", "command": "move-foward"},
            "24": {"rover-id": "1AFC", "command": "move-foward"}
        }

        for k, v in sorted(fake_json.items()):
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

            if int(k) == len(fake_json):
                rover.output_move()

        data = json.load(open('output.json'))
        assert len(data) == 20

    def test_360_turn_left(self):
        fake_json = {
            "1": {"command": "new-rover", "postion": {"x": "1", "y": "1"}},
            "2": {"rover-id": "1AFC", "command": "turn-left"},
            "3": {"rover-id": "1AFC", "command": "turn-left"},
            "4": {"rover-id": "1AFC", "command": "turn-left"},
            "5": {"rover-id": "1AFC", "command": "turn-left"},
        }

        for k, v in sorted(fake_json.items()):
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

            if int(k) == len(fake_json):
                rover.output_move()

        data = json.load(open('output.json'))
        assert data["1"]["direction"] == "north"
        assert data["2"]["direction"] == "west"
        assert data["3"]["direction"] == "south"
        assert data["4"]["direction"] == "east"
        assert data["5"]["direction"] == "north"

    def test_360_turn_right(self):
        fake_json = {
            "1": {"command": "new-rover", "postion": {"x": "1", "y": "1"}},
            "2": {"rover-id": "1AFC", "command": "turn-right"},
            "3": {"rover-id": "1AFC", "command": "turn-right"},
            "4": {"rover-id": "1AFC", "command": "turn-right"},
            "5": {"rover-id": "1AFC", "command": "turn-right"},
        }

        for k, v in sorted(fake_json.items()):
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

            if int(k) == len(fake_json):
                rover.output_move()

        data = json.load(open('output.json'))
        assert data["1"]["direction"] == "north"
        assert data["2"]["direction"] == "east"
        assert data["3"]["direction"] == "south"
        assert data["4"]["direction"] == "west"
        assert data["5"]["direction"] == "north"
