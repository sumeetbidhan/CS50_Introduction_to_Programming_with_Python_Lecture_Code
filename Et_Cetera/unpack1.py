def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) *29 + knuts

#coins = [100,50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

#print(total(coins[0], coins[1], coins[2]),"Knuts")

# another way of doing the same is by unpacking using *
#print(total(*coins),"Knuts")
print(coins)
print(*coins)

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "KNUTS")

print(total(**coins), "knuts")