"""
Betting Arbitage Project
Author:  Delice Mambi-Lambu
completed: 20/11/2023

Project Aim: 
    To create a function that can take all possiblities of 
    an event i.e matrix and calculate if betting arbitage exists 
    if no arbitage exists return the closest riskless decimal odds 
    we should take. 
    
All bets should come in the form [A, draw, B] for games where a draw is a 
possible outcome or [A, B].

it is possible to have n number of possiblities for an event i.e horse race. 
for example: [x1, x2, ....., xn]

bets should be packaged in a list of lists i.e. [[1,2,1.7], [1.24,1.9, 2]] 

each row represents the possibities of a event from a corresponding betshop. 

"""

def isArbitage(candidate: list) -> bool: 
    """
    Useful Function for later checks for arbitage 
    Remember for arbitage to exist 
    for i in 0, ...., n :
        if sum(1/odds[i]) < 1: 
            arbitage exisits 
    
    """
    calc = 0 
    for i in range(len(candidate)):
        calc += 1/candidate[i]
    return calc < 1 , round(calc , 2)

# Sanity Check 
cand01 = [1.2, 2.3, 1.7]
isArbitage(cand01) # False / 1.86
cand02 = [17.0, 6.0, 1.2]
isArbitage(cand02) # False / 1.06
cand03 = [5, 3.7, 2.9]
isArbitage(cand03) # True / 0.82
# however finding odds like this is rare!

def betArbitage(bets: list) -> list: 
    """
    In order for this to work effectively you must have mutiple bets
    The more bet shops you are using the more the chance of achieving 
    arbitage 
    """
    
    final = bets[0][:]
    final.extend(list(isArbitage(bets[0])))
    print(final)
    
    for i in range(1,len(bets)):
        for j in range(len(bets[0])): 
            if bets[i][j] >  final[j]:
                final[j] = bets[i][j]
                
        final[-2:] = isArbitage(final[:-2])
        print(final)
        if final[-2] == True: 
            return final 
        
    return final 
 
# Testcases 

# NFL San Francisco vs. Seattle Seahawks - Moneyline 
test1 = [[1.31, 3.6],
         [1.33, 3.4],
         [1.33, 3.3],
         [1.3, 3.5],
         [1.32, 3.4]]
    
betArbitage(test1)
# Result: [1.33, 3.6, False, 1.03]

# NFL Miami Dolphins vs New York Jets - Moneyline 
test2 = [[1.22, 4.70],
         [1.2, 4.8],
         [1.22, 4.33],
         [1.22, 4.4],
         [1.21, 4.4]]
    
betArbitage(test2)
# Result: [1.22, 4.8, False, 1.03]

# PL Man City vs Liverpool  
test3 = [[1.65, 4.33, 4.2],
         [1.67, 4, 4.5],
         [1.57, 3.4, 4],
         [1.67, 4.2, 4.2],
         [1.67, 4.4, 4.5]]
    
betArbitage(test3)
# Result: [1.67, 4.4, 4.5, False, 1.05]

# PL Brentford vs Arsenal (Edited to get arbitage)
test4 = [[4.2, 3.75, 1.75],
         [4.4, 3.6, 1.8],
         [4.2, 3.1, 1.62],
         [4.2, 3.6, 1.8],
         [4.6, 3.9, 1.95]] # This will give arbitage 
    
betArbitage(test4)
# Result: [4.6, 3.9, 1.95, True, 0.99]

# PL Brentford vs Arsenal (No Arbitage)
test5 = [[4.2, 3.75, 1.75],
         [4.4, 3.6, 1.8],
         [4.2, 3.1, 1.62],
         [4.2, 3.6, 1.8],
         [4.6, 3.7, 1.77]] 
    
betArbitage(test5) 
# Result: [4.6, 3.75, 1.8, False, 1.04]
    