
class ReservatioManager:

    # The following validations are performed:
    #   - None of the values can be null.
    #   - The value is integer.
    #   - Time values greater than 24 are not allowed.
    #   - Negative values are not allowed.
    #   - The start time cannot be greater than the end time.
    #   - The start and end times must be different.    
    def is_valid(st: int, ed: int) -> bool:
        if (st is None or
            ed is None or
            type(st) is not int or
            type(ed) is not int or
            st < 0 or 
            ed < 0 or 
            ed <= st or 
            ed > 24):
            return False
        else:
            return True


    def max_occupancy(bookings: list[tuple[int, int]]) -> tuple[int, list[tuple[int, int]] | None]:
            
            if not bookings:
                return (0, None)
            
            # Create an array of 24 numbers where each position is increased
            # for every occupied hour during the day.
            
            occupancy = [0] * 24
            
            for st, ed in bookings:
                if not ReservatioManager.is_valid(st,ed):
                    raise ValueError(f"There is an invalid value in the list ({st}, {ed}).")
                
                                
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
    
    print(ReservatioManager.max_occupancy([(12,14),(11,17)]))              # -> (2, [(12, 14)])
    print(ReservatioManager.max_occupancy([(9, 12), (10, 13), (11, 14)]))  # -> (3, [(11, 12)])
    print(ReservatioManager.max_occupancy([(9, 10), (10, 11), (11, 12)]))  # -> (1, [(9, 12)])
    print(ReservatioManager.max_occupancy([]))                             # -> (0, None)