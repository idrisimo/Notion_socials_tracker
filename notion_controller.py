from notion_client import Client

class Notion_controller():

  def __init__(self, auth_token):
    self.auth_token = auth_token
    
  def initialise(self):
    try:
      self.notion = Client(auth=self.auth_token)
    except Exception as err:
      print(f"Something went wrong:\n {err}")
      
  def get_database_id(self, database_name):
    params = {"query": database_name, "filter": {"value": 'database',"property": 'object' }}
    database = self.notion.search(**params)
    try:
      database_id = database["results"][0]["id"]
      return database_id
    except Exception as err:
      print(f"Something went wrong:\n{err}")
    
  def get_unpublished_pages(self, database_id):
    params = {"database_id": database_id, "filter": {"property":"Instagram Status", "select": {"is_empty":True}}}
    all_pages_response = self.notion.databases.query(**params)
    return all_pages_response

  def page_info_extractor(self, pages):
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

  def update_page_properties(self, page_id, properties):
    # Properties look like this: "properties":{"Instagram Status": {'select': {'color': 'green', 'id': 'Dkrp', 'name': 'Published'}}}
    params = {"page_id":page_id, "properties":properties}
    update_response = self.notion.pages.update(**params)
    return update_response


