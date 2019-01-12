from django.shortcuts import render, HttpResponse

# html_base = """
# <h1>AUTARKIA</h1>
# <ul>
# <li><a href="/">Portada</a></li>
# <li><a href="/about/">Acerca de</a></li>
# <li><a href="/portafolio/">Portafolio</a></li>
# <li><a href="/contacto/">Contacto</a></li>
# </ul>
# """

# Create your views here.

# def home(request):
    # html_response = '<h1>AUTARKIA</h1>'
    # for i in range(10):
    #     html_response += '<h1>BIENVENIDOS/WELCOME</h1>'
    # return HttpResponse(html_response)

    # return HttpResponse('<h1>AUTARKIA</h1><h1>BIENVENIDOS/WELCOME</h1>')

    # return HttpResponse(html_base + """
    #     <h2>BIENVENIDOS/WELCOME</h2>
    #     <p>Portada</p>
    # """)

def home(request):
    return render(request,"core/home.html")

# def about(request):
    # return HttpResponse('<h1>AUTARKIA</h1><h1>ABOUT</h1><P>Bienes y servicios</P>')
    # return HttpResponse(html_base + """
    #     <h2>ECONOMIA INDEPENDIENTE</h2>
    #     <h3>EN BUSCA DE LA LIBERTAD</h3>
    # """)

def about(request):
    return render(request,"core/about.html")

# def portafolio(request):
#
#     return HttpResponse(html_base + """
#         <h2>PORTAFOLIO</h2>
#         <h3>COMPRA Y VENTA</h3>
#         <p>Articulos y servicios</p>
#     """)

def portafolio(request):
    return render(request,"core/portafolio.html")

# def contacto(request):
#
#     return HttpResponse(html_base + """
#         <h2>CONTACTO</h2>
#         <p>Email: <a href="mailto:autarkia@email.com">autarkia@email.com</a></p>
#     """)

def contacto(request):
    return render(request,"core/contacto.html")
