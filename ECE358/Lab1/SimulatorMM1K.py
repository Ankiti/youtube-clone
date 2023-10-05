import HelperFunctions


events = [] #queue to store events


class event:

    def __init__(self, event_type, time, length):
        self.event_type = event_type
        self.time = time
        self.length = length




def observer(simulated_T, alpha):
    '''Function to calculate observation events'''
    time = 0
    while(1):
        time += HelperFunctions.generate_exponential_random_numbers(alpha)
        if(time > simulated_T):
            break
        observer_event = event("OBSERVER", time, None)  #object of class 'event'
        events.append(observer_event) #adding to the event queue

def arrival(simulated_T,lam, L):
    '''Function to calculate arrival events'''
    time = 0
    length = 0
    while(1):
        time += HelperFunctions.generate_exponential_random_numbers(lam)
        length = HelperFunctions.generate_exponential_random_numbers(1/L)
        if(time > simulated_T):
            break
        arrival_event = event("ARRIVAL", time, length)  #object of class 'event'
        events.append(arrival_event) #adding to the event queue

def departure(C):
    '''Function to calculate departure events'''
    prev_dep = 0 #variable that stores the previous packet's departure time

    for x in range(0,len(events)):

        if (events[x].event_type == "ARRIVAL"):
            service_time = events[x].length/C

            if((events[x].time - prev_dep) >= 0 ): #packet arrived after prev one finished (no waiting time) -> there is idle time
                departure_time = events[x].time + service_time
            
            else:                                   #packet arrived before prev one finished (there is waiting time) -> no idle time
                departure_time = prev_dep + service_time
                

            prev_dep = departure_time

            departure_event = event("DEPARTURE", departure_time, None)  #object of class 'event'
            events.append(departure_event) #adding to the event queue


def sort():
    '''Sort observer and arrival events based on time'''
    events.sort(key= lambda event:event.time)

def dequeue(K):
    Na = 0 #Number of arrivals
    Nd = 0 #Number of departures
    No = 0 #Number of observers
   
    Number_of_pkt = 0 #Number of packets that each observer observes
    Number_pkt_dropped = 0 #Number of packets dropped
    Number_pkt_generated = 0 #Number of packets generated
    P_loss = 0 #Probability that a packet will be dropped
    E_n = 0 #Average number of packets in the queue
    P_idle = 0 #Proportion of time the system is idle

    for x in range(0,len(events)):

        if (events[x].event_type == "OBSERVER"):
            No+=1
            Number_of_pkt += (Na-Nd)
        
        
        elif (events[x].event_type == "ARRIVAL"):
            Number_pkt_generated += 1
            if ((Na-Nd) >= K): #packet dropped as queue is full
              
                Number_pkt_dropped += 1
            else:
                Na+=1
                

        elif (events[x].event_type == "DEPARTURE"):
            if (Na == Nd):
                pass
            else:
                Nd+=1

    E_n = Number_of_pkt / No
    P_loss = Number_pkt_dropped / Number_pkt_generated
    print("E[N]: " ,E_n, "|| P_loss: ", P_loss)

    events.clear()