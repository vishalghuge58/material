
# d1={"mutable":"can not change","immutable":"can be changed","synonumus":"opposite meanig","Antonimues":"same meaning"}
# print(d1.keys())
# a=input("Enter the any word in above: ")
# print("The meaning of ",a,"  is :--",d1[a])

# Create a dictionary and take input from the user and return the meaning of the
# word from the dictionary

Dict = {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience", "programming":"the process of writing computer programs"}
print("Enter the Word")
Data1 = input()
print(Data1, "means", Dict[Data1])
