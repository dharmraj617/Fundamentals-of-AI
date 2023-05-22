def transport():
    left_bank = ["man", "goat", "cabbage", "wolf"]
    right_bank = []

    while len(right_bank) != 4:
        if "goat" in left_bank and "cabbage" in left_bank:
            left_bank.remove("goat")
            right_bank.append("goat")
            print("Man has transported goat to the right bank")
            left_bank.remove("cabbage")
            right_bank.append("cabbage")
            print("Man has transported cabbage to the right bank")
            left_bank.append("goat")
            right_bank.remove("goat")
            print("Man has transported goat to the left bank")
            left_bank.remove("wolf")
            right_bank.append("wolf")
            print("Man has transported wolf to the right bank")
            print("Man has returned to the left bank")
            left_bank.remove("goat")
            right_bank.append("goat")
            print("Man has transported goat to the right bank")

        break


print("All items have been transported to the right bank")

transport()