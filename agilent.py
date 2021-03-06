class Agilent:
    def volt_direct(self, input) -> str:
        choice = ""
        for item in self.direct_voltage.keys():
            if self.direct_voltage[item]["range"] + 1 >= input:
                choice = item
                break

        first = float(input*self.direct_voltage[item]["Accuracy1"])
        second = float(self.direct_voltage[item]["resolution"]*self.direct_voltage[item]["Accuracy2"])

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

            return (first + second)

        elif 65 < hz < 1000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_1khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_1khz"])

            return (first + second)
            
        elif 1000 <= hz < 5000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_1k-5khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_1k-5khz"])

            return (first + second)
            
        elif 5000 <= hz <= 20000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_5k-20khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_5k-20khz"])

            return (first + second)
            
        else:
            return "Something wrong"

    def ohm(self, input) -> str:
        choice = ""
        for item in self.resistans.keys():
            if self.resistans[item]["range"] + 1 >= input:
                choice = item
                break
        
        if item == "dict8":
            if input < 100*10**6:
                first = float(input*self.resistans[item]["accuracy1<=100M"])
                second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2<=100M"])

                return (first + second)
            else:
                first = float(input*self.resistans[item]["accuracy1>=100M"])
                second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2>=100M"])

                return (first + second)

        first = float(input*self.resistans[item]["accuracy1"])
        second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2"])

        return (first + second)

    def current_direct(self, input) -> str:
        choice = ""
        for item in self.resistans.keys():
            if self.resistans[item]["range"] + 1 >= input:
                choice = item
                break

        first = float(input*self.resistans[item]["accuracy1"])
        second = float(self.resistans[item]["resolution"]*self.resistans[item]["accuracy2"])

        return (first + second)

    def current_alternating(self, input, hz) -> str:
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

            return (first + second)

        elif 65 < hz < 1000:
            first = float(input*self.alternating_voltage[item]["Accuracy1_1khz"])
            second = float(self.alternating_voltage[item]["resolution"]*self.alternating_voltage[item]["Accuracy2_1khz"])

            return (first + second)
        else:
            return "Something wrong"

    def voltage_ac_dc(self, input, hz) -> str:
        #The range
        choice = ""
        for item in self.ac_dc_voltage.keys():
            if self.ac_dc_voltage[item]["range"] + 1 >= input:
                choice = item
                break 
        #HZ
        if 45 <= hz <= 65:
            temp = self.ac_dc_voltage[item]["Accuracy1_45–65hz"]
            first = float(input*temp)
            second = float(self.ac_dc_voltage[item]["resolution"]*self.ac_dc_voltage[item]["Accuracy2_45–65hz"])

            return (first + second)

        elif 65 < hz < 1000:
            first = float(input*self.ac_dc_voltage[item]["Accuracy1_1khz"])
            second = float(self.ac_dc_voltage[item]["resolution"]*self.ac_dc_voltage[item]["Accuracy2_1khz"])

            return (first + second)
            
        elif 1000 <= hz < 5000:
            first = float(input*self.ac_dc_voltage[item]["Accuracy1_1k-5khz"])
            second = float(self.ac_dc_voltage[item]["resolution"]*self.ac_dc_voltage[item]["Accuracy2_1k-5khz"])

            return (first + second)
            
        elif 5000 <= hz <= 20000:
            first = float(input*self.ac_dc_voltage[item]["Accuracy1_5k-20khz"])
            second = float(self.ac_dc_voltage[item]["resolution"]*self.ac_dc_voltage[item]["Accuracy2_5k-20khz"])

            return (first + second)
            
        else:
            return "Something wrong"
    
    def current_ac_dc(self, input, hz) -> str:
        #The range
        choice = ""
        for item in self.ac_dc_current.keys():
            if self.ac_dc_current[item]["range"] + 1 >= input:
                choice = item
                break 
        #HZ
        if 45 <= hz <= 65:
            temp = self.ac_dc_current[item]["Accuracy1_45–65hz"]
            first = float(input*temp)
            second = float(self.ac_dc_current[item]["resolution"]*self.ac_dc_current[item]["Accuracy2_45–65hz"])

            return (first + second)

        elif 65 < hz < 1000:
            first = float(input*self.ac_dc_current[item]["Accuracy1_1khz"])
            second = float(self.ac_dc_current[item]["resolution"]*self.ac_dc_current[item]["Accuracy2_1khz"])

            return (first + second)
        else:
            return "Something wrong"
    
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
                "range":                300 * 10**-6,
                "resolution":           0.01 * 10**-6,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       0.9/100,
                "Accuracy2_1khz":       25,
                },
            "dict2"  : {
                "range":                3000 * 10**-6,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       0.9/100,
                "Accuracy2_1khz":       25,
                },
            "dict3"  : {
                "range":                30 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       0.9/100,
                "Accuracy2_1khz":       25,
                },
            "dict4"  : {
                "range":                300 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.6/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       0.9/100,
                "Accuracy2_1khz":       25,
                },
            "dict5"  : {
                "range":                3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                },
            "dict6"  : {
                "range":                10,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1/100,
                "Accuracy2_1khz":       25,
                }
        }

        self.ac_dc_voltage = {
            "dict1"  : {
                "range":                30 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    40,
                "Accuracy1_1khz":       0.8/100,
                "Accuracy2_1khz":       45,
                "Accuracy1_1k-5khz":    1.1/100,
                "Accuracy2_1k-5khz":    45,
                "Accuracy1_5k-20khz":   1.1/100,
                "Accuracy2_5k-20khz":   60
                },
            
            "dict2"  : {
                "range":                300 * 10**-3,
                "resolution":           0.01 * 10**-3,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       0.8/100,
                "Accuracy2_1khz":       30,
                "Accuracy1_1k-5khz":    1.1/100,
                "Accuracy2_1k-5khz":    30,
                "Accuracy1_5k-20khz":   1.1/100,
                "Accuracy2_5k-20khz":   45
                },

            "dict3"  : {
                "range":                3,
                "resolution":           0.0001,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                "Accuracy1_1k-5khz":    1.6/100,
                "Accuracy2_1k-5khz":    30,
                "Accuracy1_5k-20khz":   2.1/100,
                "Accuracy2_5k-20khz":   45
                },

            "dict4"  : {
                "range":                30,
                "resolution":           0.001,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                "Accuracy1_1k-5khz":    1.6/100,
                "Accuracy2_1k-5khz":    30,
                "Accuracy1_5k-20khz":   2.1/100,
                "Accuracy2_5k-20khz":   45
                },

            "dict5"  : {
                "range":                300,
                "resolution":           0.01,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                "Accuracy1_1k-5khz":    1.6/100,
                "Accuracy2_1k-5khz":    30,
                "Accuracy1_5k-20khz":   2.1/100,
                "Accuracy2_5k-20khz":   45
                },

            "dict6"  : {
                "range":                1000,
                "resolution":           0.1,
                "Accuracy1_45–65hz":    0.7/100,
                "Accuracy2_45–65hz":    25,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                "Accuracy1_1k-5khz":    1.6/100,
                "Accuracy2_1k-5khz":    30,
                "Accuracy1_5k-20khz":   "-",
                "Accuracy2_5k-20khz":   "-"
                }
        }
    
        self.ac_dc_current = {
            "dict1"  : {
                "range":                300 * 10**-6,
                "resolution":           0.01 * 10**-6,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    30,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                },
            "dict2"  : {
                "range":                3000 * 10**-6,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    30,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                },
            "dict3"  : {
                "range":                30 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    30,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                },
            "dict4"  : {
                "range":                300 * 10**-3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.8/100,
                "Accuracy2_45–65hz":    30,
                "Accuracy1_1khz":       1.1/100,
                "Accuracy2_1khz":       30,
                },
            "dict5"  : {
                "range":                3,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.9/100,
                "Accuracy2_45–65hz":    35,
                "Accuracy1_1khz":       1.3/100,
                "Accuracy2_1khz":       35,
                },
            "dict6"  : {
                "range":                10,
                "resolution":           0.001 * 10**-3,
                "Accuracy1_45–65hz":    0.9/100,
                "Accuracy2_45–65hz":    35,
                "Accuracy1_1khz":       1.3/100,
                "Accuracy2_1khz":       35,
            }
        }



agilent = Agilent()

print(f"volt_direct(20): {agilent.volt_direct(20)}")

print(f"volt_alternating(25, 50): {agilent.volt_alternating(25, 50)}")

print(f"ohm(100): {agilent.ohm(100)}")

print(f"current_direct(1): {agilent.current_direct(1)}")

print(f"current_alternating(1.343, 50): {agilent.current_alternating(1.343, 50)}")

print(f"voltage_ac_dc(1.343, 50): {agilent.voltage_ac_dc(1.343, 50)}")

print(f"current_ac_dc(1.343, 50): {agilent.current_ac_dc(1.343, 50)}")



    

