from django.urls import path
from .views import UploadDocumentView, ListDocumentsView

urlpatterns = [
    path('upload/', UploadDocumentView.as_view(), name='upload-document'),
    path('list/', ListDocumentsView.as_view(), name='list-documents'),
#     path('query/', QueryDocumentView.as_view(), name='query-document'),
 ]
