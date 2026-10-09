
class ReservatioManager:

    def max_occupancy(bookings: list[tuple[int, int]]) -> tuple[int, int | None, int | None]:
        
        if not bookings:
            return (0, None, None)
        
        # Create an array of 24 numbers where each position is increased
        # for every occupied hour during the day.
        
        occupancy = [0] * 24
        
        for st, ed in bookings:
            for i in range(st,ed):
                occupancy[i] += 1    
                
        max = 0 # Maximum concurrency value
        max_start = 0 # Start of the maximum concurrency period
        max_end = 0 # End of the maximum concurrency period
        
        # Iterate through the occupancy array and extract the period
        # with maximum concurrency.
        
        for i,n in enumerate(occupancy):
            if n > max:
                max = n 
                max_start = i
                max_end = i + 1        
        
        return (max,max_start,max_end)    


    def max_multi_occupancy(bookings: list[tuple[int, int]]) -> tuple[int, list[tuple[int, int]] | None]:
            
            if not bookings:
                return (0, None)
            
            # Create an array of 24 numbers where each position is increased
            # for every occupied hour during the day.
            
            occupancy = [0] * 24
            
            for st, ed in bookings:
                for i in range(st,ed):
                    occupancy[i] += 1                
            oMax = max(occupancy) # Maximum concurrency value       
            
            lmax_occupancy = [] # List of time ranges with maximum concurrency
            imax_occupancy = [] # Current maximum concurrency range
            
            # Iterate through the occupancy array and extract the periods
            # with maximum concurrency.
            
            for i,n in enumerate(occupancy):
                         
                if n == oMax:                
                    if not imax_occupancy:                    
                        imax_occupancy = [i,0]                    
                    imax_occupancy[1] = i + 1                                
                else:                
                    if imax_occupancy:                                 
                        lmax_occupancy.append((imax_occupancy[0], imax_occupancy[1]))
                    imax_occupancy = []            
            
            # Handle the case where the last range has maximum concurrency.
            
            if imax_occupancy:                                 
                lmax_occupancy.append((imax_occupancy[0], imax_occupancy[1]))
                                                    
            return (oMax,lmax_occupancy) 



if __name__ == "__main__":
    
    print(ReservatioManager.max_occupancy([(12,14),(11,17)]))              # -> (2, 12, 14)
    print(ReservatioManager.max_occupancy([(9, 12), (10, 13), (11, 14)]))  # -> (3, 11, 12)
    print(ReservatioManager.max_occupancy([(9, 10), (10, 11), (11, 12)]))  # -> (1, 9, 10)
    print(ReservatioManager.max_occupancy([]))                             # -> (0, None, None)    