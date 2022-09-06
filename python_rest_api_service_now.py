import requests
import json
import pandas as pd

url = "https://myoffice.service-now.com/api/now/v1/table/incident?sysparm_query=assignment_group={gid}^stateIN6,7^priorityIN1,2^sys_created_on>javascript:gs.dateGenerate({sd},'23:59:59')^sys_created_on<javascript:gs.dateGenerate({ed},'00:00:00')&sysparm_fields={ls}&sysparm_display_value=true"
url = url.format(gid="",sd="'2022-07-31'",ed="'2022-09-01'",ls="number,description,state,sys_created_on,short_description,assigned_to")
headers = {
                'content-type': "application/json",
                'verify': "False",
                'cache-control': "no-cache"
        }
response = requests.request("GET", url, headers=headers, auth=('', ''))
data = json.loads(response.text)
dataframe = pd.DataFrame(data['result'])
