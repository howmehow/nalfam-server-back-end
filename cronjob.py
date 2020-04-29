

from crontab import CronTab

# cron = CronTab(user='root')
# job = cron.new(command='python keep_it_fresh.py')
# job.second.every(10)

# cron.write()

cron = CronTab(crontab="""1 * * * * python /Users/lukerhys/final_project.dun.dun.dun/cisco_app_server/keep_it_fresh.py""")


# with CronTab(crontab="""* * * * * python keep_it_fresh.py""") as cron:
#     job = cron.new(command='echo hello_world')
#     job.second.every(1)
# print('cron.write() was just executed')
cron.write()