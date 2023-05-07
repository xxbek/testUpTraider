import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Dashboard(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dashboards", null=True)

    def __repr__(self):
        return self.description


class TreePoint(models.Model):
    name = models.CharField(max_length=100, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    dashboard_id = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="points")
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name="parent", null=True, blank=True, default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class TreePointRelation(models.Model):
    point_id = models.ForeignKey(TreePoint, on_delete=models.CASCADE, null=False)
    child_id = models.ForeignKey(TreePoint, on_delete=models.CASCADE, related_name="children", null=False)

    def __repr__(self):
        return f'{self.point_id} is parent for {self.child_id}'

