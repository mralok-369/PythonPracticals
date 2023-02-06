class VotingAge:
    def __init__(self,eligibleage):
        self.eligibleage = eligibleage
    def isEligible(self,user_age):
        if user_age>=self.eligibleage:
            print("You are eligible for voting")
        else:
            print("Your are Not eligiable for voting")

v1 = VotingAge(18)
v1.isEligible(25)

v2 = VotingAge(16)
v2.isEligible(14)