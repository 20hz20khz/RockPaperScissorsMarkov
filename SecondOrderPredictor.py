# SecondOrderPredictor.py
# use a 2D array to store probabilities

class SecondOrderPredictor():
    def __init__(self, NumStates):#constructor
        self.mNumStates = NumStates
        self.kUnknownState = -1
        self.kMaxRecentStates = NumStates
        self.mRecentStates = []
        width, height = NumStates,NumStates*NumStates;
        self.mMarkovTransitionMatrix = [[0 for x in range(width)] for y in range(height)]

# mMarkovTransitionMatrix[numStates*numStates][numStates]
# Creates a Matrix containing numstates^2 lists, each of numstates items, all set to 0
# width, height = NumStates,NumStates*NumStates;
# Matrix = [[0 for x in range(width)] for y in range(height)]

    def getSecondOrderState(self,state1,state2): # private member function
        return state1+self.mNumStates*state2

    def setLearn(self,current1stOrderState): # public 
        if len(self.mRecentStates) == self.kMaxRecentStates:
            self.mRecentStates.pop(0) # remove oldest item
        self.mRecentStates.append(current1stOrderState)
        # print("len recentstates"+str(self.mRecentStates))
        if len(self.mRecentStates) == self.kMaxRecentStates:
            prev2ndOrderState = self.getSecondOrderState(self.mRecentStates[0],self.mRecentStates[1])
            self.mMarkovTransitionMatrix[prev2ndOrderState][current1stOrderState]+=1

    def getPredictedState(self): # public
        if len(self.mRecentStates) < self.kMaxRecentStates:
            return self.kUnknownState
        predictedState = self.kUnknownState
        highestFrequency = 0
        current2ndOrderState=self.getSecondOrderState(self.mRecentStates[1],self.mRecentStates[2])
        for i in range(0,self.mNumStates):
            frequency=self.mMarkovTransitionMatrix[current2ndOrderState][i]
            if frequency > highestFrequency:
                highestFrequency = frequency
                predictedState = i
        return predictedState
            
