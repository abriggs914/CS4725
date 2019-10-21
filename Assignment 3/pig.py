import random

class OneTurnPig :
    
    def __init__(self, n, n_simulations) :
        self.n = n
        self.n_simulations = n_simulations
        self.die_possibilities = list(range(1,7))
        self.counts = [0 for i in range(7)]
        self.simulate()
        
    def __repr__(self) :
        res = "n = " + str(self.n) + "; " + str(self.n_simulations) + " simulations.\n"
        for i in range(7) :
            count = "%.5f" % (self.counts[i] / self.n_simulations)
            if i == 0 :
                res += "\t0\t" + count
            else :
                res += "\t" + str(n + ((i - 1) % 6)) + "\t" + count
            res += "\n"
        return res
        
    def simulate(self) :
        for i in range(self.n_simulations) :
            self.hold_at_n()
        
    def roll(self) :
        return random.choice(self.die_possibilities)
    
    def hold_at_n(self) :
        rollSum = self.roll()
        while(0 < rollSum < self.n) :
            rollVal = self.roll()
            if rollVal == 1 :
                rollSum = 0
            else :
                rollSum += rollVal
        if rollSum == 0 :
            self.counts[0] += 1
        else :
            self.counts[(rollSum % self.n) + 1] += 1
        return rollSum
    
if __name__ == "__main__" :
    n = 25
    print(OneTurnPig(25, 100))
    print(OneTurnPig(25, 10000))
    print(OneTurnPig(25, 1000000))
    for i in range(15, 26) :
        print(OneTurnPig(i, 1000000))