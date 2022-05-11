# coding=utf-8
from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base
import random


class LuckyDrawer:
    def __init__(self, indexOfUICer,numOfFirstPrize, numOfSecondPrize,numOfThirdPrize):
        self.indexOfUICer = indexOfUICer
        self.numOfFirstPrize = numOfFirstPrize
        self.numOfSecondPrize = numOfSecondPrize
        self.numOfThirdPrize = numOfThirdPrize

    def generateFirstWinner(self):
        R1list = []
        for i in range(0,self.numOfFirstPrize):
            R1 = random.randint(0, self.indexOfUICer)
            R1list.append(R1)
        return R1list

    def generateSecondWinner(self):
        R2list = []
        for i in range(0, self.numOfSecondPrize):
            R2 = random.randint(0, self.indexOfUICer)
            R2list.append(R2)
        return R2list

    def generateThirdWinner(self):
        R3list = []
        for i in range(0, self.numOfThirdPrize):
            R3 = random.randint(0, self.indexOfUICer)
            R3list.append(R3)
        return R3list
