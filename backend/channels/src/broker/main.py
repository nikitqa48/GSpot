import asyncio
from consumers.email.consumer import EmailConsumer
from consumers.notifications.consumer import NotificationConsumer
from consumers.prepare_queue import _prepare_consumed_queue
from publisher import publish
from services.rabbitmq import rabbit_connection
from services.database import db


async def main(consumer_classes) -> None:
    await rabbit_connection.connect("amqp://channels:BMfxN8drrYcIqXZMrpWTpDT0nMcOagMduLX0bjr4jwudpN@rabbitmq:5672/")
    await db.connect()
    try:
        async with rabbit_connection.channel as channel:
            await channel.set_qos(prefetch_count=100)
            # if os.environ.get('RABBITMQ_DEAD_LETTER_ENABLED'):
            #     await _prepare_dead_letter_queue(channel)
            for consumer_class in consumer_classes:
                queue = await _prepare_consumed_queue(channel, consumer_class.queue_name)
                consumer = consumer_class(queue)
                await consumer.consume()
                # await asyncio.wait([publish(channel) for _ in range(100)])
    finally:
        await rabbit_connection.disconnect()
        await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main((EmailConsumer, NotificationConsumer)))
