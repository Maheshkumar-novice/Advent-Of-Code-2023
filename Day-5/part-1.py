import re

class Parser():
    def __init__(self, data):
        self.next_states = {
            'seeds': 'seed-to-soil map',
            'seed-to-soil map': 'soil-to-fertilizer map',
            'soil-to-fertilizer map': 'fertilizer-to-water map',
            'fertilizer-to-water map': 'water-to-light map',
            'water-to-light map': 'light-to-temperature map',
            'light-to-temperature map': 'temperature-to-humidity map',
            'temperature-to-humidity map': 'humidity-to-location map'
        }

        self.data = data
        self.state = 'seeds'

        self.seeds = []
        self.soil = []
        self.fertilizer = []
        self.water = []
        self.light = []
        self.temperature = []
        self.humidity = []
        self.location = []

        self.seed_to_soil_map = {}
        self.soil_to_fertilizer_map = {}
        self.fertilizer_to_water_map = {}
        self.water_to_light_map = {}
        self.light_to_temperature_map = {}
        self.temperature_to_humidity_map = {}
        self.humidity_to_location_map = {}

    def move_state(self):
        self.state = self.next_states[self.state]

    def parse(self):
        for idx, line in enumerate(self.data):
            # print(f'Parsing line: {idx + 1}, {line}')
            if line == '':
                self.move_state()

            self.current_data = list(map(int, re.findall(r'\d+', line)))
            if self.state == 'seeds':
                self.seeds = self.current_data
            elif self.state == 'seed-to-soil map':
                self._parse_seed_to_soil_map()
            elif self.state == 'soil-to-fertilizer map':
                self._parse_soil_to_fertilizer_map()
            elif self.state == 'fertilizer-to-water map':
                self._parse_fertilizer_to_water_map()
            elif self.state == 'water-to-light map':
                self._parse_water_to_light_map()
            elif self.state == 'light-to-temperature map':
                self._parse_light_to_temperature_map()
            elif self.state == 'temperature-to-humidity map':
                self._parse_temperature_to_humidity_map()
            elif self.state == 'humidity-to-location map':
                self._parse_humidity_to_location_map()

        print(self.seeds, self.seed_to_soil_map)
        for i in self.seeds:
            flag = False
            for key in self.seed_to_soil_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.soil.append(abs(i - key[0]) + self.seed_to_soil_map[key])
            if not flag:
                self.soil.append(i) 

        print(self.soil, self.soil_to_fertilizer_map)
        for i in self.soil:
            flag = False
            for key in self.soil_to_fertilizer_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.fertilizer.append(abs(i - key[0]) + self.soil_to_fertilizer_map[key])
            if not flag:
                self.fertilizer.append(i) 

        print(self.fertilizer, self.fertilizer_to_water_map)
        for i in self.fertilizer:
            flag = False
            for key in self.fertilizer_to_water_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.water.append(abs(i - key[0]) + self.fertilizer_to_water_map[key])
            if not flag:
                self.water.append(i) 

        print(self.water, self.water_to_light_map)
        for i in self.water:
            flag = False
            for key in self.water_to_light_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.light.append(abs(i - key[0]) + self.water_to_light_map[key])
            if not flag:
                self.light.append(i) 

        print(self.light, self.light_to_temperature_map)
        for i in self.light:
            flag = False
            for key in self.light_to_temperature_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.temperature.append(abs(i - key[0]) +  self.light_to_temperature_map[key])
            if not flag:
                self.temperature.append(i) 

        print(self.temperature, self.temperature_to_humidity_map)
        for i in self.temperature:
            flag = False
            for key in self.temperature_to_humidity_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.humidity.append(abs(i - key[0]) +  self.temperature_to_humidity_map[key])
            if not flag:
                self.humidity.append(i) 

        print(self.humidity, self.humidity_to_location_map)
        for i in self.humidity:
            flag = False
            for key in self.humidity_to_location_map.keys():
                if i >= key[0] and i <= key[1]:
                    flag = True
                    self.location.append(abs(i - key[0]) + self.humidity_to_location_map[key])
            if not flag:
                self.location.append(i) 

        print(self.location)
        print(min(self.location))

    def _parse_seed_to_soil_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.seed_to_soil_map[(source, source + incr)] = dest

    def _parse_soil_to_fertilizer_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.soil_to_fertilizer_map[(source, source + incr)] = dest

    def _parse_fertilizer_to_water_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.fertilizer_to_water_map[(source, source + incr)] = dest

    def _parse_water_to_light_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.water_to_light_map[(source, source + incr)] = dest

    def _parse_light_to_temperature_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.light_to_temperature_map[(source, source + incr)] = dest

    def _parse_temperature_to_humidity_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.temperature_to_humidity_map[(source, source + incr)] = dest

    def _parse_humidity_to_location_map(self):
        if not self.current_data: return

        dest = self.current_data[0]
        source = self.current_data[1]
        incr = self.current_data[-1]

        self.humidity_to_location_map[(source, source + incr)] = dest


with open('input.txt', 'r') as f:
    file = f.read().splitlines()
    Parser(file).parse()
