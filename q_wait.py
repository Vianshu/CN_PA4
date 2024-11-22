import matplotlib.pyplot as plt
file="./ns-allinone-3.42/ns-3.42/tcp-example.tr"
output_file="qt.txt"
src_ip="10.1.1.1"
dest_ip="10.2.2.2"
ta=[] #stores the enqueue time for packets
wt=[] #stores the waiting time for packets
fint=[] # stores the dequeue time for packets

# Packets are stored in a queue for waiting
with open(file,'r') as f:
    for i in f:
        info=i.strip().split()
# So, first when a packets is added to queue, we stores its starting time 
        if(info[0]=="+"):
            ta.append(float(info[1]))
# then when packet is dequeued , we calculate waiting time ,
        elif(info[0]=="-"):
            wait=(float(info[1])-ta[0])
            fint.append(float(info[1]))
            ta.pop(0)
            wt.append(wait)

#plotting the graph
x=[1,2,3,4,5,6,7,8,9,10]
plt.xticks(x)
plt.plot(fint,wt)
plt.xlabel('Dequeue time (seconds)')
plt.ylabel('waiting time (seconds)')
plt.show()