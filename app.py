from redis import Redis

redis_cli = Redis(host='localhost',
                  port='6379',
                  db=0
                  )

redis_cli.set('iloveu','china')

print(redis_cli.get('iloveu'))

print('ok')