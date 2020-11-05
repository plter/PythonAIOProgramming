"""
第9章/HomeSharing/app/controllers/admin.py
"""
from ..db.action_with_db import ActionWithDb
from ..db import auth
from ..db import data_grid


class index(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        await res.render("admin/index.html", title="cms4py管理面板")


class memberships(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            db.auth_membership.id > 0,
            order_by=~db.auth_membership.id
        )
        await res.render(
            "admin/memberships.html", title="关系表",
            grid=grid
        )
