

class Formatting( object ):

    def spacing_gen_new( self, row_list ):
    
        for i, elem in enumerate(row_list):
        
            if i < 1:

                if len(elem) == 6:
                    spacing = ''
                elif len(elem) == 5:
                    spacing = ' '
                elif len(elem) == 4:
                    spacing = '  '
                elif len(elem) == 3:
                    spacing = '   ' 
                elif len(elem) == 2:
                    spacing = '    ' 
                else:
                    pass
    
                yield spacing
    
                if len(row_list[i+1]) == 6:
                    spacing = ''
                elif len(row_list[i+1]) == 5:
                    spacing = ' '
                elif len(row_list[i+1]) == 4:
                    spacing = '  '
                elif len(row_list[i+1]) == 3:
                    spacing = '   '
                elif len(row_list[i+1]) == 2:
                    spacing = '    ' 
                else:
                    pass
    
                yield spacing
    
            elif i > 0 and i < len(row_list)-1:

                if len(row_list[i+1]) == 6:
                    spacing = ''
                elif len(row_list[i+1]) == 5:
                    spacing = ' '
                elif len(row_list[i+1]) == 4:
                    spacing = '  '
                elif len(row_list[i+1]) == 3:
                    spacing = '   '
                elif len(row_list[i+1]) == 2:
                    spacing = '    ' 
                else:
                    pass
    
                yield spacing
                
            else:
                pass


    def spacing_lat_lon( self, coord ):
    
        if len(coord) == 7:
            spacing = ''
        elif len(coord) == 6:
            spacing = ' '
        elif len(coord) == 5:
            spacing = '  ' 
        elif len(coord) == 4:
            spacing = '   ' 
        else:
            pass

        return spacing


    def spacing_elev( self, elev ):
    
        if len(elev) == 6:
            spacing = ''
        elif len(elev) == 5:
            spacing = ' '
        elif len(elev) == 4:
            spacing = '  ' 
        elif len(elev) == 3:
            spacing = '   '
        elif len(elev) == 2:
            spacing = '    '     
        else:
            pass

        return spacing

