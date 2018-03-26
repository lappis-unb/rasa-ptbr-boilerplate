# Config Live Transfer

In order to user `Live Transfer` feature, it is necessary to do some steps.

The first thing to do is to set the department hash, on the file used as corpus on bot. The department hash must be placed on `department` field, in the section named `livechat-transfer`, as showed on the image below. The file being used as corpus is the one defined on field `HUBOT_CORPUS`field, at docker-compose file.

![Updating corpus file](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/update_corpus.png)

The department hash can be obtained on the URL in department `edit screen` as showed on image below.

![Getting department id](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/department_hash.png)

To get to department `edit screen` close the left side menu, and click on three points icon. Select the **Livechat** option.

![Livechat option](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/livechat_option.png)

Now it is necessary to select the department to be used on transfer action. On the left side menu, click on **Departments**, and then click on the department name.

![Select department](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/new_department.png)

Once you got the department hash and placed on corpus file, restart the hubot-natural service, in order to update the container and reload `corpus` file.

Lastly is important to remember that the live transfer conversation channel will be created between any available user on department. For that, the user must be online, and must be previously added as an agent on department being used(The one defined on corpus file). For that, You must first add the user as an agent. At the right side menu, select the **User Management** option. , so search for the user you want, then click in **ADD**.

![Adding user as agent](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/add_as_agent.png)

Then again on the department edit screen, add the user to department by selecting him on **Available agents**. Then click on **Save** option.

![Add agent to department](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/add_user_to_department.png)
