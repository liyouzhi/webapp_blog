import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='webAppBlog')
    u = User(name='Test', email='test@test.com', password='123456', image='about:blank')
    await u.save()
    await orm.destroy_pool()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
