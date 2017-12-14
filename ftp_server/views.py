from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Engine, TemplateDoesNotExist, loader
import os
from django.utils._os import safe_join

from django.views.static import DEFAULT_DIRECTORY_INDEX_TEMPLATE
def video_or_directory(request,file_name=None,document_root=None,path=None):
    print(file_name)
    print(path)
    if file_name=='':
        return video_directory(request,document_root,path)
    else:
        return video(request,file_name,path)

def video(request,file_name,path):
    context={
        "file_path":path+'/'+file_name,
        "file_name":file_name
    }
    return render(request,'ftp_server/video.html',context)

def video_directory(request,document_root=None,path=''):

    full_path='/'.join([document_root,path])
    print('full_path:'+full_path)
    try:
        t = loader.select_template([
            'static/directory_index.html',
            'static/directory_index',
        ])
    except TemplateDoesNotExist:
        t = Engine(libraries={'i18n': 'django.templatetags.i18n'}).from_string(DEFAULT_DIRECTORY_INDEX_TEMPLATE)
        c = Context()
    else:
        c = {}
    files = []
    for f in os.listdir(full_path):
        print(f)
        if not f.startswith('.'):
            if os.path.isdir(os.path.join(full_path, f)):
                f += '/'
            files.append(f)
    c.update({
        'directory': full_path + '/',
        'file_list': files,
    })
    return HttpResponse(t.render(c))