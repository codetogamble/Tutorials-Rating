import multiplePages

sq=['python','Java','php','Nodejs','Android','Ruby','Qt Framework','Django','laravel','symphony','express','socket.io']
for x in sq:
	
	for i in [1,2,3,4]:
		temp= []
		temp = multiplePages.FindUrl(x,i)
		multiplePages.WF(temp)
		multiplePages.cleanup(temp)
