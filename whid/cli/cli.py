import click
from whid.core import GithubGraphQLClient, ChatGPT, CredentialManager
from datetime import datetime, timedelta

@click.command()
@click.option('-d', '--days', type=int, default=1, help="The last number of days to trace, set to 1 by default. A large number might cause ChatGPT to reject the request.")
def cli(days):
    cm = CredentialManager()
    success = cm.load_credential()

    if not success:
        cm.prompt_user_inputs()

    gh_client = GithubGraphQLClient(access_token=cm.github_access_token)
    user_name = gh_client.get_user_name()
    

    pr_info_list = []

    # github api uses UTC timezone
    current_datetime = datetime.utcnow()
    end_datetime = current_datetime - timedelta(days=days)

    # some bookkeeping variables
    cursor = None
    search_flag = True

    while search_flag:
        # get the pull requests
        response = gh_client.get_pull_requests(user_name, last_n=10, cursor=cursor)

        # iterate and extract data
        for i in range(-10, 0):
            pull_request = response['data']['user']['pullRequests']['edges'][i]

            # check timestamp
            created_at = pull_request['node']['createdAt']
            created_datetime = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')

            if created_datetime < end_datetime:
                search_flag = False
                break

            # get information
            body = pull_request['node']['body']
            title = pull_request['node']['title']
            pr_info = f'{title}\n{body}'
            pr_info_list.append(pr_info)

            # update cursor for pagination
            cursor = pull_request['cursor']

    pr_summary = '\n'.join(pr_info_list)
    chatGPT = ChatGPT(api_key=cm.openai_secret_key)
    summary = chatGPT.summarize(pr_summary)

    print("===== ChatGPT Output =====")
    print(summary)

if __name__ == '__main__':
    cli()