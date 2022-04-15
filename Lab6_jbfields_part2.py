#!/usr/bin/python

def tuitionCalc(tuition, increase):
    years = 0
    while tuition < 20000:
        tuition = tuition + (tuition * increase)
        years += 1
    return tuition, years
        
    

def main():
    tuition = 10000
    increase = .07
    values = tuitionCalc(tuition, increase)
    print(("Tuition will be doubled in %i years") % values[1])
    print(("Tuition will be $%.2f in %i years") % (values[0], values[1]))
    
    
if __name__ == "__main__":
    main()