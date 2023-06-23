from config.database import db_config
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = AsyncIOMotorClient(db_config.url, maxPoolSize=10, minPoolSize=10)
    session: AsyncIOMotorDatabase

    async def ping_server(self):
        try:
            self.client.GSpot.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    async def insert_collection(self, collection_name: str, model):
        db = self.session.client.GSpot
        collection = db.get_collection(collection_name)
        document = await collection.insert_one(model.dict())
        return document.inserted_id

    async def get_collection(self, data):
        db = self.session.client.GSpot
        collection = db.get_collection('dialog')
        result = collection.find_one({data})

    async def find_document(self, collection_name: str, field: str, value: str):
        print(collection_name, field, value)


db = MongoManager()


