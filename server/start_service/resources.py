from import_export import resources
from .models import InformationOverdue, Example


class ExampleResource(resources.ModelResource):

    class Meta:
        model = Example
