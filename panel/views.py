
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios, Agenda
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)
def index(request):
    return render(request, "index.html")

@permission_required('user.is_superuser')
def index_master(request):
    return render(request, "index_master.html")

# ERROR 404.

def error404(request, exception):
    return render(request, "error404.html")
 
# CREAR LOGIN.
def signup(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get ('username')
            password = form.cleaned_data.get('password1')            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('ingreso')
        else:
            return render(request, "registration/signup.html", {'form': form})
    else:
        form = UserCreationForm
        return render(request, "registration/signup.html", {'form': form})

# SALIR DEL LOGIN.
def signout (request):
    logout (request)
    return redirect('index')

# LOGIN.
def signin (request):
    if request.user.is_authenticated:
        return render(request, "registration/ingreso.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password' ]        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ingreso') #profile
        else:
            msg = 'Error de Login'
            form = AuthenticationForm(request . POST)
            return render(request, "registration/signin.html", {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, "registration/signin.html", {'form': form})

# CRUD USUARIOS ADM
@permission_required('user.is_superuser')
def listar(request):
    if request.method=='POST':
            palabra = request.POST.get('keyword')
            lista = User.objects.all()
            if palabra is not None:
                resultado_busqueda = lista.filter(
                    Q(id__icontains=palabra) |
                    Q(nombre__icontains=palabra) |
                    Q(apellido__icontains=palabra) |
                    Q(correo__icontains=palabra)                 
                )
                datos = {'usuarios': resultado_busqueda}
                return render(request, "crud usuarios/listar.html", datos)
            else:
                datos = { 'usuarios' : lista }
                return render(request, "crud usuarios/listar.html", datos)
    else:
        users = User.objects.order_by('-id')[:10]
        datos = { 'usuarios' : users }
        return render(request, "crud usuarios/listar.html", datos)
         
@permission_required('user.is_superuser')
def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_crear') and request.POST.get('tipouser'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_crear = request.POST.get('f_crear')
            user.tipouser = request.POST.get('tipouser')
            user.save()
            return redirect('listar')
    else:
        return render(request, "crud usuarios/agregar.html")

@permission_required('user.is_superuser')
def actualizar(request, idUsuario):
    try:
     if request.method=='POST':
        if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('telefono') and request.POST.get('f_crear') and request.POST.get('tipouser'):
            user = Usuarios()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_crear = request.POST.get('f_crear')
            user.tipouser = request.POST.get('tipouser')
            user.save()
            return redirect('listar')
     else:
        users = Usuarios.objects.all()
        user = Usuarios.objects.get(id=idUsuario)
        datos = { 'usuarios' : users, 'usuario' : user}
        return render(request, "crud usuarios/actualizar.html", datos)
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = { 'usuarios' : users, 'usuario' : user}
        return render(request, "crud usuarios/actualizar.html", datos)

@permission_required('user.is_superuser')
def eliminar(request, idUsuario):
    try:
     if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tupla = User.objects.get(id = id_a_borrar)
            tupla.delete()
            return redirect('listar')
     else:
        users = User.objects.all()
        user = User.objects.get(id=idUsuario)
        datos = { 'usuarios' : users, 'usuario' : user}
        return render(request, "crud usuarios/eliminar.html", datos)
    except User.DoesNotExist:
        users = User.objects.all()
        user = None
        datos = { 'usuarios' : users, 'usuario' : user}
        return render(request, "crud usuarios/eliminar.html", datos)

# LISTAR SOLICITUD AGENDA
@permission_required('user.is_superuser')
def solicitud(request):
    if request.method=='POST':
            palabra = request.POST.get('keyword')
            lista = Agenda.objects.all()
            if palabra is not None:
                resultado_busqueda = lista.filter(
                    Q(id__icontains=palabra) |
                    Q(marca__icontains=palabra) |
                    Q(modelo__icontains=palabra) |
                    Q(patente__icontains=palabra)                 
                )
                datos = {'solicitud': resultado_busqueda}
                return render(request, "mantencion/solicitud.html", datos)
            else:
                datos = { 'solicitud' : lista }
                return render(request, "mantencion/solicitud.html", datos)
    else:
        users = Agenda.objects.order_by('id')[:10]
        datos = { 'solicitud' : users }
        return render(request, "mantencion/solicitud.html", datos)

# ASIGNAR SOLICITUD AGENDA
@permission_required('user.is_superuser')
def asignar(request, idSolicitud):
    try:
     if request.method=='POST':
        if request.POST.get('modelo') and request.POST.get('marca') and request.POST.get('patente') and request.POST.get('chasis') and request.POST.get('f_ingreso') and request.POST.get('falla') and request.POST.get('descripcion'):
            agenda = Agenda()
            agenda.modelo = request.POST.get('modelo')
            agenda.marca = request.POST.get('marca')
            agenda.patente = request.POST.get('patente')
            agenda.chasis = request.POST.get('chasis')
            agenda.f_ingreso = request.POST.get('f_ingreso')
            agenda.falla = request.POST.get('falla')
            agenda.descripcion = request.POST.get('descripcion')            
            agenda.save()
            return redirect('solicitud')
     else:
        solicitudes = Agenda.objects.all()
        solicitud = Agenda.objects.get(id=idSolicitud)
        datos = { 'solicitudes' : solicitudes, 'solicitud' : solicitud}
        return render(request, "mantencion/asignar.html", datos)
    except Agenda.DoesNotExist:
        solicitudes = Agenda.objects.all()
        solicitud = None
        datos = { 'solicitudes' : solicitudes, 'solicitud' : solicitud}
        return render(request, "mantencion/asignar.html", datos)

# CREAR AGENDA.
def agenda(request):
    if request.method=='POST':
        if request.POST.get('modelo') and request.POST.get('marca') and request.POST.get('patente') and request.POST.get('chasis') and request.POST.get('f_ingreso') and request.POST.get('falla') and request.POST.get('descripcion'):
            agenda = Agenda()
            agenda.modelo = request.POST.get('modelo')
            agenda.marca = request.POST.get('marca')
            agenda.patente = request.POST.get('patente')
            agenda.chasis = request.POST.get('chasis')
            agenda.f_ingreso = request.POST.get('f_ingreso')
            agenda.falla = request.POST.get('falla')
            agenda.descripcion = request.POST.get('descripcion')            
            agenda.save()
            return redirect('agenda')            
    else:
        return render(request, "agenda/agenda.html")        

# ELIMINAR AGENDA.

@permission_required('user.is_superuser')
def eliminaragenda(request, idSolicitud):
    try:
     if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tupla = Agenda.objects.get(id = id_a_borrar)
            tupla.delete()
            return redirect('solicitud')
     else:
        solicitudes = Agenda.objects.all()
        solicitud = Agenda.objects.get(id=idSolicitud)
        datos = { 'solicitudes' : solicitudes, 'solicitud' : solicitud}
        return render(request, "mantencion/eliminaragenda.html", datos)
    except Agenda.DoesNotExist:
        solicitudes = Agenda.objects.all()
        solicitud = None
        datos = { 'solicitudes' : solicitudes, 'solicitud' : solicitud}
        return render(request, "mantencion/eliminaragenda.html", datos)

# INGRESO INTERMEDIO.
def ingreso(request):
    return render(request, "registration/ingreso.html")

