import discord
import os
from datetime import date
from dotenv import load_dotenv
from recipes import *

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from keepalive import keep_alive

from botfunctions import *

load_dotenv()
bot = discord.Client()

GUILD = os.getenv('DISCORD_GUILD')

class MyClient(discord.Client):
    @bot.event
    async def on_ready(self):
        print("fitbot is now online as {0}".format(self.user))

    @bot.event
    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user.mentioned_in(message) and is_plot_request(
                message)[0] == 1:
            x = str(message.author.name) 
            plot_seven_day(person_dict[x])
            await message.channel.send(file=discord.File('{}_plot.png'.format(str(message.author.name))))

        if self.user.mentioned_in(message) and is_weight_update(
                message)[0] == 1:
            x = str(message.author.name)
            person_x = person_dict[x]
            update_weight(person_x, message.content.split()[1])
            
        if self.user.mentioned_in(message) and is_macro_update(message)[0] == 1 or is_macro_update(message)[0] == 2:
          x = str(message.author.name)
          person_x_1 = person_dict[x]
          change_macros(message, person_x_1)
          await message.channel.send(person_x_1.daily_macros)

        if self.user.mentioned_in(message) and is_calorie_reset_request(message)[0] == 1:
          x = str(message.author.name)
          person_x_2 = person_dict[x]
          reset_macros(person_x_2)
          await message.channel.send(person_x_2.daily_macros)
        
        if self.user.mentioned_in(message) and is_help_request(message)[0] == 1: 
          updatemacrosstr = 'To update macros, ping bot with \n\'@fitbot _code\'\n or   \n \'@fitbot calories/protein/fats/carbs\' '
          plotstr = '\nTo view plot of weight for the week, first update weight by pinging bot with integer weight \n\' @fitbot weight\' \n and then ping bot with \n \'@fitbot plot\''
          resetmacrosstr = '\nTo reset macros, ping the bot with \n\'@fitbot reset\'\n'
          

          await message.channel.send(updatemacrosstr+'\n'+plotstr+'\n'+resetmacrosstr)

keep_alive()
client = MyClient()
client.run(os.getenv('TOKEN'))

if __name__ == "__main__":
    main()
