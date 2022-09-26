from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import subprocess
from django.conf import settings
from django.templatetags.static import static
import xml.etree.ElementTree as ET
from zipfile import ZipFile, ZIP_DEFLATED
from os.path import basename
from converter.main import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        error = ""
        data = {}
        input_files =  request.FILES.getlist('tex_file_input')
        if len(input_files)!=2:
            error += "Obtained files doesn't match the expected count (2)"
            print(error)
        else:
            tex_file_input = ""
            ref_file_input = ""
            for f in input_files:
                if f.name.split(".")[-1]=="tex":
                    tex_file_input = f
                elif f.name.split(".")[-1]=="bib":
                    ref_file_input = f
                else:
                    error += "Received files with invalid extensions."
            if error=="":
                try:
                    tex_file_path = os.path.join(settings.MEDIA_ROOT, "XML_Pipeline/static/input.tex")
                    if os.path.exists(tex_file_path):
                        os.remove(tex_file_path)
                    fs = FileSystemStorage()
                    tex_file_name = fs.save("XML_Pipeline/static/input.tex", tex_file_input)
                    ref_file_path = os.path.join(settings.MEDIA_ROOT, "XML_Pipeline/static/reference.bib")
                    if os.path.exists(ref_file_path):
                        os.remove(ref_file_path)
                    fs = FileSystemStorage()
                    ref_file_name = fs.save("XML_Pipeline/static/reference.bib", ref_file_input)
                    tex_output_file_path = 'XML_Pipeline/static/journal.xml'

                    input_filepath = 'XML_Pipeline/static/input.tex'
                    output_filepath = 'XML_Pipeline/static/journal.xml'
                    reference_input_filepath = 'XML_Pipeline/static/reference.bib'
                    reference_output_filepath = 'XML_Pipeline/static/reference.xml'
                    main(input_filepath, output_filepath, reference_input_filepath, reference_output_filepath)
                    # command = 'pandoc ' + tex_file_name + ' -f latex -t jats -s -o ' + tex_output_file_path
                    # subprocess.call(command.split(" "))
                    print("Conversion Done...")
                    # tree = ET.parse('XML_Pipeline/static/journal.xml')
                    # root = tree.getroot()
                    # make_conflict_of_interest(root)
                    # tree.write('XML_Pipeline/static/journal.xml')
                    with ZipFile(file='XML_Pipeline/static/output.zip',mode='w',compression=ZIP_DEFLATED) as zip:
                        zip.write(output_filepath,basename(output_filepath))
                        zip.write(reference_output_filepath,basename(reference_output_filepath))
                    data['file_name'] = "output.zip"
                    data['file_path'] = "XML_Pipeline/static/output.zip"
                except Exception as e:
                    print(e)
                    error += "Unable to convert the file"
        if error=="":
            print(data)
            return render(request,'converter/index.html',data)
        return render(request,'converter/index.html', {'error': error})
    return render(request,'converter/index.html')