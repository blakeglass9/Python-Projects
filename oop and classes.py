class Game:
    variable1 = 'Hello'
    variable2 = 'World!'

if __name__ == "__main__":
    x = Game()
    # Correctly use {} as placeholders for format
    print("{} {}".format(x.variable1, x.variable2))

