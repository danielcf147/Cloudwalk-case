# from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from io import StringIO
from parte2 import main


class TransactionView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file received"}, status=400)

        try:
            # Use StringIO to handle file data
            file_str = StringIO(file.read().decode("utf-8"))

            # Call the main function
            result = main(file_str)

            return Response({"result": result}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
