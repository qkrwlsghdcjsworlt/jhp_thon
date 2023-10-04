all:
	eval ssh-agent; ssh-add ~/.ssh/id_todo_rsa; git add .;git commit -m “update”;git push origin main
	
