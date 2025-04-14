class ServeReceiveStats:
    def __init__(self) -> None:
        self.perfect_serves = 0
        self.great_serves = 0
        self.medium_serves = 0
        self.poor_serves = 0
        self.serve_errors = 0
        self.total_serves = 0
        self.in_system_percentage = 0.0
        self.out_of_system_percentage = 0.0
        self.serve_average = 0.0

    def set_perfect_serves(self, perfect_serves: int) -> None:
        '''
        Set the number of perfect serves from the player serve receive stats.
        '''
        self.perfect_serves = perfect_serves

    def set_great_serves(self, great_serves: int) -> None:
        '''
        Set the number of great serves from the player serve receive stats.
        '''
        self.great_serves = great_serves

    def set_medium_serves(self, medium_serves: int) -> None:
        '''
        Set the number of medium serves from the player serve receive stats.
        '''
        self.medium_serves = medium_serves

    def set_poor_serves(self, poor_serves: int) -> None:
        '''
        Set the number of poor serves from the player serve receive stats.
        '''
        self.poor_serves = poor_serves

    def set_serve_errors(self, serve_errors: int) -> None:
        '''
        Set the number of serve errors from the player serve receive stats.
        '''
        self.serve_errors = serve_errors

    def set_total_serves(self, total_serves: int) -> None:
        '''
        Set the total number of serves from the player serve receive stats.
        '''
        self.total_serves = total_serves

    def set_in_system_percentage(self, in_system_percentage: float) -> None:
        '''
        Set the in-system percentage of the serve receive stats.
        '''
        self.in_system_percentage = in_system_percentage

    def set_out_of_system_percentage(self, out_of_system_percentage: float) -> None:
        '''
        Set the out-of-system percentage of the serve receive stats.
        '''
        self.out_of_system_percentage = out_of_system_percentage

    def set_serve_average(self, serve_average: float) -> None:
        '''
        Set the average of the serve receive stats.
        '''
        self.serve_average = serve_average
        
        

    