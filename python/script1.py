#code to check for diskspace
import subprocess
out=subprocess.check_output(["df","-h"])
res=out.split("\n")
for x in res[1:]:
    x=x.split()
    if x:
        x[4]=x[4].replace("%","")
        if (int(x[4]))>70 :
            print(x[0])
