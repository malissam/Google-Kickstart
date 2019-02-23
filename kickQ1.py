import sys
def guess(a, b):
    g = ((a+1)+b)//2
    return g

def main():
    
    t = int(input())
    
    
    
    for x in range(1,t+1):
    
        
        a, b = [int(x) for x in input().split()]
        tries = int(input())
        for i in range(1,tries+1):
            
            guessed_number = guess(a,b)
            print(guessed_number)
            answer = input()
            if answer == "CORRECT":
                break 
            elif answer == "TOO_SMALL":
                a = guessed_number
                #guessed_number = b+a/(2+guessed_number)
                #if (b-a) == 1:
                #    guessed_number = b
            elif answer == "TOO_BIG":
                b = guessed_number
            #wrong_answer
        else: 
            break
       
main()  