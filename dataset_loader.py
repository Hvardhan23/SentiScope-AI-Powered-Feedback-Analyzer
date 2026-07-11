from datasets import load_dataset
from authentication import authenticate_huggingface

class DatasetLoader:

    Dataset_id = "zeroshot/twitter-financial-news-sentiment"

    def __init__(self, dataset_id: str = Dataset_id):
        authenticate_huggingface()  # Authenticate with Hugging Face
        self.dataset_id = dataset_id
        self.dataset = load_dataset(dataset_id, split="train")

    def load_dataset(self):
        return self.dataset.to_pandas()  # Convert the dataset to a pandas DataFrame

    def print_dataset(self):
        print(self.load_datasetz())

    def dataset_info(self):
        #columns_names = self.dataset.column_names
        #return columns_names
        return self.dataset.info()  # Return dataset information
    
    def choose_your_feature(self):
        choice = input(f"Enter the feature you want to choose from {self.dataset.column_names}: \n")

        if choice in self.dataset.column_names:
            return self.dataset[choice]
        else:
            print(f"Invalid choice. Please choose from {self.dataset.column_names}.")
            return self.choose_your_feature()  # Recursively ask for a valid choice
    

data=DatasetLoader()  # Create an instance of DatasetLoader
data.print_dataset
