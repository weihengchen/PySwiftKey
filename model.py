import sys;
import nltk;

def get_traindata(input_file):
    fin = open(input_file);
    data = [];
    for line in fin.readlines():
        data.append(line.decode('utf-8'));
    words = ' '.join(data);
    fin.close();
    return words;

def get_tokens(raw):
    toker = nltk.RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
    tokens = toker.tokenize(raw);
    return tokens;

def build_model():
    words = get_traindata('test.txt');
    tokens = get_tokens(words);
    text = nltk.Text(tokens);
    bigram = nltk.bigrams(text);
    trigram = nltk.trigrams(text);

    unigram = nltk.FreqDist(text);
    bigram = nltk.FreqDist(bigram);
    trigram = nltk.FreqDist(trigram);

class SwiftKeyModel(object):

    #init
    def __init__(self):
        self.traindata = '';
        self.tokens = [];
        self.unigram = nltk.Text(self.tokens);
        self.bigram = nltk.Text(self.tokens);
        self.trigram = nltk.Text(self.tokens);
        return ;

    #train data set
    def set_traindata(self, input_files):
        # set encoding
        enc = 'utf-8';
        data = [];
        for f in input_files:
            fin = open(f);
            for line in fin.readlines():
                data.append(line.decode(enc));
            fin.close();
        self.traindata = ''.join(data);
        return ;

    def clean_data(self):
        toker = nltk.RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True);
        self.tokens = toker.tokenize(self.traindata);
        return ;

    def train(self):
        self.clean_data();

        text = nltk.Text(self.tokens);
        self.unigram = nltk.FreqDist(text);
        self.bigram = nltk.FreqDist(nltk.bigrams(text));
        self.trigram = nltk.FreqDist(nltk.trigrams(text));

    def predict(self, words):
        words = words.split(' ');
        uni = words[-1];
        bi = tuple(words[-2:]);
        tri = tuple(words[-3:]);

        print self.unigram[words[-1]];
        print self.bigram[tuple(words[-2:])];
        print self.trigram[tuple(words[-3:])];

        return;

if __name__ == '__main__':
    """
    words = get_traindata('test.txt');
    tokens = get_tokens(words);
    text = nltk.Text(tokens);
    bigram = nltk.bigrams(text);
    trigram = nltk.trigrams(text);

    unifreq = nltk.FreqDist(text);
    bifreq = nltk.FreqDist(bigram);
    trifreq = nltk.FreqDist(trigram);
    """
    f = ['test.txt', 'input.txt'];
    model = SwiftKeyModel();
    model.set_traindata(f);
    model.train();
    model.predict('the dog I');


