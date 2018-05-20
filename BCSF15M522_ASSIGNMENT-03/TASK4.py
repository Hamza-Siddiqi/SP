import psutil 
import sys
import datetime

if len(sys.argv) == 1 :
	print ("No arguments were given")
else :
	for i in range(1,len(sys.argv)):
		if(sys.argv[i].isdigit()):
			inpid=int(sys.argv[i])
			if(psutil.pid_exists(inpid)):
				p=psutil.Process(inpid)
				Propid=str(p.pid)
				print("Process ID : "+Propid)
				ProName=str(p.name())
				print("Process Name : "+ProName)
				ProStatus=str(p.status())
				print("Process Status : "+ProStatus)
				ProPPid=str(p.ppid())
				print("Process Parent ID : "+ProPPid)
				par=psutil.Process(p.ppid())
				ProPPName=str(par.name())
				print("Process Parent Name : "+ProPPName)
				timeobj = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
				print("Process Creation Time : "+timeobj)
				
				x=str(p.open_files())
				y=x[1:(len(x)-2)]
				list_my=(y.split("popenfile"))
				print("Files opened by the process information :")
				if(p.num_fds()==0):
					print("\n".join(list_my))
				else:
					print("No files are opened")
				ProM=str(p.memory_full_info())
				pm=ProM[9:(len(ProM)-1)]
				ProMemory=pm.split(",")
				print("Memory Information :")
				print("\n".join(ProMemory))
			else:
				print("This Process Does Not Exists")
		else:
			print("Invalid PID")
