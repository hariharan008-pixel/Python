import pandas as pd

a=pd.DataFrame({"Name":{0:"Hari",1:"abc",2:"xyz",3:"mno"},
                "Age":{0:24,1:23,2:22,3:21},
                "Job":{0:"TCS",1:"CTS",2:"INFOSYS",3:"ZOHO"}})

a.to_excel("file2.xlsx")

print("DataFrame is saved as Excel Successfully")
