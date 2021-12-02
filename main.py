from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont

from answers import Answers
from scores import Scores
from questions import Questions
import random

class PersonalityGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.answers = Answers('answers.txt')
        self.scores = Scores('scores.txt')
        self.questions=Questions('questions.txt')

        questionLayout = QGridLayout()

        self.questionWindow=QTextEdit()
        self.questionWindow.setReadOnly(True)


        questionLayout.addWidget(self.questionWindow,0,0)


        answerLayout=QGridLayout()

        self.whichAnswer=QTextEdit()
        self.whichAnswer.setReadOnly(True)
        answerLayout.addWidget(self.whichAnswer,0,0,1,2)

        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        answerLayout.addWidget(self.message, 1, 0, 1, 2)

        self.numInput=QLineEdit()
        self.numInput.setMaxLength(1)
        answerLayout.addWidget(self.numInput,2,0)

        self.selectButton=QToolButton()
        self.selectButton.setText("선택")
        self.selectButton.clicked.connect(self.selectClicked)
        answerLayout.addWidget(self.selectButton,2,1)

        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        answerLayout.addWidget(self.newGameButton, 3, 0)

        mainLayout=QGridLayout()
        #mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(questionLayout,0,0)
        mainLayout.addLayout(answerLayout,0,1)

        self.setLayout(mainLayout)

        self.setWindowTitle("성격 테스트")

        self.startGame()

    def startGame(self):
        #self.question=Question()
        #self.questionWindow.setText(self.word.randFromDB())
        self.gameOver=False
        self.numList=[]
        self.scoreDict=dict()
        for i in range(8):
            r = random.randrange(52)
            self.numList.append(r)
        self.remainingQuestions=8
        self.display(self.numList[0])

    def display(self,n):
        self.questionWindow.setText(self.questions.words[n])
        self.lenAnswer=len(self.answers.words[n])
        answertext=""
        for i in range(self.lenAnswer):
            answertext+=str(i+1)+'. '
            answertext+=self.answers.words[n][i]
            answertext+='\n'
        self.whichAnswer.setText(answertext)

    def selectClicked(self):
        selectChar=self.numInput.text()
        self.numInput.clear()
        self.message.clear()
        if self.gameOver==True:
            self.message.setText("게임 중이 아닙니다")
            return

        if len(selectChar)!=1:
            self.message.setText("입력의 길이가 1이 아닙니다.")
            return

        if not selectChar.isdigit():
            self.message.setText("숫자가 아닙니다.")
            return

        if int(selectChar)>self.lenAnswer or int(selectChar)==0:
            self.message.setText("1~"+str(self.lenAnswer)+" 사이의 숫자를 입력해주세요.")
            return
        self.answerSelect(int(selectChar))
    def answerSelect(self,m):
        n=8-self.remainingQuestions
        n=self.numList[n]
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    fontDB=QFontDatabase()
    fontDB.addApplicationFont("./D2Coding.ttf")
    app.setFont(QFont("D2Coding"))
    game = PersonalityGame()
    game.show()
    sys.exit(app.exec_())




