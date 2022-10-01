### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
 
    
def chocolatePrice(ali_budget,bashir_budget):                        # I am basically here calculating HCF
    ali_budget = r_off(ali_budget)
    bashir_budget = r_off(bashir_budget)
    guess = 2                                                        
    counter = 1
    while ali_budget>=guess and bashir_budget>=guess:
        if ali_budget%guess==0 and bashir_budget%guess==0:
            ali_budget = ali_budget/guess
            bashir_budget = bashir_budget/guess
            counter = counter*guess
        else :
            guess = guess+1
    return counter 


#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###

def r_off(x):
    guess = 1
    while guess<=x:
        if x-guess<1:
            if x-guess>=0.5:
                return guess+1
            else :
                return guess
            return
        else :
            guess=guess+1 


def calculateProfit(ali_budget,bashir_budget):
    if type(ali_budget)==str or type(bashir_budget)==str or ali_budget<=0 or bashir_budget<=0:
        return "Not Possible"
    else :
        ali_budget = r_off(ali_budget)
        bashir_budget = r_off(bashir_budget)
        if ali_budget>bashir_budget:
            total_price_ali = ali_budget*(3/2)
            profit_ali = total_price_ali - ali_budget
            total_price_bashir = bashir_budget*(2) 
            profit_bashir = total_price_bashir - bashir_budget
            profit_ali = r_off(profit_ali)
            profit_bashir = r_off(profit_bashir)
            if profit_ali>=profit_bashir:
                return profit_ali
            else: 
                return profit_bashir
            return
        else :
            total_price_ali = ali_budget*(2)
            profit_ali = total_price_ali - ali_budget
            total_price_bashir = bashir_budget*(3/2) 
            profit_bashir = total_price_bashir - bashir_budget
            profit_ali = r_off(profit_ali)
            profit_bashir = r_off(profit_bashir)           
            if profit_ali>=profit_bashir:
                return profit_ali
            else: 
                return profit_bashir
            return
        return
    return



#### End OF MARKER


