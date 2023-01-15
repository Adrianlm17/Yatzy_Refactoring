from src.pips import Pips

class Yatzy:


    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dices):
        count = 0

        for die in dices:
            count += die

        return count


    @staticmethod
    def yatzy(*dice):

        if dice[0] * 5 == sum(dice):
            return 50
        return 0
    

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE
    

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO
    

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE
    

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR
    

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE
    

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX
    

    @staticmethod
    def score_pair(*dice):

        duplicateDice = [x for i, x in enumerate(dice) if i != dice.index(x)]

        if len(duplicateDice) > 1:
            for die in duplicateDice:
                if die > duplicateDice[0]:
                    max = die
                else:
                    max = duplicateDice[0]
            return (max + max)  
        return 0

    
    @staticmethod
    def two_pair(*dice):
        
        duplicateDice = [x for i, x in enumerate(dice) if i != dice.index(x)]
        
        duplicateDice = list(dict.fromkeys(duplicateDice))

        if len(duplicateDice) == 2:
            duplicateDice.sort()

            count = duplicateDice[-1] + duplicateDice[-1] + duplicateDice[-2] + duplicateDice[-2]
            return count
        return 0

    
    @staticmethod
    def three_of_a_kind(*dados):

        num = 0
        for dado in dados:
            
            if dados.count(num) >= 3:
                
                return num + num + num
            
            num += 1
            
        return 0


    @staticmethod
    def four_of_a_kind(*dados):

        num = 0
        for dado in dados:
            
            if dados.count(num) >= 4:
                
                return num + num + num + num
            
            num += 1
            
        return 0



    @staticmethod
    def smallStraight(*dados):

        if 1 and 2 and 3 and 4 and 5 in dados:
            return 15
        return 0
    

    @staticmethod
    def largeStraight(*dados):
        
        if 2 and 3 and 4 and 5 and 6 in dados:
            return 20
        return 0
    

    @staticmethod
    def fullHouse(*dados):
        
        num1 = 1
        num2 = 1
        for dado in dados:
            
            if dados.count(num1) == 2:
                
                for dado in dados:
                    if dados.count(num2) == 3:
                    
                        return num1 + num1 + num2 + num2 + num2
                    
                    num2 += 1

            num1 += 1
            
        return 0
