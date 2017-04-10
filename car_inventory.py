import sys

class Car_logic():
    '''
    From a file of car makers and a file of corresponding car models:
    read the list of car makers,
    read the list of car models
    create a dictionary of makers and models
    '''

    def read_car_makes():
        ''' read the car_makes.txt file '''
        with open('car_makes.txt', 'r') as make_reader:
            # print(make_reader.read())
            return make_reader.readlines()

    def read_car_models():
        ''' read the car_models file '''
        with open('car_models', 'r') as model_reader:
            return model_reader.readlines()

    def create_car_dictionary():
        ''' create a dictionary of makers and models '''
        car_dictionary = {}
        car_make_data = Car_logic.read_car_makes()
        car_model_data = Car_logic.read_car_models()
        for maker in car_make_data:
            car_dictionary[maker.rstrip()] = []
            for model in car_model_data:
                make_identifier = model[0]
                if make_identifier == maker[0]:
                    model_name = model[2:].rstrip()
                    car_dictionary[maker.rstrip()].append(model_name)
        print(car_dictionary)

Car_logic.create_car_dictionary()