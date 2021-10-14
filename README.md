Discord Webhook Spammer 
##########################
Requirements To use discord Webhook spammer :

A role in a discord server that has accesss to create and delete Webhooks for specific channels. 
If there is an existing Webhook for a specified channel and you know the Webhook url, you can use that as well.

########################
Step 1
How to setup the script : 

It's a very simple thing to do. 
You will need your webhook url for this.
Once you have your webhook url, replace the String "Webhook url" with your webhook url and make sure you have the "" around the webhook url otherwise python won't register it as a string. 
For the String "Message" you can put any word 
You want in the "Message" string. This will be your Message that your Webhook will send to the channel. 
 
Don't get ahead of yourself. You still have two one thing to do And one is optional. First thing is the string "Raid bot" can be changed to any name you desire. This will act as your webhook username. Webhooks are like Discord Scripts that act as bots almost.
Default username is configured to "Raid bot". Feel free to change it if you want.
############################
Step 2 Get Python

If you dont have python installed, download pythons latest version for windows and make sure you click on the 'ADD TO PATH' option during the installation.

pip install the requirement in cmd

pip install requests
then run the script..
python webhook_spammer.py

Then you are all setup! 
###############################

Note : @everyone and @here will work for webhook spammers no matter what. 
So in your sting you can use @everyone or @here all you want!






