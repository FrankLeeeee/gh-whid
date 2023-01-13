# gh-whid

> Use ChatGPT to summarize your work on a daily or weekly basis.
> 使用ChatGPT来生成你的日报和周报。

`whid` stands for **"What Have I done"**. This tool is to summarize your latest work on GitHub based on your Pull Request description with ChatGPT.


## Usage

1. Create a personal access token according to the [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

2. Create an OpenAI secret key via this [account page](https://beta.openai.com/account/api-keys).

3. Install and run 

```bash
# installation
pip install gh-whid

# generate work summary for today
whid

# generate work summary for the last n days
# a large value for n might lead to ChatGPT request rejected
# as it exceeds the max number of tokens allowed for prompt
whid -d n
```

**The credentials are stored in `~/.cache/whid/credentials.json`, do take care of this file and set expiry date on your credentials.**

Sample output will be like:

```text
===== ChatGPT Output =====
Summary:

- Updated the README
- Added an OpenAI Query demo
- Added a command line tool
- Added the release to PyPI workflow
- Updated the documentation
- Updated the release workflow

总结:

1. 更新README
2. 添加OpenAI查询演示
3. 添加命令行工具
4. 添加发布到PyPI的工作流
5. 更新文档
6. 更新发布工作流
```

