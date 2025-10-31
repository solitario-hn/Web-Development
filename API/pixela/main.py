import requests
from datetime import datetime
USERNAME="solit"
TOKEN="hemnixxxxxxxx"
header={
     "X-USER-TOKEN":TOKEN,
}
DATE_TODAY=datetime.now().strftime("%Y%m%d")
endpoint="https://pixe.la/v1/users"
graph_id="ggrxxxx"

#CREATING THE ACCOUNT AT PIXELA USING POST REQUEST AND SENDING JSON DATA (OUR PARAMTERS) TO THE ENDPOINT.
# endpoint="https://pixe.la/v1/users"
# parameters={
#     "token":"hemnihemni0225",
#     "username":"solit",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes",
# }

# response=requests.post(url=endpoint,json=parameters)   
# response.raise_for_status()


# #CREATING A GRAPH
#graph_endpoint=f"https://pixe.la/v1/users/{USERNAME}/graphs"

# parameters={
#      "id":"ggr899",
#      "name":"Read",
#      "unit":"commit",
#      "type":"int",
#      "color":"ajisai",
# }

# response=requests.post(url=f"{endpoint}/{USERNAME}/graphs",headers=header,json=parameters)
# response.raise_for_status()

#POSTING A PIXEL ON THE CREATED GRAPH

pixel_paramters={
     "date":DATE_TODAY,
     "quantity":"10",
 }

pixel_post=requests.post(url=f"{endpoint}/{USERNAME}/graphs/{graph_id}",headers=header,json=pixel_paramters)
pixel_post.raise_for_status()


# updated_para={"quantity":"20"}
# pixel_put=requests.put(url=f"{endpoint}/{USERNAME}/graphs/{graph_id}/{DATE_TODAY}",headers=header,json=updated_para)
# pixel_put.raise_for_status()
# print(pixel_put.text)

#DELETING A PIXEL USING REQUESTS.DELETE 
# pixel_delete=requests.delete(url=f"{endpoint}/{USERNAME}/graphs/{graph_id}/{DATE_TODAY}",headers=header)
# pixel_delete.raise_for_status()
# print(pixel_delete.text)
