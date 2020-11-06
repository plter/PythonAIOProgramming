"""
第9章/HomeSharing/app/controllers/house.py
"""
from app.db import data_grid
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


class all(ActionWithDb):

    async def execute(self, req, res):
        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "house/all_row.html",
                row=row
            )

        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            # 多表查询
            (db.house_res.id > 0) &
            (db.house_res.owner_id == db.auth_user.id),
            fields=[
                # 只显示指定的字段
                db.house_res.id,
                db.house_res.res_title,
                db.house_res.pub_time,
                db.auth_user.user_name,
                db.auth_user.user_phone,
            ],
            order_by=~db.house_res.id,
            row_render=row_render,
            header_render=lambda *args: ""
        )
        await res.render(
            "house/all.html",
            title="房源", grid=grid
        )
        pass
