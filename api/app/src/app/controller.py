import logging

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import UserEvent
from .permissions import AlgorithmPermission
from src.base_crud import BaseCRUD
from src.init_database import Session
from .utils import get_client_ip

logging.basicConfig(
    level=logging.ERROR,
    filename='program.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

basecrud = BaseCRUD(Session)


class TestController(viewsets.ViewSet):
    serializer_classes = {
        "get_result": None,
    }

    def get_result(self, request):
        return Response(
            data={"result": "python-test-api"}, status=status.HTTP_200_OK
            )


class AlgorithmView(viewsets.ViewSet):
    permission_classes = (AlgorithmPermission,)

    def get_events(self, request):
        try:
            results = basecrud.get_many_by_statement(
                "SELECT * FROM events ORDER BY date_created DESC LIMIT 5"
                )
            data = [dict(row) for row in results]
            return Response(data, status=status.HTTP_200_OK)
        except Exception as error:
            logging.error(error, exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post_event(self, request):
        try:
            basecrud.insert(UserEvent, user_ip=get_client_ip(request))
            basecrud.commit()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as error:
            logging.error(error, exc_info=True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
