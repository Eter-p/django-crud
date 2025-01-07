from django.shortcuts import redirect

def actualizar_datos(request,registro,usuario,form):
	if len(registro) == 0:
		form_datos_p = form(request.POST)
		new_form_datos_p = form_datos_p.save(commit=False)
		new_form_datos_p.cuenta = usuario
		new_form_datos_p.save()
		return new_form_datos_p
	form_datos_p = form(request.POST,instance=registro[0])
	if form_datos_p.is_valid():
		new_form_datos_p = form_datos_p.save()
		correo = request.POST.get("correo_1")
		if correo != None:
			usuario.email = correo
			usuario.save()
		return new_form_datos_p
	return redirect("failure","actualizacion")

	