from instabot import InstaBot

bot = InstaBot('username', 'password',
               like_per_day=100000,
               more_than_likes=50,
               tag_list = ['your', 'tags', 'here'],
               max_like_for_one_tag=50,
               log_mod = 0)
bot.auto_mod()
