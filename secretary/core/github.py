import requests



class GithubGraphQLClient:

    GITHUB_GRAPHQL_API = "https://api.github.com/graphql"

    def __init__(self, access_token):
        self._access_token = access_token
    
    def query(self, query_string):
        headers = {"Authorization": f"Bearer {self._access_token}"}
        data = {"query": query_string}
        response = requests.post(self.GITHUB_GRAPHQL_API, json=data, headers=headers).json()
        return response


def get_user_name(client: GithubGraphQLClient):
    query = """
    {
        viewer { 
            login
        }
    }
    """
    response = client.query(query_string=query)
    return response['data']['viewer']['login']


def get_pull_requests(client: GithubGraphQLClient, user_name: str):
    query = f"""
    {{
        user(login: "{user_name}") {{
            pullRequests(last: 10) {{
                totalCount
                nodes {{
                    createdAt
                    title
                    body
                    baseRepository {{
                        owner {{
                            login
                            id
                        }}
                        name
                        id
                    }}
                }}
            }}
        }}
    }}
    """
    
    response = client.query(query_string=query)
    return response
