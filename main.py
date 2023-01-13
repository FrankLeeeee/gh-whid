from secretary.core.github import GithubGraphQLClient, get_pull_requests, get_user_name
from secretary.core.request import set_credentials, summarize


if __name__ == "__main__":
    OPENAI_API_KEY = ""
    access_token = ""
    gh_client = GithubGraphQLClient(access_token=access_token)
    user_name = get_user_name(gh_client)
    prs = get_pull_requests(gh_client, user_name)

    pr_info_list = []
    for i in range(-5, 0):
        pr = prs['data']['user']['pullRequests']['nodes'][i]
        body = pr['body']
        title = pr['title']
        pr_info = f'{title}\n{body}'
        pr_info_list.append(pr_info)

    pr_summary = '\n'.join(pr_info_list)

    set_credentials(OPENAI_API_KEY)
    summary = summarize(pr_summary)
    print(summary)

