"""  
 Name: Discord_Bot
 Date: 10/11/2019
 Description: Old notes from development of trying different ways of implementing the bot.

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""
# Old methods/tests kept for notes please ignore below.
"""
*COROUTINES* are generalization of subroutines. They are used for cooperative multitasking 
where a process voluntarily yield (give away) control periodically or when idle in order 
to enable multiple applications to be run simultaneously.
"""
"""
#decorator
@client.event
async  def on_message(message):
    #checks to see if the message is from a user to prevent bot recursion
    if message.author == client.user:
        return

    if message.content == "!test":
        response = "Testing self ping: "
        my_id = "<@!313686003594559488>"
        #await suspends the execution of the surrounding coroutine until each coroutine has finished.
        await message.channel.send(response + my_id + " pong")

    if message.content == "!patchnotes":
        response = "<@!251728492272680971> I could make the bot do this but its funnier " \
                                           "to have a bot ping you for patch notes."
        await message.channel.send(response)

    if message.content == "!smallbraincoder":
        response = "<@!120554480541368320> Rust is a neat language - Python Bot"
        await message.channel.send(response)

    if message.content == "!avoidslegday":
        response = "<@!277561909803483136> Oh hey look a hill, guess I'll " \
                                           "just take the elevator - Tevin"
        await message.channel.send(response)

    #manual exception raise from discord to console
    elif message.content == "!exception":
        response = "Error: exception written to error.log"
        await  message.channel.send(response)
        raise discord.DiscordException
        
# Catching exceptions for on_message function and writing it to a file
@bot.event
async def on_error(event, *args, **kwargs):
    with open("error.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise       
"""
"""
# Dm's users that just joined the server for the first time
@client.event
async def on_member_join(member):
    #waits on exec of the higher coroutine until each inner coroutine has finished
    await member.create_dm()
    await member.dm_channel.send(
        f"Sigh {member.name}, I guess you can join the server."
    )
"""
"""
#looks for matching server name as bot can be in multiple servers
    for guild in client.guilds:
        if guild.name == guild:
            break
"""
""" 
#Prints all members of the server in a formatted string to console
members = "\n - " .join([member.name for member in guild.members])
print(f"Server Members:\n - {members}")
"""

"""
req = requests.get("https://www.reddit.com/r/Warthunder/.json%22)
data = req.content

obj = json.loads(data, object_hook=RedditData)
de = DataExtractor(obj)


#we know this is a reddit response
if hasattr(obj,'kind'):
    print(obj.kind)
    print(obj.data["children"][0]) #gets the first child post. 


#this is a error
if hasattr(obj,"message"):
    print(de.getMessage())
"""