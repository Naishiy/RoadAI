from application import Application
from enums import ApplicationArguments


def main() -> None:
    arguments: dict = {ApplicationArguments.CAMERA_INDEX: 0}
    Application.main(arguments)


if __name__ == "__main__":
    main()
