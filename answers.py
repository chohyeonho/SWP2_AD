class Answers:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip().split(',')

            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)
        print(self.words)