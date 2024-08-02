
import torch

class ShakespeareDataset:
    def __init__(self, file_name="input.txt"):
        self.file_name = file_name
        self.char_to_idx = {}
        self.idx_to_char = {}
        self.data = None
        self.load()
        self.encoded_data = self.encode(self.data, tensor=True)
    
    def load(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            self.data = f.read()
           
        print("Length of data: ", len(self.data))
        
        chars = sorted(list(set(self.data)))
        vocab_size = len(chars)
        print("Vocab size: ", vocab_size)
        print("Chars: ", chars)
        
        # TODO replace by BP/Sentencepiece encoding or tokenizer
        self.char_to_idx = {ch: i for i, ch in enumerate(chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(chars)}
        
    def encode(self, text, tensor=False):
        if tensor:
            return torch.tensor([self.char_to_idx[ch] for ch in text])
        else:
            return [self.char_to_idx[ch] for ch in text]
    
    def decode(self, encoded_text, tensor=False):
        if tensor:
            encoded_text = "".join([self.idx_to_char[i.item()] for i in encoded_text])
        else:
            return "".join([self.idx_to_char[i] for i in encoded_text])
        
    def split_dataset(self, split=0.9):
        self.train_data = self.encoded_data[:int(len(self.data)*split)]
        self.test_data = self.encoded_data[int(len(self.data)*split):]
        return self.train_data, self.test_data
    
    def get_batch(self, split="train", context_length=8, batch_size=32):
        if split == "train":
            data = self.train_data
        else:
            data = self.test_data
        ix = torch.randint(len(data) - context_length, (batch_size,))
        x = torch.stack([data[i:i+context_length] for i in ix])
        y = torch.stack([data[i+1:]])

        

def train(train_dataset, test_dataset, context_length=8):
    
    

if __name__ == "__main__":
    torch.manual_seed(42)
    dataset = ShakespeareDataset()

    print(dataset.encode("hello"))
    print(dataset.decode([46, 43, 50, 50, 53]))
    
    encoded_data = dataset.encode(dataset.data, tensor=True)
    print(encoded_data[:10])
    
    train_data, test_data = dataset.split_dataset()
    
    
    