import json
import requests

url = 'https://api.github.com/graphql'
api_token = 'dce3b4447251158c91e118c30a92e322df444650'

data = '{"query": "{ search(query:\\"stars:>100\\", type:REPOSITORY, first:100){ nodes { ... on Repository {nameWithOwner url createdAt updatedAt pullRequests{ totalCount } releases{ totalCount } primaryLanguage{ name } all_issues: issues{ totalCount } closed_issues: issues(states:CLOSED){ totalCount } } } } }"}'
headers = {'Authorization': 'token %s' % api_token}
response = requests.post(url, headers=headers, data=data)

if response.status_code != 200:
    print("Houve um erro ao executar o codigo")

print(json.loads(response.text))


