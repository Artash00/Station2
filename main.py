import random

def RandomCube():
    cube1 = random.randrange(1, 6, 1)
    cube2 = random.randrange(1, 6, 1)
    cubeSum = cube1 + cube2
    print("The sum of dice is ", cube1, "+", cube2, "=", cubeSum)
    return cubeSum
    
cubeSum = RandomCube()
if cubeSum == 7 or cubeSum == 11:
    print("You won")
elif cubeSum == 2 or cubeSum == 3 or cubeSum == 12:
    print("You lose")
elif (cubeSum >= 4 and cubeSum <= 6) or (cubeSum >= 8 and cubeSum <= 10):
    goalNumber = cubeSum
    print ("Now your goal number", goalNumber)

    while True:
        cubeSum = RandomCube()
        if cubeSum == 7:
            print("You lose")
            break
        elif cubeSum == goalNumber:
            print("You won")
            break
