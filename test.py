volt_info = {
    "dict1"  : {"range": 30 * 10**-3,"resoltion": 0.001 * 10**-3, "Accuracy1": 0.05/100, "Accuracy2": 20},
    
    "dict2"  : {"range": 300 * 10**-3,"resoltion": 0.01 * 10**-3, "Accuracy1": 0.05/100, "Accuracy2": 5},

    "dict3"  : {"range": 3,"resoltion": 0.0001, "Accuracy1": 0.05/100, "Accuracy2": 5},

    "dict4"  : {"range": 30,"resoltion": 0.001, "Accuracy1": 0.05/100, "Accuracy2": 2},

    "dict5"  : {"range": 300,"resoltion": 0.01, "Accuracy1": 0.05/100, "Accuracy2": 2},

    "dict6"  : {"range": 1000,"resoltion": 0.1, "Accuracy1": 0.05/100, "Accuracy2": 2}
}

print(volt_info["dict1"]["range"])

input = 30.3
choice = ""

for item in volt_info.keys():
    if volt_info[item]["range"]+1 >= input:
        choice = item
        break

first = float(input*volt_info[item]["Accuracy1"])
second = float(volt_info[item]["resoltion"]*volt_info[item]["Accuracy2"])

print(choice)
print(str(first + second))


    

