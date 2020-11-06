"""
第9章/HomeSharing/app/controllers/house.py
"""
from app.db.action_with_db import ActionWithDb


class by_id(ActionWithDb):
    async def execute(self, req, res):
        house = await self.db.house_res.by_id(req.arg(0))
        owner = None
        if house:
            owner = await self.db.auth_user.by_id(house['owner_id'])
        await res.render(
            "house/by_id.html",
            title=house['res_title'] if house else '找不到房源',
            house=house,
            owner=owner
        )
