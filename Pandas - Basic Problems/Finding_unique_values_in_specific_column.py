import pandas as pd

a=pd.DataFrame({"Name":{0:"Hari",1:"abc",2:"xyz",3:"mno"},
                "Age":{0:24,1:22,2:22,3:21},
                "Job":{0:"TCS",1:"CTS",2:"INFOSYS",3:"ZOHO"}})
print(a.Age.unique())