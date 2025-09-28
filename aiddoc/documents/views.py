from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Document
from .serializers import DocumentSerializer
# from .langchain_utils.chains import build_qa_chain

class UploadDocumentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListDocumentsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        docs = Document.objects.filter(user=request.user)
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)

# class QueryDocumentView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         doc_id = request.data.get("doc_id")
#         query = request.data.get("query")

#         try:
#             doc = Document.objects.get(id=doc_id, user=request.user)
#         except Document.DoesNotExist:
#             return Response({"error": "Document not found"}, status=404)

#         qa_chain = build_qa_chain(doc.file.path)
#         answer = qa_chain.run(query)
#         return Response({"answer": answer})
