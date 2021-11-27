class Agilent:
    def __init__(self):
        self.direct_voltage = {
            "dict1"  : {
                "range": 30 * 10**-3,
                "resolution": 0.001 * 10**-3, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 20
                },
            
            "dict2"  : {
                "range": 300 * 10**-3,
                "resolution": 0.01 * 10**-3, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 5
                },

            "dict3"  : {
                "range": 3,
                "resolution": 0.0001, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 5
                },

            "dict4"  : {
                "range": 30,
                "resolution": 0.001, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 2
                },

            "dict5"  : {
                "range": 300,
                "resolution": 0.01, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 2
                },

            "dict6"  : {
                "range": 1000,
                "resolution": 0.1, 
                "Accuracy1": 0.05/100, 
                "Accuracy2": 2
                }
        }

        self.alternating_voltage = {
            "dict1"  : {
                "range":                30 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       0.7/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   1/100,
                "Accuracy2_5k-20khz":   40
                },
            
            "dict2"  : {
                "range":                300 * 10**-3,
                "resolution":           0.01 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       0.7/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   1/100,
                "Accuracy2_5k-20khz":   40
                },

            "dict3"  : {
                "range":                3,
                "resolution":           0.0001,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1.5/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   2/100,
                "Accuracy2_5k-20khz":   40
                },

            "dict4"  : {
                "range":                30,
                "resolution":           0.001,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1.5/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   2/100,
                "Accuracy2_5k-20khz":   40
                },

            "dict5"  : {
                "range":                300,
                "resolution":           0.01,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1.5/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   2/100,
                "Accuracy2_5k-20khz":   40
                },

            "dict6"  : {
                "range":                1000,
                "resolution":           0.1,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                "Accuracy1_1k-5khz":    1.5/100,
                "Accuracy2_1k-5khz":    25,
                "Accuracy1_5k-20khz":   "-",
                "Accuracy2_5k-20khz":   "-"
                }
        }

        self.resistans = {
            "dict1" : {
                "range" :       30,
                "resolution" :  0.001,
                "accuracy1" :   0.2/100,
                "accuracy2" :   10
            },
            "dict2" : {
                "range" :       300,
                "resolution" :  0.01,
                "accuracy1" :   0.2/100,
                "accuracy2" :   5
            },
            "dict3" : {
                "range" :       3*10**3,
                "resolution" :  0.0001*10**3,
                "accuracy1" :   0.2/100,
                "accuracy2" :   5 
            },
            "dict4" : {
                "range" :       30*10**3,
                "resolution" :  0.001*10**3,
                "accuracy1" :   0.2/100,
                "accuracy2" :   5 
            },
            "dict5" : {
                "range" :       300*10**3,
                "resolution" :  0.01*10**3,
                "accuracy1" :   0.2/100,
                "accuracy2" :   5 
            },
            "dict6" : {
                "range" :       3*10**6,
                "resolution" :  0.0001*10**6,
                "accuracy1" :   0.6/100,
                "accuracy2" :   5 
            },
            "dict7" : {
                "range" :       30*10**6,
                "resolution" :  0.001*10**6,
                "accuracy1" :   1.2/100,
                "accuracy2" :   5 
            },
            "dict8" : {
                "range" :       300*10**6,
                "resolution" :  0.01*10**6,
                "accuracy1<=100M" :   2/100,
                "accuracy2<=100M" :   10,
                "accuracy1>100M" :   8/100,
                "accuracy2>100M" :   10 
            }
        }


        self.direct_current = {
            "dict1" : {
                "range" :       300*10**-6,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.2/100,
                "accuracy2" :   3 
            },
            "dict2" : {
                "range" :       3000*10**-6,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.2/100,
                "accuracy2" :   3 
            },
            "dict3" : {
                "range" :       30*10**-3,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.2/100,
                "accuracy2" :   3 
            },
            "dict4" : {
                "range" :       300*10**-3,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.2/100,
                "accuracy2" :   3
            },
            "dict5" : {
                "range" :       3,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.3/100,
                "accuracy2" :   10
            },
            "dict6" : {
                "range" :       10,
                "resolution" :  0.001*10**6,
                "accuracy1" :   0.3/100,
                "accuracy2" :   10
            },

        }

        self.alternating_current = {
            "dict1"  : {
                "range":                30 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    20,
                "Accuracy1_1khz":       0.7/100,
                "Accuracy2_1khz":       25,
                }
        }

    def volt_direct(self, input) -> str:
        choice = ""
        for item in self.direct_voltage.keys():
            if self.direct_voltage[item]["range"] + 1 >= input:
                choice = item
                break

        first = float(input*self.direct_voltage[item]["Accuracy1"])
        second = float(self.direct_voltage[item]["resolution"]*self.direct_voltage[item]["Accuracy2"])

        print(choice)
        return str(first + second)

    def volt_alternating(self, input, hz) -> str:
        #The range
        choice = ""
        for item in self.alternating_voltage.keys():
            if self.direct_voltage[item]["range"] + 1 >= input:
                choice = item
                break 
        #HZ
        if 45 <= hz <= 65:
            temp = self.alternating_voltage[item]["Accuracy1_45–65hz"]
            first = float(input*temp)
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_45–65hz"])

            print(choice)
            return (first + second)

        elif 65 < hz < 1000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_1khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_1khz"])

            print(choice)
            return (first + second)
            
        elif 1000 <= hz < 5000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_1k-5khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_1k-5khz"])

            print(choice)
            return (first + second)
            
        elif 5000 <= hz <= 20000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_5k-20khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_5k-20khz"])

            print(choice)
            return (first + second)
            
        else:
            return "Something wrong"

    def ohm(self, input) -> str:
        choice = ""
        for item in self.resistans.keys():
            print(item)
            if self.resistans[item]["range"] + 1 >= input:
                choice = item
                break
        
        if item == "dict8":
            if input < 100*10**6:
                first = float(input*self.resistans[item]["accuracy1<=100M"])
                second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2<=100M"])

                print(choice)
                return (first + second)
            else:
                first = float(input*self.resistans[item]["accuracy1>=100M"])
                second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2>=100M"])

                print(choice)
                return (first + second)

        first = float(input*self.resistans[item]["accuracy1"])
        second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2"])

        print(choice)
        return (first + second)

    def current_direct(self, input) -> str:
        choice = ""
        for item in self.resistans.keys():
            print(item)
            if self.resistans[item]["range"] + 1 >= input:
                choice = item
                break

        first = float(input*self.resistans[item]["accuracy1"])
        second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2"])

        print(choice)
        return (first + second)

    def current_alternating(self, input, hz) -> str:
        ...
        

        

agilent = Agilent()

print(agilent.volt_direct(20))

print(agilent.volt_alternating(25, 50))

print(25*(0.6/100) + (20*0.001))

print(agilent.ohm(100))

print(agilent.current_direct(1))

    

