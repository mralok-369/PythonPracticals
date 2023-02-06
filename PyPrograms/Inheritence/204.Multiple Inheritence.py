class CementDealer:
    def getCemenetCost(self,quantity):
        return quantity*300

class IronDealer:
    def getIronCost(self,quantity):
        return quantity*4500

class Builder(CementDealer,IronDealer):
    def getTotalCost(self,cQ,iQ):
        c_cost = self.getCemenetCost(cQ)
        i_cost = self.getIronCost(iQ)
        totalCost = c_cost + i_cost
        return totalCost

cement = int(input("Enter Cement quantity : "))
iron = int(input("Enter Iron quantity : "))
b = Builder()

total_cost = b.getTotalCost(cement,iron)
print("Total Cost : ",total_cost)