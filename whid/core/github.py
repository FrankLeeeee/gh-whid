import requests
from datetime import date, timedelta



class GithubGraphQLClient:

    GITHUB_GRAPHQL_API = "https://api.github.com/graphql"

    def __init__(self, access_token):
        self._access_token = access_token
    
    def query(self, query_string):
        headers = {"Authorization": f"Bearer {self._access_token}"}
        data = {"query": query_string}
        response = requests.post(self.GITHUB_GRAPHQL_API, json=data, headers=headers).json()
        return response

    def get_user_name(self):
        query = """
        {
            viewer { 
                login
            }
        }
        """
        response = self.query(query_string=query)
        return response['data']['viewer']['login']

    def get_pull_requests(self, user_name: str, last_n: int = 10, cursor: str = None):
        if cursor is None:
            offset = ""
        else:
            offset = f"before: \"{cursor}\""

        query = f"""
        {{
            user(login: "{user_name}") {{
                pullRequests(last: {last_n} {offset}) {{
                    totalCount
                    edges {{
                        cursor
                        node {{
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
        }}
        """
        
        response = self.query(query_string=query)
        return response
