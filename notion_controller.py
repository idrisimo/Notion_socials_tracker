from notion_client import Client
from pprint import pprint

int_token = "secret_S9SEmPUibV8GqucR8BBYLAmVwtkaIiCEs9zFPu15DTY"
notion = Client(auth=int_token)

stuff_filter = {"filter": {
      "value": 'database',
      "property": 'object'
    }}
list_databases_response = notion.search(**{"query": "social media management dash", "filter": {
      "value": 'database',
      "property": 'object'
    }})

dashboard_db_id = list_databases_response["results"][0]["id"]
pprint(dashboard_db_id)

my_pages = notion.databases.query(**{"database_id": dashboard_db_id, "filter": {"property":"Instagram Status", "select": {"is_empty":True}}})
for page in my_pages["results"]:
  title = page["properties"]["Content"]["title"][0]["text"]["content"]
  page_id = page["id"]
  date = page["properties"]["Date"]["date"]
  insta_status = page["properties"]["Instagram Status"]
  print("Title: ",title)
  print("Page id: ",page_id)
  print("Date: ",date["start"])
  print("instagram status: ",insta_status["select"])
  # pprint(page["properties"])

  # update = notion.pages.update(**{"page_id":page_id, "properties":{"Instagram Status": {'select': {'color': 'green', 'id': 'Dkrp', 'name': 'Published'}}}})




def get_database_id(database_name):
  params = {"query": database_name, "filter": {"value": 'database',"property": 'object' }}
  database = notion.search(**params)
  try:
    database_id = database["results"][0]["id"]
    return database_id
  except Exception as err:
    print(f"Something went wrong:\n{err}")
  
def get_unpublished_pages(database_id):
  params = {"database_id": database_id, "filter": {"property":"Instagram Status", "select": {"is_empty":True}}}
  all_pages_response = notion.databases.query(**params)
  return all_pages_response

def page_info_extractor(pages):
  pages_list =[]
  for page in pages["results"]:
    title = page["properties"]["Content"]["title"][0]["text"]["content"]
    page_id = page["id"]
    try:
      date = page["properties"]["Date"]["date"]["start"]
    except TypeError as err:
      print("No date")
      date = "No Date available"
    insta_status = page["properties"]["Instagram Status"]["select"]
    pages_list.append({"page id": page_id,"title": title, "date": date, "instagram status": insta_status})
  return pages_list

def update_page_properties(page_id, properties):
  params = {"page_id":page_id, "properties":properties}
  update_response = notion.pages.update(**params)
  return update_response


