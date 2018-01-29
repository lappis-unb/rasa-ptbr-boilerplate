# Hubot Natural Bot

## Adding Hubot Natural Bot

To add the bot into your Rocket Chat, you must create an administrator account. In the initial screen, click on **Register a new account**, and fill the informations, you don't need to use a real email account.

![New account example](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/new_account.png)

Once you filled the informations, click on REGISTER A NEW ACCOUNT, and then go back to login page, and do login.

In the left side menu, click on tree points icon, and then click on **Administration** option.

After that, click on **Users** option. It will appear a right side bar, having the '+' button. Click on this button and fill the informations according to the following image. The name of bot can be modified, but must be used the user and password that are defined on ROCKETCHAT_USER and ROCKETCHAT_PASSWORD variables, on `production.yml` file. By default, the user and password are `botnat` and `botnatpass`, respectively.

To add the role to bot, click the option **Select a Role**, select bot and click on **ADD ROLE** option. Then click on **Save**.

![Adding bot tutorial](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/adding_bot.png)

Now you are ready to talk to the bot using the channels, or using @botnat before the message.

### Livechat

The Livechat allows a feature of a window that can be integrated to other pages. To activate it, you must access again the **Administration** option, by clicking on three points icon, on the left side menu. Then click on **Livechat** option.

![Livechat option on adm menu](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/livechat_sidebar.png)

On the next screen, mark the **Livechat enabled** option as True, and the **Show pre-registration form** option as False, in order to not be asked for email and password when using chat. Click then in **SAVE CHANGES**.

![Livechat activation screen](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/active_livechat.png)

Close the left side menu, and click on three points icon. Select the **Livechat** option.

![Livechat option](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/livechat_option.png)

At the right side menu, select the **User Management** option. You must add the bot as an agent, so search for botnat, then click in **ADD**.

![Adding bot as agent](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/add_agent.png)

Now it is necessary to create an department. On the left side menu, click on **Departments**, and then click in **NEW DEPARTMENT**.

![Adding bot as agent](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/new_department.png)

On the next screen, write a name and a description for the department and add the bot by selecting him on **Available agents**. Then click on **Save** option.

![Create new department](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/add_agent_to_department.png)

On the left side menu, click at **Installation**. Now you only need to copy and paste the code on your site, where you want to integrate the conversation window.

![Installation code](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/installation.png)

After integrating the code to your site, a window like the one showed in the image should be available, and ready to use.

![Livechat window](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/livechat_en.png)

#### Welcome message on Livechat

To fire a welcome message can be used **Triggers**. A **Trigger** fire an action according to a condition. A condition can be the user accessing an URL, or the time user stay on site. The action, in this case, is the welcome message send.

To add a **trigger** to Livechat, on the left side menu, click on **Triggers** option. Then mark the option **Enabled** as **Yes**, and fill the trigger name and description. In case of the firing critery is the user entering a URL, then choose the option **Visitor page URL** on **Condition** field, and on the side field write the desired URL.
Select the option **Send a message** at field **Action**, type the bot name(**botnat**) and the welcome message. After all, click on **Save**.

![Livechat Trigger URL](https://gitlab.com/lappis-unb/projects/minc/rouanet-bot/wikis/images/trigger_url.png)

## Updating the YAML


To read more information about the YAML structure and how to modify it, access the [Hubot-Natural README](https://github.com/RocketChat/hubot-natural/blob/master/README.md).
