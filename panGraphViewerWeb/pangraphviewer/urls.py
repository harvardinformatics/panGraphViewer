from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.graph, name='default'),

    # main pages
    path('graph', views.graph, name='graph'),
    path('vcf_to_gfa', views.vcf_to_gfa, name='vcf_to_gfa'),

    # supporting pages
    path('getdata', views.getdata, name='getdata'),
    path('parse_gfa', views.parse_gfa, name='parse_gfa'),
    path('parse_vcf', views.parse_vcf, name='parse_vcf'),
    path('parse_bed', views.parse_bed, name='parse_bed'),
    path('viewseq', views.viewseq, name='viewseq'),
    path('downloadseq', views.downloadseq, name='downloadseq'),

    path('upload_file', views.upload_file, name='upload_file'),

    path('convert_vcf', views.convert_vcf, name='convert_vcf'),
    path('download_rgfa', views.download_rgfa, name='download_rgfa'),

    path('get_uploaded_list', views.get_uploaded_list, name='get_uploaded_list'),
    path('manage_file', views.manage_file, name='manage_file'),

    path('draw_overlap_gene', views.draw_overlap_gene, name='draw_overlap_gene'),
    path('check_node_id', views.check_node_id, name='check_node_id'),
]
