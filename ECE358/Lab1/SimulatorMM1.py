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
        observer_event = event("OBSERVER", time,None)  #object of class 'event'
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

def dequeue():
    Na = 0 #Number of arrivals
    Nd = 0 #Number of departures
    No = 0 #Number of observers
    Idle_counter = 0 #Idle counter
    Number_of_pkt = 0 #Number of packets that each observer observes
    E_n = 0 #Average number of packets in the queue
    P_idle = 0 #Proportion of time the system is idle

    for x in range(0,len(events)):

        if (events[x].event_type == "OBSERVER"):
            No+=1
            Number_of_pkt += (Na-Nd)
            if (Na == Nd):
                Idle_counter += 1 
        
        elif (events[x].event_type == "ARRIVAL"):
            Na+=1
        elif (events[x].event_type == "DEPARTURE"):
            Nd+=1

    E_n = Number_of_pkt / No
    P_idle = Idle_counter / No

    print("E[N]: " ,E_n, "|| P_idle: ", P_idle)

    events.clear()

# def main():
#     observer(10)
#     arrival(5, 75, 100)
#     departure(1000)
#     sort()
#     # for x in range(0,len(events)):
#     #     print(events[x].event_type, events[x].time)
#     dequeue()
# main()