import requests

# Make an API call, and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Kod stanu: ", r.status_code)
# Store API response in a variable
response_dict = r.json()
print("Całkowita liczba repozytoriów: ", response_dict['total_count'])

# Process results
repo_dicts = response_dict['items']
print('Liczba zwróconych repozytoriów: ', len(repo_dicts))
# Analyze first repositorium
repo_dict = repo_dicts[0]
# Show selected information about most rated repos
for repo_dict in repo_dicts:
    print(repo_dict['name'])
    print(repo_dict['owner']['login'])
    print(repo_dict['stargazers_count'])
    print(repo_dict['html_url'])
    print(repo_dict['description'])