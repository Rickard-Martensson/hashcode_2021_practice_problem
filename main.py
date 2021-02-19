# Author: Rickard Mårtensson <rmarte@kth.se>

INPUT_FILE_NAME = "in"
OUTPUT_FILE_NAME = "out2"

"""
Calculates the number of points for the google hashcode preparation problem 2021

Usage:
    1.  choose INPUT_FILE_NAME to be the input data from the problem description
    2.  Either choose OUTPUT_FILE_NAME (on row 20) to be the name of your output file (the file to be tested),
        Example usage would be:
            4 OUTPUT_FILE_NAME = "my_own_output_to_be_tested.txt"
        OR
        feed your output directly to the program trough the command line.
        Example usage would be:
            > python main.py < my_own_output_to_be_tested.txt


"""


in_rader = None
out_rader = None


def läs_indata():
    global in_rader, out_rader
    fil_1 = open(INPUT_FILE_NAME, "r")
    in_rader = fil_1.readlines()

    indata = input()
    if indata and OUTPUT_FILE_NAME != None:
        läs_list = []
        for i in range(int(indata.split()[0])):
            läs_list.append(input())
        out_rader = läs_list

    else:
        fil_2 = open(OUTPUT_FILE_NAME, "r")
        out_rader = fil_2.readlines()
        out_rader.pop(0)


läs_indata()


använda_pizzor = set()
poäng = 0
lag = list(map(int, in_rader[0].split()))
# lag_2 = in_rader.split()[1]
# lag_3 = in_rader.split()[2]
# lag_4 = in_rader.split()[3]


def ge_toppings(rad):
    global använda_pizzor
    if rad in använda_pizzor:
        Exception(UnicodeDecodeError, "använder en pizza mer än en gång (lag # {} )".format(rad))
    använda_pizzor.add(rad)
    pizza_str = in_rader[rad]
    toppings = list(pizza_str.split())
    toppings.pop(0)
    # print(toppings)
    return toppings


# Strips the newline character
def main():
    global poäng
    for rad in out_rader:

        # idx_set = set()
        topping_set = set()
        pizza_idx = list(map(int, rad.split()))
        # print(pizza_idx)
        lagstorlek = pizza_idx[0]
        print(lag[3], lagstorlek - 1)
        print(lag[lagstorlek - 1])
        lag[lagstorlek - 1] -= 1
        if lag[lagstorlek] < 0:
            Exception(
                UnicodeError,
                "finns ej tillräckligt med lag av rätt storlek (försökte leverera fler ordrar av storlek {0} än vad det fanns lag av storlek {0})".format(lagstorlek),
            )
        if len(pizza_idx) - 1 != lagstorlek:
            Exception(UnicodeEncodeError, "felaktikt antal pizzor till ett lag (antalet pizzor = {}, lagstorlek = {}".format(len(pizza_idx) - 1, lagstorlek))
        for i in range(lagstorlek):
            # print(".", end="")
            # idx_set.add(pizza_idx[i + 1])
            # topping_set.add(in_rader[pizza_idx[i + 1] + 1])

            toppings = ge_toppings(pizza_idx[i + 1] + 1)
            for top in toppings:
                topping_set.add(top)

            # print(in_rader[i])
        # print(idx_set)

        # print(topping_set)
        poäng += len(topping_set) ** 2


main()
print("poäng =", poäng)
