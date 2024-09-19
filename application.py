from src import MachineLearning
import os


class Application:

    @classmethod
    def main(cls) -> None:
        source_path: str = '/Users/j/Documents/GitHub/RoadAI/resources/'
        destination_path: str = '/Users/j/Documents/GitHub/RoadAI/results/'

        for file in os.listdir(source_path):
            MachineLearning.launch(
                source_path + file,
                destination_path + file
            )
            input()
        return


if __name__ == "__main__":
    Application.main()
