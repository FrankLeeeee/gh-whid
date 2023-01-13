import click
from whid.core import GithubGraphQLClient, ChatGPT, CredentialManager

@click.command()
@click.option('-o', '--owner', help="The repository owner")
@click.option('-r', '--repository', help="The repository name")
def cli(owner, repository):
    # TODO: the parameters are not used yet
    cm = CredentialManager()
    success = cm.load_credential()

    if not success:
        cm.prompt_user_inputs()

    gh_client = GithubGraphQLClient(access_token=cm.github_access_token)
    user_name = gh_client.get_user_name()
    prs = gh_client.get_pull_requests(user_name)

    pr_info_list = []

    # TODO: time range should be added
    # currently only check for the latest 10 PRs for simplicity
    for i in range(-10, 0):
        pr = prs['data']['user']['pullRequests']['nodes'][i]
        body = pr['body']
        title = pr['title']
        pr_info = f'{title}\n{body}'
        pr_info_list.append(pr_info)

    pr_summary = '\n'.join(pr_info_list)
    chatGPT = ChatGPT(api_key=cm.openai_secret_key)
    summary = chatGPT.summarize(pr_summary)

    print("===== ChatGPT Output =====")
    print(summary)

if __name__ == '__main__':
    cli()