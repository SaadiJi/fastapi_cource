def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
print(total(*coins), "Knuts")  # * unpack the coins list as param for def total

coinss = {"galleons":100, "sickles":50, "knuts": 25}
print(total(**coinss), "Knuts") # ** unpack the coinss dict 
# the difference b/w list and dict list unpack with singl * and dict with **py