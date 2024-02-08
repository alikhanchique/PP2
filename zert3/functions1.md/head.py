def solve(numheads, numlegs):
    chl = numheads*2
    rab = int((numlegs-chl)/2)
    chickens = numheads - rab
    x = "There are {} chickens and {} rabbits"
    print(x.format(chickens, rab))


numheads = int(input())
numlegs = int(input())
solve(numheads, numlegs)