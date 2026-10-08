
class ReservatioManager:

    def max_occupancy(bookings: list[tuple[int, int]]) -> tuple[int, int | None, int | None]:
        
        if not bookings:
            return (0, None, None)
        
        occupancy = [0] * 24
        
        for st, ed in bookings:
            for i in range(st,ed):
                occupancy[i] += 1    
                
        max = 0
        max_start = 0
        max_end = 0
        
        for i,n in enumerate(occupancy):
            if n > max:
                max = n
                max_start = i
                max_end = i + 1        
        
        return (max,max_start,max_end)    






if __name__ == "__main__":
    
    print(ReservatioManager.max_occupancy([(12,14),(11,17)]))              # -> (2, 12, 14)
    print(ReservatioManager.max_occupancy([(9, 12), (10, 13), (11, 14)]))  # -> (3, 11, 12)
    print(ReservatioManager.max_occupancy([(9, 10), (10, 11), (11, 12)]))  # -> (1, 9, 10)
    print(ReservatioManager.max_occupancy([]))                             # -> (0, None, None)    