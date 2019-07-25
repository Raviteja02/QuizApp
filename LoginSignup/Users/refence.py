if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password1']
		password2= request.POST['password2']
		email    = request.POST['email']
		firstname= request.POST['firstname']
		lastname = request.POST['lastname']
		if password == password2:
			user = QuizAppUser(username=username,password=password,email=email,firstname=firstname,lastname=lastname)
			user.save()
			login(request,users)
		return redirect('userpage')

	else:
		return render(request, 'registration/register.html')