from datasets import load_dataset, DatasetDict
import random

random.seed(1234)

dataset = load_dataset("lighteval/natural_questions_clean")

dataset_train_size = len(dataset['train'])
sampled_dataset_size = 10000

indices = random.sample(range(1, dataset_train_size), sampled_dataset_size)

small_dataset = dataset['train'].select(indices)


train_testvalid = small_dataset.train_test_split(test_size=0.3)
# Split the 10% test + valid in half test, half valid
test_valid = train_testvalid['test'].train_test_split(test_size=0.3)
# gather everyone if you want to have a single DatasetDict
train_test_valid_dataset = DatasetDict({
    'train': train_testvalid['train'],
    'test': test_valid['train'],
    'valid': test_valid['test']})

train_test_valid_dataset['train'].to_json("NQ_sampled_train.json")
train_test_valid_dataset['valid'].to_json("NQ_sampled_valid.json")
train_test_valid_dataset['test'].to_json("NQ_sampled_test.json")

breakpoint()