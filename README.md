```
                                       _   _ _ 
 ___ _ __ ___   __ _ _ __  _ __  _   _| |_(_) |
/ __| '_ ` _ \ / _` | '_ \| '_ \| | | | __| | |
\__ \ | | | | | (_| | |_) | |_) | |_| | |_| | |
|___/_| |_| |_|\__,_| .__/| .__/ \__,_|\__|_|_|
                    |_|   |_|
```

⚙ smapputil that contains utility scripts in python, bash or javascript. Javascript run here will be of the variety node.js 5.0.0. Python is generally python 2.7.11 moving to python 3. Shellscript/bash is expected to be in bash 3.2. A lot of the code here are refined, modularized, improved versions of scripts that used to be in Sandbox and smappPy.

- [py](https://github.com/SMAPPNYU/smapputil#py)
    - [merge_bson](https://github.com/SMAPPNYU/smapputil#merge_bson)
    - [merge_json](https://github.com/SMAPPNYU/smapputil#merge_json)
    - [csv_to_json](https://github.com/SMAPPNYU/smapputil#csv_to_json)
    - [date_filter_bson](https://github.com/SMAPPNYU/smapputil#date_filter_bson)
    - [list_collections](https://github.com/SMAPPNYU/smapputil#list_collections)
    - [query_user_tweets](https://github.com/SMAPPNYU/smapputil#query_user_tweets)
    - [query_search_tweets](https://github.com/SMAPPNYU/smapputil#query_search_tweets)
    - [query_user_objects](https://github.com/SMAPPNYU/smapputil#query_user_objects)
    - [transfer_collection](https://github.com/SMAPPNYU/smapputil#transfer_collection)
    - [ssh_tunnel](https://github.com/SMAPPNYU/smapputil#ssh_tunnel)
    - [rotating_tunnel](https://github.com/SMAPPNYU/smapputil#rotating_tunnel)
    - [mail_tweet_counts](https://github.com/SMAPPNYU/smapputil#mail_tweet_counts)
    - [username_id_convert](https://github.com/SMAPPNYU/smapputil#username_id_convert)
- [js](https://github.com/SMAPPNYU/smapputil#js)
    - [adduserstomongo](https://github.com/SMAPPNYU/smapputil#adduserstomongo)
- [sh](https://github.com/SMAPPNYU/smapputil#sh)
    - [hades_rotating_tunnel](https://github.com/SMAPPNYU/smapputil#hades_rotating_tunnel)
    - [kill_hades_rotating_tunnel](https://github.com/SMAPPNYU/smapputil#kill_hades_rotating_tunnel)
    - [logger](https://github.com/SMAPPNYU/smapputil#logger)
    - [clear_history](https://github.com/SMAPPNYU/smapputil#clear_history)

#logging

Logging is required on all scripts. A few reasons:

1. Easier to spot and identify bugs while performing daily tasks
2. Easier to debug the immediate problem and deliver, bugs are never expected but they always happen.
3. By default the logs go into a folder path at ~/pylogs ~/shlogs or ~/jslogs with the name of the script and the date it was run.

I recommend creating these log folders in your home directory `pylogs` `jslogs` `shlogs`. Scripts with no logging will not be allowed into the repository.

mkdir ~/pylogs ~/jslogs ~/shlogs

That said you can specify whatever log path  you want. Just know that you must have one.

[Python Logging Example](https://github.com/SMAPPNYU/smapputilities/blob/master/py/merge_bson/merge_bson.py)

[Javascript Logging Software w/ Examples](https://github.com/trentm/node-bunyan)

[Bash Logging Example]() 

#tests

You must write tests for every function in every script. Whenever you add a new script you need to run your unit tests. Scripts with no tests will not be allowed into the repository. 

[Python Testing Framework (unittest)](http://docs.python-guide.org/en/latest/writing/tests/)

[Python Testing Tutorial](http://docs.python-guide.org/en/latest/writing/tests/)

[Bash Testing Framework (shunit2)](https://shunit2.googlecode.com/svn/trunk/source/2.1/doc/shunit2.html)

[Bash Testing Tutorial](https://wiki.umn.edu/UmmCSci3401f09/VerySimpleExampleOfShellScriptingAndTestingWithShunit2)

[Javascript Testing Framework/ Test Runner (mocha)](http://mochajs.org/)

[The co-wrapper for mocha](https://github.com/blakeembrey/co-mocha)

[The chai assertion library](http://chaijs.com/)

[Chai cheat sheet](http://ricostacruz.com/cheatsheets/chai.html)

[Javascript Testing Example](https://github.com/SMAPPNYU/smapputilities/blob/master/js/mailtweetcounts/test/test_mailtweetcounts.js)

#py

python utilities / scripts that do useful things. Built in python 2.7.X. To ru nthe python scripts I suggest activating the scriptsenv virtual environment with `source scriptsenv/bin/activate`. You should see a `(scriptsenv)` appear at the beginning of your consode prompt. (you can deactivate by typing `deactivate` anytime)

environment.yml - for anaconda users to be able to create an environment easily, installs things from pip. to replicate the environment run `conda env create -f environment.yml` or simply `conda env create` in the `py` directory. [see this page.](http://conda.pydata.org/docs/using/envs.html#export-the-environment-file)
requirements.txt - a file containing dependencies smapputilities needs

#tests:

to test your scripts create a file called `test_NAME_OF_YOUR_SCRIPT.py` following the format of files like [test_date_filter.py](https://github.com/SMAPPNYU/smapputilities/blob/master/py/test/test_date_filter.py) then run `python test/test_NAME_OF_YOUR_SCRIPT.py`

#resources:

[Python Unit Test Framework](https://docs.python.org/2/library/unittest.html#assert-methods)

[Adding imports to python sys path](http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath/471168)

#[merge_bson](https://github.com/SMAPPNYU/smapputilities/blob/master/py/merge_bson)

takes arbitrary number of bson files and merges them.

abstract:
```python
/path/to/scriptsvenv/bin/python merge_bson.py -i /path/to/bson1.bson /path/to/bson2.bson -o /path/to/output.bson -l /path/to/log.log
```

practical:
```python
python merge_bson.py -i ~/bson1.bson ~/bson2.bson -o ~/output.bson -l ~/log.log
# or if you want to ensure a unique field
python merge_bson.py -i ~/bson1.bson ~/bson2.bson -o ~/output.bson -l ~/log.log -f '_id'
```

*returns* a bson file that writes to disk in the output.

test: `python -m unittest test.test_merge_bson`

#[ssh_tunnel](https://github.com/SMAPPNYU/smapputil/tree/master/py/ssh_tunnel)

creates an ssh tunnel.

abstract:
```python
python py/ssh_tunnel/ssh_tunnel.py -lo LOGIN_HOST -u LOGIN_USERNAME -p LOGIN_PASSWORD -rh REMOTE_HOST -rp REMOTE_PORT -lh localhost -lp LOCAL_PORT
```

practical:
```python
python py/ssh_tunnel/ssh_tunnel.py -lo hpc.nyu.edu -u LOGIN_USERNAME -p LOGIN_PASSWORD -rh REMOTE_HOST -rp 27017 -lp 27017
# or in a script
from ssh_tunnel import start_ssh_tunnel, stop_ssh_tunnel

ssh_tunnel.start_ssh_tunnel(args.loginhost, args.username, args.password, args.localhost, args.localport, args.remotehost, args.remoteport)
```

`-lh` is optional

*returns* an ssh tunnel

test: `python test/test_ssh_tunnel LOGIN_USER LOGIN_PASSWORD`


#[rotating_tunnel](https://github.com/SMAPPNYU/smapputil/tree/master/py/rotating_tunnel)

*not ready*

creates a keyed login only rotating tunnel. less general than ssh_tunnel, rotates the tunnels among
login nodes and remote ports provided in input.

abstract:
```python
python py/ssh_tunnel/rotating_tunnel.py -rh REMOTE_HOST -rp REMOTE_PORT -lh localhost -lp LOCAL_PORT
```

practical:
```python
python py/ssh_tunnel/rotating_tunnel.py -rh REMOTE_HOST -rp REMOTE_PORT -lh localhost -lp LOCAL_PORT

```

*returns* a tunnel that maps yous local ports to a rotating set of remote ports and hosts

*input* a file that contains a set of login hosts and a set of remotehosts

```
{
    "loginhosts":[
        {
            "host":"host1",
            "user":"user1"
        },
        {
            "host":"host2",
            "user":"user2"
        }
    ],
    "remotehosts":[
        {
            "host":"host3",
            "user":"user3"
        },
        {
            "host":"host4",
            "user":"user4"
        }
    ]
}
```

note: if using the tunnel to connect to nyu bastion host contact the sys admin there to add your public keys to the authorized_hosts file for your account on that machine.

#[merge_json](https://github.com/SMAPPNYU/smapputilities/blob/master/py/merge_json)

merges two files where each file has a json object on each line, or each file i a list of json objects

abstract:
```python
python merge_json.py -i /path/to/json1.json /path/to/json2.json -o /path/to/output.json -l /path/to/log.log
```

practical:
```python
python merge_json.py -i ~/json1.json ~/json2.json -o ~/output.json -l ~/merge_json_log.log
# or if you want to ensure a unique field
python merge_json_unique.py -i ~/json1.json ~/json2.json -o ~/output.json -l ~/merge_json_log.log -f '_id'
# or with flags
python merge_json_unique.py -i ~/json1.json ~/json2.json -o ~/output.json -l ~/merge_json_log.log --jsonload --jsonlist
```

*returns* a json file that writes to disk with the original input files merged

test: `python -m unittest test.test_merge_json`

`--jsonload`: loads input files as entire json objects, not line by line (useful for a jsonlist input or file w/ one object spaced over multiple lines)

`--jsonlist`: outputs a json list instead of a json object on each line

#[csv_to_json](https://github.com/SMAPPNYU/smapputilities/tree/master/py/csv_to_json)

take a csv and make it into a json file or a json list

abstract:
```python
python csv_to_json.py -i /path/to/csv1.csv /path/to/csv2.json -o /path/to/output.json -l /path/to/log.log
```

practical:
```python
python csv_to_json.py -i ~/csv1.csv ~/csv2.csv -o ~/output.json -l ~/csv_to_json.log
# or if you want the output as a json list
python csv_to_json.py -i ~/csv1.csv ~/csv2.csv -o ~/output.json -l ~/csv_to_json.log --jsonlist
# or if you want to skip the header
python csv_to_json.py -i ~/csv1.csv ~/csv2.csv -o ~/output.json -l ~/csv_to_json.log --skipheader
```

*returns* a json file that has a json object on each line or it returns a json list file.

test: `python -m unittest test.test_csv_to_json`

`--skipheader`: skips the first line of every input file

`--jsonlist`: outputs a json list instead of a json object on each line

#[date_filter_bson](https://github.com/SMAPPNYU/smapputilities/blob/master/py/date_filter/date_filter_bson.py)

Uses the [smapp-toolkit](https://github.com/SMAPPNYU/smapp-toolkit) to filter by date.

Make sure to convert between UTC and EST (or wtvr time zone you're in). Use this [site.](http://www.wsanford.com/~wsanford/exo/TCT.html)

Ex:

`2016-01-17 09:00:00 PM EST` to `2016-01-17 11:00:00 PM PM EST`

goes to

`2016-01-18 02:00:00 AM UTC` to `2016-01-18 04:00:00 AM UTC`

Takes two date times of format `2016-01-19 09:47:00` and produces a new bson file filtered by the date we want. A quick trick is add 5 hours to new york time (eastern standard time) to get the right time/date in utc. Do not forget to roll over the day.

abstract:
```python
/path/to/scriptsvenv/bin/python date_filter_bson.py -i /path/to/bson1.bson -d1 '2016-01-18 02:00:00' -d2 '2016-01-18 04:00:00' -o /path/to/output.bson -l /path/to/log.log
```
practical:
```python
python date_filter_bson.py -i ~/bson1.bson -d1 '2016-01-18 02:00:00' -d2 '2016-01-18 04:00:00' -o ~/output.bson -l ~/log.log
```

`d1` the first date (applied via [since](https://github.com/SMAPPNYU/smapp-toolkit#since) in the smapp-toolkit)

`d2` the second date (applied via [until](https://github.com/SMAPPNYU/smapp-toolkit#until) in smapp-toolkit)

*returns* a bson file that writes to disk. Filtered by the dates given.

test: `python test/test_date_filter.py`

#[list_collections](https://github.com/SMAPPNYU/smapputilities/tree/master/py/list_collections)

a way to list the running collections on a machine by logging in and listing that machine's crontab, would be nice to add a name field to the script input and output files, would also be nice to have the number per machine running.

abrstact:
```python
/path/to/scripts/env/bin/python /path/to/list_collections.py -i ~/serverlist.csv -o ~/pylogs/collections.json 
```

practical:
```python
python ~/smapputilities/py/list_collections/list_collections.py -i ~/serverlist.json -o ~/pylogs/collections.json 
```

*inputs* a csv or json file that is a list of ip addresses or severnames

csv should look like so:
```txt
sever1,user1
server2,user2
```
json should look like:
```json
{
    'server_one': 'user_one',
    'server_two': 'user_two'
}
```

*returns* a json file with servernames as keys and a list of collections as the value for each key

note: logging is only used for errors and paramiko automatically taps into our logger.

note: make sure you have `~/pylogs` directory before running this script.

test: `python test/test_list_collections.py SERVER_IP_OR_NAME SERVER_USERNAME`

#[query_user_tweets](https://github.com/SMAPPNYU/smapputilities/blob/master/py/query_twitter/query_user_tweets.py)

take a list of users and get each of their 3200 most recent tweets. Works on the twitter api with tweepy.

abstract:
```python
/path/to/scriptsenv/bin/python query_user_tweets.py -i /path/to/input.json -o /path/to/output.json -a /path/to/auth.json -l /path/to/log.log
```

practical:
```python
python query_user_tweets.py -i ~/input.json -o ~/output.json -a ~/auth.json -l ~/log.log
```

*returns* a json file that writes to disk, with the 3200 (or less) of a user's most recent tweets.

note: input is json or csv, csv must be a one column csv with `id_str` as the column, json is just a json list ['id_one', 'id_two']

note: `smapp_count` term added to each tweet object to tell you which count of a particular user's tweets you are looking at.

#[query_search_tweets](https://github.com/SMAPPNYU/smapputilities/blob/master/py/query_twitter/query_search_tweets.py)

queries the twitter search api for any list of terms.

abstract:
```python
/path/to/scriptsenv/bin/python query_search_tweets.py -i /path/to/input.json -o /path/to/output.json -a /path/to/auth.json -l /path/to/log.log
```

practical:
```python
python query_search_tweets.py -i ~/input.json -o ~/output.json -a ~/auth.json -l ~/log.log
```

*returns* a json file that writes to disk with the resulting tweet objects in JSON format

note: fields `smapp_term` and `smapp_count` are added to each tweet object to tell you which term the tweet war queried for and what its count in the query was.

note: input is json or csv, csv must be a one column csv with `id_str` as the column, json is just a json list ['id_one', 'id_two']

#[query_user_objects](https://github.com/SMAPPNYU/smapputilities/blob/master/py/query_twitter/query_user_objects.py)

queries the twitter api for any list of user objects. takes a list of twitter user ids as input.

abstract:
```python
/path/to/scriptsenv/bin/python query_user_objects.py -i /path/to/input.json -o /path/to/output.json -a /path/to/auth.json -l /path/to/log.log
```

practical:
```python
python query_user_objects.py -i ~/input.json -o ~/output.json -a ~/auth.json -l ~/log.log
```

*returns* a json file that writes to disk with the resulting user objects in JSON format

note: input is json or csv, csv must be a one column csv with `id_str` as the column, json is just a json list ['id_one', 'id_two']

#[transfer_collection](https://github.com/SMAPPNYU/smapputilities/tree/master/py/transfer_collection)

transfers a smapp tweet collection from one db to another. updating all necessary metadata documents.

abstract:
```python
/path/to/scripts/env/bin/python /path/to/transfer_collection.py -s SOURCE_HOST -p SOURCE_HOST_PORT -u SOURCE_USERNAME -w SOURCE_USER_PASSOWRD -d SOURCE_DB_NAME -ts TARGET_HOST -tp TARGET_HOST_PORT -tu TARGET_USERNAME -tw TARGET_USER_PASSWORD -td TARGET_DB_NAME -au AUTHENTICATION_USER -aw AUTHENTICATION_USER_PASSWORD -adb AUTHENTICATION_DATABASE
```

practical:
```python
~/pyenvs/bin/python ~/smapputilities/py/transfer_collection/transfer_collection.py -s localhost -p 27017 -u db_user -w supersecret_pwd -d germany_election -ts foreign.host.org -tp 27017 -tu foreign_usr -tw foreign_usr_secret_pwd5 -td new_germany_election -au auth_user_Admin_of_some_kind -aw super_secret_yo -adb admin
```

*returns* nothing but instead transfers data fro one running mongo instance to another

note: requires at least mongo 3.0

#[mail_tweet_counts](https://github.com/SMAPPNYU/smapputilities/tree/master/py/mail_tweet_counts)

mails tweet counts daily from our db

abstract:
```python
python py/mail_tweet_counts/mail_tweet_counts.py -ho HOSTNAME -p PORT
```

practical:
```python
python py/mail_tweet_counts/mail_tweet_counts.py -ho localhost -p 27017
```

*returns* an email to the specified address with the tweet counts in the db.

needs config.py that looks like so in mail_tweet_counts dir:

```
config = \
{ \
    'ignore_dbs': ['admin', 'config', 'test', 'EgyptToleranceUsersNetworks', 'OWSUsers', 'FilterCriteriaAdmin'], \
    'ignore_collections':['tweets_limits', 'tweets_filter_criteria', 'system.indexes', 'smapp_metadata', 'tweets_deletes'], \
    'mail': {
        'toemail': 'email',
        'gmailuser': 'smappmonitor@gmail.com', \
        'gmailpass': 'PWD' \
    } \
}
```

#[username_id_convert](https://github.com/SMAPPNYU/smapputilities/tree/master/py/username_id_convert)

convert twitter ids to usernames and vice versa.

abstract:
```python
python py/username_id_convert/username_id_convert.py -op OPERATION -i PATH/TO/INPUT.JSON -o PATH/TO/OUTPUT.json -a PATH/TO/OAUTH.json
```

practical:
```python
python py/username_id_convert/username_id_convert.py -op users_ids -i py/test/test_handles.csv -o ~/pylogs/username_id_convert_output_2.json -a ~/misc/oauthpools/pool.json
```

OPERATION - ids_users, users_ids

*returns* a json file with a json object on each line.

takes a json 
```
[
22997097, 14281853, 20686582, 19977542
]
```


or csv input:

```
screen_name
mcdonald4avalon
jeannie4avalon
lbarnettavalon
ScottAndrewsNL
Jenn_McCreath
judyfootemp
teejohnny
Scott_Simms
ClaudetteNDP
YvonneJJones
EdwardNDP
PeterPenashue
Gudie
```



#js

javascript scripts that perform useful tasks that we can run. It was built for node v5.X.X. All js code should adhere to [js standard code style](https://github.com/feross/standard). so far i'm using js scripts fo mongo operations that need good async and are difficult to replicate in python 


For a fresh install:

```
sudo apt-get purge nodejs*
sudo apt-get remove nodejs
wget -qO- https://deb.nodesource.com/setup_5.x | sudo bash -
sudo apt-get install --yes nodejs
```

Your node install can now be run to check version like so: `nodejs --version`. As of this writing node.js is on version 5.X, just replace the 5.X with 6.X or wtvr version you're looking for. Do not use node.js versions 0.X they are being phased out.

[How to install node.js on Linux](http://askubuntu.com/questions/672994/how-to-install-nodejs-4-on-ubuntu-15-04-64-bit-edition)

Respources:

[Package / Dependencies](http://blog.nodejitsu.com/package-dependencies-done-right/)
[Beginner Guide](http://blog.modulus.io/absolute-beginners-guide-to-nodejs)
[How to install node via homebrew](https://changelog.com/install-node-js-with-homebrew-on-os-x/)

Generators / Pormises / Co Resources:

[promises explanation](http://www.mattgreer.org/articles/promises-in-wicked-detail/)

[explanation](http://stackoverflow.com/questions/23099855/koa-co-bluebird-or-q-generators-promises-thunks-interplay-node-js)

[co tutorial](https://medium.com/@tjholowaychuk/callbacks-vs-coroutines-174f1fe66127#.d1cud742h)

[co libraries](https://github.com/tj/co/wiki)

[js generators reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator)

[js promises + generators](https://www.promisejs.org/generators/)

[js promises tutorial](http://alexperry.io/node/2015/03/25/promises-in-node.html)

[js generators tutorial](http://www.sitepoint.com/javascript-generators-preventing-callback-hell/)

[js promises chaetsheet](http://ricostacruz.com/cheatsheets/bluebird.html)

#[adduserstomongo](https://github.com/SMAPPNYU/smapputilities/tree/master/js/adduserstomongo)

adds a set of specified users to specified databases running on a mongodb instance

useful for:

adding a user safely. 
mass addind users to every db, normally a tedious task.


Abstract:
```javascript
node /path/to/adduserstomongo.js
```

Practical:
```javascript
node ~/smapp-repositories/smapputilities/js/adduserstomongo/adduserstomongo.js
```

the structure of the config file `smapputilities/js/adduserstomongo/adduserstomongoconfig.js` is:
```
{
    mongo: {
        mongotest:  'mongodb://USER_ON_TEST_DB:USER_ON_TEST_PASSWORD@SERVER:PORT/test',
        mongoanydb: 'mongodb://READONLY_SINGLEDB_USER:READONLY_SINGLEDB_PASS@SERVER:PORT/',
        existingtestuser: {
            name:'USER_ON_TEST_DB', 
            pass:'PASSWORD'
        }
    },
    addusers: [
        {name: 'USER_NAME', pass: 'PASS_WORD', roles:['read']},
        {name: 'USER_NAME', pass: 'PASS_WORD', roles: ['readWrite']},
    ]
    dbs: [
    'DB_NAME_ONE'
    'DB_NAME_TWO'
    .
    .
    .
    'DB_NAME_THIRTY'
    'DB_NAME_THIRTYONE'
    'DB_NAME_THIRTYTWO'
    ]
}
```

*Returns* nothing really, it updates the databses you list on the smapputilitiesconfig.js file 

Test: 

`npm install -g mocha`

then

run `mocha` in `smapputilities/js/adduserstomongo/`

#sh 

bash utilities / scripts that do useful thngs. Built in bash 3.2.X. You may notice many of the scripts are clones of scripts in [shellscripts repo](https://github.com/SMAPPNYU/shellscripts). This is temporary. Their final reting place will be here. The difference will be modularized testing, modularized scripts, each script will get its own tests (instead of the single file), the tests will be unit tests and as little as porrible system state tests, etc. As soon as the move is done and we're sure these scripts work we will phase out shellscripts repo (it was originally an experiment and we're going to wrangle it under control now before it becomes a legacy).

#testing:

[Download the shunit2 framework](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/shunit2/shunit2-2.1.6.tgz), put it in `sh/bash_modules`. Go into the `smapputilities/sh/test` folder using `cd test` and run `bash test_*.sh` this should run a series of shunit2 tests. You should only run tests on a system that isn't running any hades tunnels currently.

For now check out the [shellscripts repository](https://github.com/SMAPPNYU/shellscripts).

For bash testing we could try to use [maybe] (https://github.com/p-e-w/maybe) with the bash [`test` builtin](http://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#Bourne-Shell-Builtins).

i know that testing with bash is hard and can be very sketchy. just do your best to modularize the code and test each piece that is important.

#logging:

you'll want to import the logger into your bash script:

```bash
source "/Users/yvan/smapprepos/smapputilities/sh/hades_tunnels/bash_modules/logger.sh" --source-only
```

and then use it like so:
```bash
log "blah"
log "blah $c"
```

#resources:

[run a bash program in the back ground] (http://stackoverflow.com/questions/13676457/how-can-i-put-the-current-running-linux-process-in-background)

[bash docs / reference](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc7)

[how to write a for loop in bash](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html)

[bash exit codes](http://www.tldp.org/LDP/abs/html/exitcodes.html)


#[hades_rotating_tunnel](https://github.com/SMAPPNYU/smapputilities/blob/master/sh/ssh_tunnels/hades_rotating_tunnel.sh)

a tunnel script that replaces our old tunnel scripts and eliminates the need to restart tunnels hourly usng autossh and an infinite loop. if a running tunnel dies 10x on one run of autossh it will rotate to the next login node on a new autossh tunnel. if a tunnel dies for any other reason and auto ssh exits it will rotate to the next tunnel.

note: the input is the `LISTEN_PORT` for auto ssh. each colector box needs a different listen port because the listen port get set on the remote machine. i recommend using ports 40001 to 40121 for this parameter, because they are unbound.

abstract:
```sh
echo 'PASS' | bash /path/to/hades_rotating_tunnel.sh LISTEN_PORT NETID
```

practical:
```sh
echo 'crazycats' | bash ~/smapprepos/smapputilities/sh/hades_tunnels/hades_rotating_tunnel.sh 56899 gtp324
```

*returns* a rotating tunnel that manages autossh connections between nodes on hades.

test: 

*WARNING: do not test on a server already running tunnels*

```sh
cd smapputilities/sh/hades_tunnels/test
# then
echo 'YOUR_HPC_PWD' | bash test_tunnel_functions.sh
```

#[kill_hades_rotating_tunnel](https://github.com/SMAPPNYU/smapputilities/blob/master/sh/ssh_tunnels/kill_hades_rotating_tunnel.sh)

a script that kills a running [hades_rotating_tunnel.sh]() 

abstract:
```sh
bash /path/to/kill_hades_rotating_tunnel.sh
```

practical:
```sh
bash ~/smapprepos/smapputilities/sh/hades_tunnels/kill_hades_rotating_tunnel.sh
```

*returns* nothing really, kills the rotating tunnel(s).

test: 

*WARNING: do not test on a server already running tunnels*

```sh
cd smapputilities/sh/hades_tunnels/test
# then
bash test_tunnel_functions.sh 
```

#[logger](https://github.com/SMAPPNYU/smapputilities/tree/master/sh/logger)

this is a logger that can log output to a file, written in bash.

abstract:
```sh
# in your bash script write
setlogpath /path/to/your/log/file
log "LOG_TEXT"
```

practical:
```sh
# in your bash script write
readonly datetime=`date +"%a-%b-%d-%T-%Z-%Y"`
readonly scriptname=`basename "$0"`
setlogpath ~/shlogs/$scriptname-$datetime
log "hey it works, nvm, error, error, oh man this is baaadddd"
```

*returns* the ability to log in your bash script mad easily

test: `bash sh/logger/test/test_logger.sh`

#[clear_history](https://github.com/SMAPPNYU/smapputil/blob/master/sh/utility/clear_history.sh)

clears bash history when run

abstract / practical:
```bash
bash clear_history.sh
```

*returns* a cleared bash history

note: you will also have to close all running terminal sessions to clear history as this is the only way to completely wipe bash history.

#author

[yvan](https://github.com/yvan)
