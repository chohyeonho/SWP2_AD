class Scores:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            line = line.rstrip().split()
            word=[]
            for i in line:
                i=i.split(',')
                word2=[]
                for j in i:
                    word2.append([j[1:],int(j[0])])
                word.append(word2)
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)
        print(self.words)


