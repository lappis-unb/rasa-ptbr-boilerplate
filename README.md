# Hubot Natural

[![Build Status](https://travis-ci.org/RocketChat/hubot-natural.svg?branch=master)](https://travis-ci.org/RocketChat/hubot-natural)

## Natural Language ChatBot

Hubot is one of the most famous bot creating framework on the web, that's because github made it easy to create. If you can define your commands in a RegExp param, basically you can do anything with Hubot. That's a great contribution to ChatOps culture.

Inspired by that, we wanted to provide the same simplicity to our community to develop chatbots that can actually process natural language and execute tasks, as easy as building RegExp oriented bots.

So, we've found a really charming project to initiate from, the [Digital Ocean's Heartbot](https://github.com/digitalocean/heartbot) _a shot of love to for your favorite chat client_ =)

Based on Heartbot, we introduced some NLP power from [NaturalNode](https://github.com/NaturalNode/natural) team, an impressive collections of Natural Language Processing libs made to be used in NodeJS.

And so, the _magic_ happens...

Welcome to *HubotNatural*, a new an exciting chatbot framework based in Hubot and NaturalNode libs, with an simple and extensible architecture designed by Digital Ocean's HeartBot Team, made with love and care by Rocket.Chat Team.  

We hope you enjoy the project and find some time to contribute.  

## How it Works

HubotNatural is made to be easy to train and extend. So what you have to understand basically is that it has an YAML corpus, where you can design your chatbot interactions using nothing but YAML's notation.

All YAML interactions designed in corpus can have it's own parameters, which will be processed by an event class.

Event classes give the possibility to extend HubotNatural. By writing your own event classes you can give your chatbot the skills to interact with any services you need.

### YAML corpus

The YAML file is loaded in `scripts/index.js`, parsed and passed to chatbot bind, which will be found in `scripts/bot/index.js`, the cortex of the bot, where all information flux and control are programmed.

The YAML corpus is located in `training_data/corpus.yml` and it's basic structure looks like this:  

```yaml
trust: .85
interactions:
  - name: salutation
    expect:
      - hi there
      - hello everyone
      - what's up bot
      - good morning
    answer:
      - - Hello there $user, how are you?
        - Glad to be here...
      - Hey there, nice to see you!
    event: respond
```

What this syntax means:

- `trust`: the minimum level of certain that must be returned by the classifier in order to run this interaction. Value is 0 to 1 (0% to 100%). If a classifier returns a value of certainty minor than `trust`, the bots responds with and error interaction node.  
- `interactions`: An vector with lots of interaction nodes that will be parsed. Every interaction designed to your chatbot must be under an interaction.node object structure.
- `name`: that's the unique name of the interaction by which it will be identified. Do not create more than one interaction with the same `node.name` attribute.  
- `expect`: Those are the sentences that will be given to the bots training. They can be strings or keywords vectors, like `['consume','use']`.   
- `answer`: the messages that will be sent to the user, if the classifiers get classified above the trust level. The `node.message` will be parsed and sent by event class. In order to use multiline strings inside your YAML, you must follow the [YAML Multiline Strings](http://yaml-multiline.info/) syntax. You can specify variables in message. By default HubotNatural comes with `$user`, `$bot` and `$room` variables.
- `event`: is the name of the CoffeeScript or JavaScript Class inside `scripts/events`, without the file extension.

### Event Coffee Classes

Event classes can be written to extend the chatbot skills. They receives the interaction object and parse the message, like this:  

```yaml
class respond
  constructor: (@interaction) ->
  process: (msg) =>
    sendMessages(stringElseRandomKey(@interaction.answer), msg)

module.exports = respond
```

It's base constructor is the `@interaction` node so you can have access to all attributes inside an interaction just using `@interaction.attribute`. Here you can parse texts, call APIs, read files, access databases, and everything else you need.  
You may want to use the function `stringElseRandomKey` to get a random element of a list, if it's parameter is a list, and use the function `sendMessages` to send messages to an user.

#### Logistic Regression Classifier

The NaturalNode library comes with two kinds of classifiers, the Naive Bayes classifier known as the `BayesClassifier` and the `LogisticRegressionClassifier` functions. By default, HubotNatural uses the `LogisticRegressionClassifier`. It just came with better results in our tests.

#### PorterStemmer

There is also more than one kind of stemmer. You should set the stemmer to define your language. By default we use the PorterStemmerPt for portuguese, but you can find english, russian, italian, french, spanish and other stemmers in NaturalNode libs, or even write your own based on those.

Just check inside `node_modules/natural/lib/natural/stemmers/`.

To change the stemmers language, just set the environment variable `HUBOT_LANG` as `pt`, `en`, `es`, and any other language termination that corresponds to a stemmer file inside the above directory.

## Deploy with Docker

We have a Dockerfile that builds a lightweight image based in Linux Alpine with all the repository content so you can upload that image to a docker registry and deploy your chatbot from there.

You also can use `docker-compose.yml` file to load a local instance of Rocket.Chat, MongoDB and HubotNatural services, where you can change the parameters if you must.

The docker-compose file looks like this:

```yaml
version: '2'

services:
  rocketchat:
    image: rocketchat/rocket.chat:latest
    restart: unless-stopped
    volumes:
      - ./uploads:/app/uploads
    environment:
      - PORT=3000
      - ROOT_URL=http://localhost:3000
      - MONGO_URL=mongodb://mongo:27017/rocketchat
      - MONGO_OPLOG_URL=mongodb://mongo:27017/local
      - MAIL_URL=smtp://smtp.email
#       - HTTP_PROXY=http://proxy.domain.com
#       - HTTPS_PROXY=http://proxy.domain.com
    depends_on:
      - mongo
    ports:
      - 3000:3000

  mongo:
    image: mongo:3.2
    restart: unless-stopped
    volumes:
     - ./data/db:/data/db
     #- ./data/dump:/dump
    command: mongod --smallfiles --oplogSize 128 --replSet rs0

  mongo-init-replica:
    image: mongo:3.2
    command: 'mongo mongo/rocketchat --eval "rs.initiate({ _id: ''rs0'', members: [ { _id: 0, host: ''localhost:27017'' } ]})"'
    depends_on:
      - mongo

  hubot-natural:
    build: .
    restart: unless-stopped
    environment:
      - HUBOT_ADAPTER=rocketchat
      - HUBOT_NAME='Hubot Natural'
      - HUBOT_OWNER=RocketChat
      - HUBOT_DESCRIPTION='Hubot natural language processing'
      - HUBOT_LOG_LEVEL=debug
      - HUBOT_CORPUS=corpus.yml
      - HUBOT_LANG=pt
      - RESPOND_TO_DM=true
      - RESPOND_TO_LIVECHAT=true
      - RESPOND_TO_EDITED=true
      - LISTEN_ON_ALL_PUBLIC=false
      - ROCKETCHAT_AUTH=password
      - ROCKETCHAT_URL=rocketchat:3000
      - ROCKETCHAT_ROOM=GENERAL
      - ROCKETCHAT_USER=botnat
      - ROCKETCHAT_PASSWORD=botnatpass
      - HUBOT_NATURAL_DEBUG_MODE=true
    volumes:
      - ./scripts:/home/hubotnat/bot/scripts
      - ./training_data:/home/hubotnat/bot/training_data
    depends_on:
      - rocketchat
    ports:
      - 3001:8080
```

You can change the attributes of variables and volumes to your specific needs and run `docker-compose up` in terminal to start the rocketchat service at `http://localhost:3000`.
*ATTENTION:* You must remember that hubot must have a real rocketchat user created to login with. So by the first time you run this, you must first go into rocketchat and create a new user for hubot, change the `ROCKETCHAT_USER` and `ROCKETCHAT_PASSWORD` variables in the docker-compose.yml file, and then reload the services using `docker-compose stop && docker-compose up` to start it all over again.

If you want to run only the hubot-natural service to connect an already running instance of Rocket.Chat, you just need to remember to set the `ROCKETCHAT_URL` to a correct value, like `https://open.rocket.chat`.

## Deploy with Hubot

To deploy HubotNatural, first you have to install yo hubot-generator:

```shell
npm install -g yo generator-hubot
```

Then you will clone HubotNatural repository:  

```shell
git clone https://github.com/RocketChat/hubot-natural.git mybot
```

Change 'mybot' in the git clone command above to whatever your bot's name will be, and install hubot binaries, without overwitting any of the files inside the folder:

```shell
cd mybot
npm install
yo hubot

                     _____________________________
                    /                             \
   //\              |      Extracting input for    |
  ////\    _____    |   self-replication process   |
 //////\  /_____\   \                             /
 ======= |[^_/\_]|   /----------------------------
  |   | _|___@@__|__
  +===+/  ///     \_\
   | |_\ /// HUBOT/\\
   |___/\//      /  \\
         \      /   +---+
          \____/    |   |
           | //|    +===+
            \//      |xx|

? Owner Diego <diego.dorgam@rocket.chat>
? Bot name mybot
? Description A simple helpful chatbot for your Company
? Bot adapter rocketchat
   create bin/hubot
   create bin/hubot.cmd
 conflict Procfile
? Overwrite Procfile? do not overwrite
     skip Procfile
 conflict README.md
? Overwrite README.md? do not overwrite
     skip README.md
   create external-scripts.json
   create hubot-scripts.json
 conflict .gitignore
? Overwrite .gitignore? do not overwrite
     skip .gitignore
 conflict package.json
? Overwrite package.json? do not overwrite
     skip package.json
   create scripts/example.coffee
   create .editorconfig
```

Now, to run your chatbot in shell, you should run:  

```shell
bin/hubot
```

wait a minute for the loading process, and then you can talk to mybot.

Take a look to adapters to run your bot in other platafforms.

## Env Variables:

In your terminal window, run:

```shell
export HUBOT_ADAPTER=rocketchat
export HUBOT_OWNER=RocketChat
export HUBOT_NAME='Bot Name'
export HUBOT_DESCRIPTION='Description of your bot'
export ROCKETCHAT_URL=https://open.rocket.chat
export ROCKETCHAT_ROOM=GENERAL
export LISTEN_ON_ALL_PUBLIC=false
export RESPOND_TO_DM=true
export RESPOND_TO_LIVECHAT=true
export ROCKETCHAT_USER=catbot
export ROCKETCHAT_PASSWORD='bot password'
export ROCKETCHAT_AUTH=password
export HUBOT_LOG_LEVEL=debug
export HUBOT_CORPUS='corpus.yml'
export HUBOT_LANG='en'
bin/hubot -a rocketchat --name $HUBOT_NAME
```  

You can check [hubot-rocketchat](https://github.com/RocketChat/hubot-rocketchat) adapter project for more details.

### PM2 Json File

As NodeJS developers we learned to love [Process Manager PM2](http://pm2.keymetrics.io), and we really encourage you to use it.

```shell
npm install pm2 -g
```

Create a `mybot.json` file and jut set it's content as:  

```json
{
	"apps": [{
		"name": "mybot",
		"interpreter": "/bin/bash",
		"watch": true,
		"ignore_watch" : ["client/img"],
		"script": "bin/hubot",
		"args": "-a rocketchat",
		"port": "3001",
		"env": {
			"ROCKETCHAT_URL": "https://localhost:3000",
			"ROCKETCHAT_ROOM": "general",
			"RESPOND_TO_DM": true,
			"ROCKETCHAT_USER": "mybot",
			"ROCKETCHAT_PASSWORD": "12345",
			"ROCKETCHAT_AUTH": "password",
			"HUBOT_LOG_LEVEL": "debug"
		}
	}
]
}
```

You can also instantiate more than one process with PM2, if you want for example to run more than one instance of your bot:  

```json
{
	"apps": [{
		"name": "mybot.0",
		"interpreter": "/bin/bash",
		"watch": true,
		"ignore_watch" : ["client/img"],
		"script": "bin/hubot",
		"args": "-a rocketchat",
		"port": "3001",
		"env": {
			"ROCKETCHAT_URL": "https://localhost:3000",
			"ROCKETCHAT_ROOM": "general",
			"RESPOND_TO_DM": true,
			"ROCKETCHAT_USER": "mybot",
			"ROCKETCHAT_PASSWORD": "12345",
			"ROCKETCHAT_AUTH": "password",
			"HUBOT_LOG_LEVEL": "debug"
		}
	}, {
		"name": "mybot.1",
		"interpreter": "/bin/bash",
		"watch": true,
		"ignore_watch" : ["client/img"],
		"script": "bin/hubot",
		"args": "-a rocketchat",
		"port": "3002",
		"env": {
			"ROCKETCHAT_URL": "https://mycompany.rocket.chat",
			"ROCKETCHAT_ROOM": "general",
			"RESPOND_TO_DM": true,
			"ROCKETCHAT_USER": "mybot",
			"ROCKETCHAT_PASSWORD": "12345",
			"ROCKETCHAT_AUTH": "password",
			"HUBOT_LOG_LEVEL": "debug"
		}
	}
]
}
```

And of course, you can go nuts setting configs for different plataforms, like facebook mensenger, twitter or telegram ;P.

## Hubot Adapters

Hubot comes with at least 38 adapters, including Rocket.Chat addapter of course.  
To connect to your Rocket.Chat instance, you can set env variables, our config pm2 json file.

Checkout other [hubot adapters](https://github.com/github/hubot/blob/master/docs/adapters.md) for more info.

## Thanks to

In Rocket.Chat we are so in love by what we do that we couldn't forget to thanks everyone that made it possible!

### Github Hubot Team

Thanks guys for this amazing framework, hubots lives in the heart of Rocket.Chat, and we recommend everyone to checkout https://hubot.github.com and find much much more about hubot!

### Natural Node Project

To the NaturalNode Team our most sincere "THAK YOU VERY MUCH!! We loved your project and we are excited to contribute!".  
Checkout https://github.com/NaturalNode/natural and let your mind blow!

### Digital Ocean's Heartbot

We can not thanks Digital Ocean enough, not only for this beautifull [HeartBot project](https://github.com/digitalocean/heartbot), but also for all the great tutorials and all the contributions to OpenSource moviment.

### Thanks to Our Community

And for last but not least, thanks to our big community of contributors, testers, users, partners, and everybody who loves Rocket.Chat and made all this possible.
