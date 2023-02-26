from notion_client import Client
from pprint import pprint

int_token = "secret_S9SEmPUibV8GqucR8BBYLAmVwtkaIiCEs9zFPu15DTY"
notion = Client(auth=int_token)

# list_users_response = notion.users.list()
# pprint(list_users_response)

# results = notion.search(query="People").get("results")
# pprint(results)

# my_page = notion.databases.query()
# pprint(my_page)
stuff_filter = {"filter": {
      "value": 'database',
      "property": 'object'
    }}

list_databases_response = notion.search(**stuff_filter)
pprint(list_databases_response["results"])

# response = notion.pages.create({})
