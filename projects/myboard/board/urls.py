from django.urls import path

from.import views
app_name = 'board'
urlpatterns = [
    # board/라면
    path('', views.index, name='index'),
    # 글읽기 주소 /board/0
    path('<int:id>/', views.read, name='detail'),
    # 글쓰기 주소
    path('write/', views.write, name='write'),
    # 수정 주소
    path('<int:id>/update/', views.update, name='update'),
    # 삭제 주소
    path('<int:id>/delete/', views.delete, name='delete'),
    # 댓글쓰기 주소
    path('<int:id>/write_reply/', views.write_reply, name = 'write_reply'),
    # 댓글 삭제 주소(id: 글번호, rid: 댓글번호)
    path('<int:id>/delete_reply/', views.delete_reply, name='delete_reply'),
    # 댓글 수정 주소
    path('<int:id>/update_reply/', views.update_reply, name='update_reply'),

    # AJAX
    path('callAjax/', views.call_ajax),
    
    # AJAX_댓글 목록
    path('<int:id>/load_reply/',views.load_reply, name = 'load_reply'),
    path('<int:id>/downlad/',views.downlad,name='downlad'),


    # CBV 방식으로 호출할 주소
    # as_view() : 클래스를 뷰의 기능으로서 사용하겠다~
    path('cbv/', views.BoardList.as_view()),
    path('cbv/<int:pk>/', views.BoardDetail.as_view()),
]