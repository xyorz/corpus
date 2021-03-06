from django.urls import path
from dmdb import views

app_name = 'dmdb'
urlpatterns = [
    path('n_search/', views.search, name='n_search'),
    path('download_result/', views.download_result),
    path('download_readme/', views.download_readme, name='download_readme'),
    path('download_backend_readme/', views.download_backend_readme, name='download_backend_readme'),
    path('get_context/', views.new_get_content),
    path('get_res_statistics/', views.get_res_statistics),
    path('insert/', views.corpus_insert, name='insert'),
    path('manage/', views.corpus_manage, name='manage'),
    path('get_sections_by_doc_id/', views.get_sections_by_doc_id),
    path('doc/', views.doc, name='doc'),
    path('get_section/', views.get_section),
    path('delete/', views.corpus_delete),
    path('authors_info_insert/', views.authors_info_insert),
    path('authors_info/', views.authors_info),
    path('authors_change_preset/', views.authors_change_preset),
    path('login/', views.login),
    path('logout/', views.logout),
    path('get_user_list/', views.get_user_list),
    path('delete_user/', views.delete_user),
    path('add_user/', views.add_user),
    path('update_user/', views.update_user),
    path('deactivate/', views.deactivate),
    path('update_zh_to_hant/', views.update_zh_to_hant),
    path('get_hant_by_zh/', views.get_hant_by_zh),
    path('get_zh_to_hant_list/', views.get_zh_to_hant_list),
    path('update_zh_to_hant_1/', views.update_zh_to_hant_1),
    path('set_preset/', views.set_preset),
    path('get_preset/', views.get_preset),
]