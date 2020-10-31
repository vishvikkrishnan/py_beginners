# The code below explains how to extract the key of salary from the json objects.
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])
# output of salary = 70000
