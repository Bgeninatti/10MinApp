


class App:

    def __init__(self, name):
        self.name = name



def main():
    app = App("10MinApp")
    print(f"Hey! I'm {app.name}")


if __name__ == '__main__':
    main()
