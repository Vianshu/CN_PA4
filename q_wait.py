import matplotlib.pyplot as plt
input_file="tcp-example.tr"
output_file="qt.txt"
src_ip="10.1.1.1"
dest_ip="10.2.2.2"
ta=[] #stores the enqueue time for packets
wt=[] #stores the waiting time for packets
fint=[] # stores the dequeue time for packets

# Packets are stored in a queue for waiting
with open(input_file,'r') as trace_file,open(output_file,'w') as output:
    for line in trace_file:
        field=line.strip().split()
# So, first when a packets is added to queue, we stores its starting time 
        if(field[0]=="+"):
            ta.append(float(field[1]))
# then when packet is dequeued , we calculate waiting time ,
        elif(field[0]=="-"):
            wait=(float(field[1])-ta[0])
            fint.append(float(field[1]))
            ta.pop(0)
            wt.append(wait)

#plotting the graph
plt.plot(fint,wt)
plt.xlabel('Dequeue time (seconds)')
plt.ylabel('waiting time (seconds)')
plt.show()